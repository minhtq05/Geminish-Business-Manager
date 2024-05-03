import json
import re
import time
from typing import List
from datetime import datetime, timedelta
from rich import print, inspect


from src.api.config import GEMINI_API_KEY_BACKUP
from src.api.gmail.service import GmailService
from src.api.gemini.agents import GeminiCustomerFeedbackAgent
from src.api.firestore.firestore import FirestoreDB
from src.api.types import Message, Product
from src.api.types import JiraTicket
from src.api.jira.agent import Jira
from src.format import json_clean

# This is a test function only.
# Remember to change the random module with an id generator

"""
The Business class will pack every services needed for a business
Features:
- a Gmail API service
- Gemini and other AI API services
- a FireStore database
"""


class BusinessAgent():
    def __init__(self, business_name: str, products: List[Product]):
        self.products = products
        self.business_name = business_name
        self._firestoredb = FirestoreDB(
            business_name=business_name, auto_init=True)

        _gmail_token = self._firestoredb.get_gmail_token()
        self._gmail_service = GmailService(
            business_name=business_name, gmail_token=_gmail_token)

        if _gmail_token is None:
            token = json.loads(self._gmail_service.gmail_token)
            self._firestoredb.save_gmail_token(token)

        self._gemini_agent = GeminiCustomerFeedbackAgent(
            business_name=business_name, products=products)

        self.raw_messages = None
        self.reports = None
        self._jira = Jira()
        print(f"""Business '{business_name}' initialized!
You can now use all the features of this business!""")

    def timeit(func):
        def wrapper(self, *args, **kwargs):
            start = datetime.now()
            print(f"Start running function [green]{func.__name__}[/]")
            result = func(self, *args, **kwargs)
            print(f"Function: [green]{func.__name__}[/], execution time: {(datetime.now() - start).seconds} s.")
            return result
        return wrapper

    def inspect(self):
        print("Here is the inspection of this business class: ")
        inspect(self, private=True)
        print("Here are all the features of this business: ")
        inspect(self._gmail_service, private=True)
        inspect(self._gemini_agent, private=True)
        inspect(self._firestoredb, private=True)

    def unix_time(self, time: datetime):
        return datetime.timestamp(time)

    @timeit
    def get_raw_messages(self) -> List[Message]:
        self.add_new_messages()
        # if not found give the first day of 2000
        if self.raw_messages is None or (datetime.now() - self.raw_messages.get("updated_on", datetime.min) > timedelta(hours=1)):
            self.raw_messages = {
                "messages": self._gmail_service.get_all_messages(),
                "updated_on": datetime.now(),
            }
        return self.raw_messages

    @timeit
    def get_reports(self):
        def json_clean(text):
            json_match = re.search(r"```json\s*(.*?)\s*```", text, re.DOTALL)
            if json_match:
                return json_match.group(1)
            else:
                return "Something went wrong when cleaning json!"

        def filter(messages: List[Message]):
            """
            Accept only the first 250 words of a message
            """
            filtered_messages = messages
            for i in range(len(filtered_messages)):
                filtered_messages[i]['body'] = ' '.join(filtered_messages[i]['body'].split(' ')[
                    :250])

            return filtered_messages

        # if self.reports is None:
        #     self.reports = self._firestoredb.get_reports()
        #     self.reports['updated_on'] = datetime.fromtimestamp(
        #         self.reports['updated_on'].timestamp())

        # if not found give the first day of 2000
        if self.reports is None or (datetime.now() - self.reports.get("updated_on", datetime.min) > timedelta(hours=1)):
            gemini_report = self._gemini_agent.get_feedback_report(
                filter(self.get_raw_messages()["messages"]))
            print("Calling gemini agent to get reports...")
            error_count = 0
            while True:
                try:
                    reports = json.loads(json_clean(gemini_report))
                    break
                except:
                    error_count += 1
                    print(
                        "Something went wrong when cleaning json! Error count:", error_count)

            reports = {
                "reports": reports,
                "updated_on": datetime.now(),
            }
            self._firestoredb.load_new_reports(reports)
            self.reports = reports

        return self.reports

    def existing_message_ids(self):
        return self._firestoredb.get_existing_message_ids()

    def add_new_messages(self):
        # Need optimization later!!!
        message_ids = self._gmail_service.get_all_messages_id()
        existing_message_ids = self.existing_message_ids()

        messages = []

        for id in message_ids:
            if id not in existing_message_ids:
                messages.append(id)

        messages = [self._gmail_service.get_message_by_id(
            id) for id in messages]

        self._firestoredb.add_messages(messages)

    def get_filtered_messages(self) -> List[Message]:
        messages = self._gmail_service.get_all_messages()
        filtered_messages = self._gemini_agent.filter_messages(messages)
        return filtered_messages

    def get_reports_summarize(self, reports: List[dict]):
        pass

    def get_improvements_options(self) -> dict:
        """
        dict structure:
        {'product_name': [[summary 1, description 1], [summary 2, description 2]]                 [summary 3, description 3]]}
        Use Gemini AI to generate a product improvement options from filtered messages
        """
        options = None
        for i in range(3):
            try:
                options = self._gemini_agent.create_improvements_option(
                    self.get_filtered_messages())
                options = re.sub("\'", "\"", options)
                options = json_clean(options)
                options = json.loads(options)
                print(options)
                break
            except Exception as e:
                print(f'Error: {e}. Trying again')
                print('Number of tries:', i+1)
                self._gemini_agent = GeminiCustomerFeedbackAgent(
                         business_name=self.business_name,
                         products=self.products,
                         api = GEMINI_API_KEY_BACKUP
                        )
                # if '429' in e:
                #     self._gemini_agent = GeminiCustomerFeedbackAgent(
                #         business_name=self.business_name,
                #         products=self.products,
                #         api = GEMINI_API_KEY_BACKUP
                #     )
                options = {}
                time.sleep(2)
                pass
        return options

    def upload_issue(self, payload: List[JiraTicket]) -> List:
        """
        payload: list of Jira tickets that need to be uploaded
        Upload all ticket from payload to Jira
        """
        jira_response = [self._jira.upload_issue(issue) for issue in payload]
        jira_response = [json.loads(response.text) for response in jira_response]
        return jira_response

    def get_all_issue(self, key: str) -> List[JiraTicket]:
        """
        key: Jira project chosen to upload the issue
        return a list of JiraTicket
        create a list of JiraTicket from list of improvement options
        """
        option_list_raw = self.get_improvements_options()
        ticket_list = []
        for product, options in option_list_raw.items():
            jira_ticket_list = self._jira.option_to_jira(key, product, options)
            ticket_list.extend(jira_ticket_list)
            print(ticket_list)
        return ticket_list

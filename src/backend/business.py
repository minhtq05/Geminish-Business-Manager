import json
import re
from src.api.gmail.service import GmailService
from src.api.gemini.agents import GeminiCustomerFeedbackAgent
from src.api.firestore.firestore import FirestoreDB
from rich import inspect
from typing import List
from src.api.types import Message, Product, JiraTicket
from src.api.jira.agent_jira import Jira
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
        self._firestoredb = FirestoreDB(business_name=business_name, auto_init=True)

        _gmail_token = self._firestoredb.get_gmail_token()
        self._gmail_service = GmailService(business_name=business_name, gmail_token=_gmail_token)
        
        if _gmail_token is None:
            token = json.loads(self._gmail_service.gmail_token)
            self._firestoredb.save_gmail_token(token)

        self._gemini_agent = GeminiCustomerFeedbackAgent(business_name=business_name, products=products)
        self._jira = Jira()
        print(f"""Business '{business_name}' initialized!
You can now use all the features of this business!""")
        

    def inspect(self):
        print("Here is the inspection of this business class: ")
        inspect(self, private=True)
        print("Here are all the features of this business: ")
        inspect(self._gmail_service, private=True)
        inspect(self._gemini_agent, private=True)
        inspect(self._firestoredb, private=True)


    def get_raw_messages(self) -> List[Message]:
        return self._firestoredb.get_all_messages()
    

    def get_reports(self):
        def json_clean(text):
            json_match = re.search(r"```json\s*(.*?)\s*```", text, re.DOTALL)
            if json_match:  
                return json_match.group(1)
            else:
                return "Something went wrong when cleaning json!"
        messages = self._gmail_service.get_all_messages()
        messages = self._gemini_agent.filter_messages(messages)
        json.loads(json_clean(self._gemini_agent.get_feedback_report(messages)))
        return json.loads(json_clean(self._gemini_agent.get_feedback_report(messages)))


    def existing_message_ids(self):
        return self._firestoredb.get_existing_message_ids()

    def load_new_messages(self):
        # Need optimization later!!!
        message_ids = self._gmail_service.get_all_messages_id()
        existing_message_ids = self.existing_message_ids()

        messages = []

        for id in message_ids:
            if id not in existing_message_ids:
                messages.append(id)

        messages = [self._gmail_service.get_message_by_id(id) for id in messages]

        self._firestoredb.add_messages(messages)
    def get_filtered_messages(self):
        messages = self._gmail_service.get_all_messages()
        filtered_messages = self._gemini_agent.filter_messages(messages)
        return filtered_messages

    def get_reports_summarize(self, reports: List[dict]):
        pass
    def get_improvements_options(self) -> dict:
        # {'product_name': [[summary 1, description 1],
        #                   [summary 2, description 2],
        #                   [summary 3, description 3]]}
        options = None
        for i in range(3):
            try:
                options = self._gemini_agent.create_improvements_option(self.get_filtered_messages())
                options = re.sub("\'", "\"", options)
                options = json_clean(options)
                options = json.loads(options)
                print(options)
                break
            except Exception as e:
                print(f'Error: {e}. Trying again')
                print('Number of tries:', i)
                pass
        return options

    def upload_issue(self,payload: List[JiraTicket]) -> dict:
        """
        payload: list of Jira tickets that need to be uploaded
        Upload all ticket from payload to Jira
        """
        #[JiraTicket]
        # option_list_raw = self.get_improvements_options()
        #
        # payload = []
        #
        # for product in option_list_raw:
        #     print(f'Here the improvement options for {product} and its description')
        #     for i, option in enumerate(option_list_raw[product]):
        #         print(f'Option {i + 1}: {option}')
        #     for tries in range(len(option_list_raw[product])):
        #         print(f'Choose option number you want to upload as jira ticket for {product}')
        #         choice = input()
        #         if choice == 'None':
        #             break
        #         choice = int(choice) - 1
        #         payload += self._jira.option_to_jira(project_key, product, option_list_raw[product][choice])
        #         print(payload)
        for issue in payload:
            res = self._jira.upload_issue(issue)
            return json.loads(res.text)

    def get_all_issue(self, key: str) -> List[JiraTicket]:
        """
        key: Jira project chosen to upload the issue
        return a list of JiraTicket
        create a list of JiraTicket from list of improvement options
        """
        option_list_raw = self.get_improvements_options()
        ticket_list = []
        for product in option_list_raw:
            ticket_list += self._jira.option_to_jira(key, product, option_list_raw[product])
        return ticket_list
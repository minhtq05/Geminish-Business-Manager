import random
import os
import json
from src.api.gmail.service import GmailService
from src.api.gemini.agents import GeminiCustomerFeedbackAgent
from src.api.firestore.firestore import FirestoreDB
from rich import print, inspect
from typing import List
from src.api.types import Message, Product
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
        self._firestoredb = FirestoreDB(business_name=business_name, auto_init=True)

        _gmail_token = self._firestoredb.get_gmail_token()
        self._gmail_service = GmailService(business_name=business_name, gmail_token=_gmail_token)
        
        if _gmail_token is None:
            token = json.loads(self._gmail_service.gmail_token)
            self._firestoredb.save_gmail_token(token)


        self._gemini_agent = GeminiCustomerFeedbackAgent(business_name=business_name, products=products)
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
        return self._gmail_service.get_all_messages()
    

    def get_reports(self, messages: List[Message]):
        return self._gemini_agent.get_feedback_report(messages)



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


    def get_reports_summarize(self, reports: List[dict]):
        pass

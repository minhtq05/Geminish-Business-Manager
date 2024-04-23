import os.path
import base64
import re
import json
from typing import Dict
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from src.api.types import Message
from src.api.config import GMAIL_API_CREDENTIAL

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# This gmail api is owned by this product, not the business using it!
# It is used for using and billing the Gmail API!
GMAIL_API_CREDENTIAL = GMAIL_API_CREDENTIAL



# The main Gmail API service for loading messages, sending emails, and many other functionalities.
class GmailService():
    def __init__(self, business_name: str, gmail_token: Dict) -> None | Exception:
        self._business_name = business_name
        self.gmail_token = gmail_token # This one is a credential dict and need to be kept as a secret!
        self._service, self.gmail_token = self._gmail_service()


    def get_all_messages_id(self, from_date=None):
        # Get the ids of all the messages.
        data = self._service.users().messages().list(userId='me').execute()
        message_ids = [message['id']
                           for message in data.get('messages', [])]
        return message_ids


    def get_raw_message_by_id(self, message_id):
        message = self._service.users().messages().get(
            userId='me', id=message_id).execute()
        return message


    def get_message_by_id(self, message_id):
        # Get the content of a single message searched using the given id.
        message = self.get_raw_message_by_id(message_id)

        labels = message.get('labelIds', [])

        payload = message.get('payload', {})

        headers = payload.get('headers', [])

        sender, receiver, send_date, content_type, subject = None, None, None, None, None

        for item in headers:
            match item.get('name', ''):
                case 'From':
                    sender = item.get('value', '').split(' <')
                    if len(sender) == 1:
                        sender = {'name': sender[0].strip(
                            '\"'), 'email': sender[0]}
                    else:
                        sender = {'name': sender[0].strip(
                            '\"'), 'email': sender[1][:-1]}
                case 'To':
                    receiver = item.get('value', '').split(' <')
                    if len(receiver) == 1:
                        receiver = {'name': receiver[0].strip(
                            '\"'), 'email': receiver[0]}
                    else:
                        receiver = {'name': receiver[0].strip(
                            '\"'), 'email': receiver[1][:-1]}
                case 'Date':
                    send_date = item.get('value', '')
                case 'Content-Type':
                    content_type = item.get('value', '')
                case 'Subject':
                    subject = item.get('value', '')
                case _:
                    pass

        if content_type.startswith('text/plain'):
            body = payload.get('body', {}).get('data', '')
        else:
            parts = payload.get('parts', [])
            body = ""
            for part in parts:
                if (part.get('mimeType', '') == 'text/plain'):
                    body = part.get('body', {}).get('data', '')
                    break

        body = base64.urlsafe_b64decode(body).decode('utf-8')
        # body = re.sub('\u200c', '', body)
        body = re.sub('\r\n\r\n','\n', body)
        body = re.sub('\r\n', ' ', body)
        # body = body.split('\r\n')
        # body = re.sub('<.*?>', '', '\n'.join(body))

        return Message(message_id, sender, receiver, send_date, content_type, labels, subject, body)


    def get_all_messages(self):
        # Get the contents of all the messages. Might be slow at the moment for large number of messages.
        ids = self.get_all_messages_id()
        msgs = [self.get_message_by_id(id) for id in ids]
        return msgs


    # This is the sample code from Gmail APi documentation.
    # Please visit https://developers.google.com/gmail/api/quickstart/python for more information on how to set up the Gmail API.
    def _gmail_service(self):
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        # if os.path.exists(f"src/api/gmail/business_credentials/{self._business_id}/token.json"):
            # creds = Credentials.from_authorized_user_file(f"src/api/gmail/business_credentials/{self._business_id}/token.json", SCOPES)
        if self.gmail_token is not None:
            creds = Credentials.from_authorized_user_info(self.gmail_token, SCOPES)
        else:
            creds = None
        
        token = None
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    #   "credentials.json", SCOPES
                    f"src/api/gmail/{GMAIL_API_CREDENTIAL}", SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            # with open(f"src/api/gmail/business_credentials/{self._business_id}/token.json", "w") as token:
            #     token.write(creds.to_json())

            token = creds.to_json()

        try:
            # Call the Gmail API
            service = build("gmail", "v1", credentials=creds)
            # results = service.users().labels().list(userId="me").execute()
            # labels = results.get("labels", [])

            print("Gmail API services intialized")

            return (service, token)

            # if not labels:
            #   print("No labels found.")
            #   return
            # print("Labels:")
            # for label in labels:
            #   print(label["name"])

        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f"An error occurred: {error}")
            return (None, None)


if __name__ == '__main__':
    print("""
Gmail API services for scraping email data.
""")

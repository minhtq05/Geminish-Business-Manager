import os.path
import base64
import re
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from api.types import Message

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

CREDENTIAL = "client_secret_877330635552-7f159rmq44osoihigpv21u44f5h983r6.apps.googleusercontent.com.json"

# class Message():
#     def __init__(self, id, sender, receiver, send_date, content_type, labels, subject, body):
#         self.id = id
#         self.sender = sender
#         self.receiver = receiver
#         self.send_date = send_date
#         self.content_type = content_type
#         self.labels = labels
#         self.subject = subject
#         self.body = body

#     def __str__(self):
#         return {
#             'type': 'Gmail Message',
#             'id': self.id,
#             'sender': self.sender,
#             'receiver': self.receiver,
#             'send_date': self.send_date,
#             'content_type': self.content_type,
#             'labels': self.labels,
#             'subject': self.subject,
#             'body': self.body
#         }
#
#     def __repr__(self):
#         return self.__str__()


# The main Gmail API service for loading messages, sending emails, and many other functionalities.
class GmailService():
    def __init__(self):
        self.service = gmail_service()
        pass

    def get_messages_id(self, from_date=None):
        # Get the ids of all the messages.
        data = self.service.users().messages().list(userId='me').execute()
        message_id_list = [message['id']
                           for message in data.get('messages', [])]
        return message_id_list

    def get_raw_message(self, message_id):
        message = self.service.users().messages().get(
            userId='me', id=message_id).execute()
        return message

    def get_message(self, message_id):
        # Get the content of a single message searched using the given id.
        message = self.get_raw_message(message_id)

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

        body = base64.urlsafe_b64decode(body).decode('utf-8').split('\r\n')
        body = re.sub('<.*?>', '', '\n'.join(body))

        return Message(message_id, sender, receiver, send_date, content_type, labels, subject, body)

    def get_messages_list(self):
        # Get the contents of all the messages. Might be slow at the moment for large number of messages.
        ids = self.get_messages_id()
        msgs = [self.get_message(id) for id in ids]
        return msgs


# This is the sample code from Gmail APi documentation.
# Please visit https://developers.google.com/gmail/api/quickstart/python for more information on how to set up the Gmail API.

def gmail_service():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                #   "credentials.json", SCOPES
                f"api/gmail/{CREDENTIAL}", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build("gmail", "v1", credentials=creds)
        # results = service.users().labels().list(userId="me").execute()
        # labels = results.get("labels", [])

        print("Gmail API services intialized")

        return service

        # if not labels:
        #   print("No labels found.")
        #   return
        # print("Labels:")
        # for label in labels:
        #   print(label["name"])

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")
        return None


if __name__ == '__main__':
    print("""
Gmail API services for scraping email data.
""")

import firebase_admin
from firebase_admin import credentials, firestore
from src.api.gmail.service import Message
from typing import List, Union
from datetime import datetime

#! Remember to get credentials from Firebase Console save it in the same directory as this file
cred = credentials.Certificate("src/api/firestore/firebase-credentials.json")

app = firebase_admin.initialize_app(cred)
db = firestore.client()

def add_emails(emails_list: List[Message]) -> None:
    for email in emails_list:
        new_document = db.collection("messages").document()
        new_document.set({
            'type': 'feedback',
            'id': email["id"],
            'sender': email["sender"],
            'receiver': email["receiver"],
            'send_date': email["send_date"],
            'content_type': email["content_type"],
            'labels': email["labels"],
            'subject': email["subject"],
            'body': email["body"]
        })

def get_all_emails() -> List[Message]:
    output = []
    # create reference to email collection in db
    emails_collection_ref = db.collection("messages")
    emails = emails_collection_ref.stream()
    
    for email in emails:
        output.append(email)
    return output

def delete_email_by_id(query_id: str) -> None:
    emails_collection_ref = db.collection("messages")
    emails_to_delete = emails_collection_ref.where("id", "==", query_id).stream()
    
    for email in emails_to_delete:
        email.reference.delete()

def get_email_by_id(query_id: str) -> Union[Message, None]:
    emails_collection_ref = db.collection("messages")
    email_with_id = emails_collection_ref.where("id", "==", query_id).stream()
    
    if not email_with_id:
        return None
    return email_with_id[0]
        
def update_email_by_id(query_id: str, new_email: Message) -> None:
    emails_collection_ref = db.collection("messages")
    emails_to_update = emails_collection_ref.where("id", "==", query_id).stream()
    
    for email in emails_to_update:
        email.reference.update(new_email)
    
def get_email_by_date(query_date: datetime) -> List[Message]:
    # can change to string 9
    # asusume email's send date format as 04/12/2024 time abc abc
    output = []
    formatted_query_date = query_date.strftime("%m/%d/%Y")
    emails_collection = db.collection("messages").stream()
    
    for email in emails_collection:
        doc_date = email.to_dict()["send_date"][:11]
        if doc_date == formatted_query_date:
            output.append(email)
    return output

def get_email_by_range(start_query_date: datetime, end_query_date: datetime) -> List[Message]:
    output = []
    emails_collection = db.collection("messages").stream()
    start_date = start_query_date.date()
    end_date = end_query_date.date()
    
    for email in emails_collection:
        curr_date = datetime.strptime(email.to_dict()["send_date"], "%m/%d/%Y").date()
        if start_date <= curr_date <= end_date:
            output.append(email)
    return output

if __name__ == "__main__":
    print("Test getting email")
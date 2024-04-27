import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from src.api.types import Message, User
from src.api.config import FIREBASE_API_CREDENTIAL
from typing import List, Union
from datetime import datetime, timedelta
from rich import print


# all methods inside this module will only belong to the business you have initialized using init_business!
# USE WITH CAUTION!


#! Remember to get credentials from Firebase Console save it in the same directory as this file, put its name to an .env file, and name it as FIREBASE_CREDENTIAL.
#! Also remember to remove your credential from 
cred = credentials.Certificate(f"src/api/firestore/{FIREBASE_API_CREDENTIAL}")

"""
Businesses can have existing databases with different names for their users and messages databases.
"""
collections = {
    "users": "users",
    "messages": "messages",
}

app = firebase_admin.initialize_app(cred)
db = firestore.client()

business_db = None
users_collection_ref = None
emails_collection_ref = None


def check_empty_query(query, error: Exception = None) -> bool:
    if not query:
        if error != None:
            raise error
        return True

    return False


def validate_field(field, field_name: str) -> None:
    if field is None:
        raise ValueError(f"Field {field_name} cannot be None")


def check_db_references() -> None:
    if business_db is None:
        raise AttributeError("Attribute 'business_db' is not initialized correctly. Please run init_business(business_name) first to initialize the business's database you are trying to access first!")


def init_business(business_name: str) -> bool:
    global users_collection_ref, emails_collection_ref
    """
    Run this function first to initialize the business you are working on
    """
    query = (
        db.collection("businesses")
        .where(filter=FieldFilter("name", "==", business_name))
        .limit(1)
        .stream()
    )

    check_empty_query(query, ValueError(f"No business found under the name '{business_name}'!"))

    query = next(query)

    business_id = query.id
    business_db = db.collection("businesses").document(business_id)
    users_collection_ref = business_db.collection(collections["users"])
    emails_collection_ref = business_db.collection(collections["messages"])


def add_emails(emails_list: List[Message]) -> None:
    for email in emails_list:
        emails_collection_ref.set({
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
    emails = (emails_collection_ref.stream())
    
    for email in emails:
        output.append(email.to_dict())
    return output


def delete_email_by_id(query_id: str) -> None:
    emails_to_delete = (
        emails_collection_ref
        .where("id", "==", query_id)
        .limit(1)
        .stream()
    )

    for email in emails_to_delete:
        email.reference.delete()


def get_email_by_id(query_id: str) -> Union[Message, None]:
    email_with_id = (
        emails_collection_ref
        .where("id", "==", query_id)
        .limit(1)
        .stream()
    )
    
    if not email_with_id:
        return None
    return email_with_id[0]
        

def update_email_by_id(query_id: str, new_email: Message) -> None:
    emails_to_update = (
        emails_collection_ref
        .where("id", "==", query_id)
        .limit(1)
        .stream()
    )
    
    for email in emails_to_update:
        email.reference.update(new_email)
    

def get_email_by_date(query_date: datetime) -> List[Message]:
    # Query returning every messages sent during query_date, from 00:00:00 am to 11:59:59 pm
    output = []
    date_begin = query_date.timestamp()
    date_end = (query_date + timedelta(days=1))
    # formatted_query_date = query_date.strftime("%m/%d/%Y")
    emails_collection = (
        emails_collection_ref
        .where(filter=FieldFilter("send_date", ">=", date_begin))
        .where(filter=FieldFilter("send_date", "<", date_end))
        .stream()
    )
    
    for email in emails_collection:
        output.append(email)
    return output


def get_email_by_range(start_query_date: datetime, end_query_date: datetime) -> List[Message]:
    output = []
    start_date = start_query_date.timestamp()
    end_date = end_query_date.timestamp()

    emails_collection = (
        emails_collection_ref
        .where(filter=FieldFilter("send_date", ">=", start_date))
        .where(filter=FieldFilter("send_date", "<=", end_date))
    )
    
    for email in emails_collection:
        output.append(email)
    return output


def user_exists(email: str) -> bool | User:
    validate_field(email, "email")
    
    query = (
        users_collection_ref
        .where(filter=FieldFilter("email", "==", email))
        .limit(1)
        .stream()
    )
    
    return False if query is None else next(query)


def register_new_user(email: str, password: str, is_admin: bool = False) -> bool | Exception:
    validate_field(email, "email")
    validate_field(password, "password")

    if user_exists(email):
        return ValueError(f"User with email {email} already exists!")

    users_collection_ref.add({
        "email": email,
        "password": password,
        "created_on": datetime.now(),
        "is_admin": is_admin,
    })


def authenticate_user(email: str, password: str) -> bool | Exception:
    user = user_exists(email)
    if not user:
        return ValueError(f"No user found under email {email}")

    if user.to_dict()["password"] != password: # Need to use hash later
        return ValueError(f"Password is incorrect!")

    return True    


if __name__ == "__main__":
    print("Test getting email")
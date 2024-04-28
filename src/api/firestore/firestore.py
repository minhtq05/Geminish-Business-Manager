import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin.firestore import Query
from google.cloud.firestore_v1.base_query import FieldFilter
from src.api.types import Message, User, Report
from src.api.config import FIREBASE_API_CREDENTIAL
from typing import List, Union, Dict
from datetime import datetime, timedelta
from rich import print

"""
To-do list:
- Remove init_business and give each business a unique firestore databse reference

"""

cred = credentials.Certificate(f"{FIREBASE_API_CREDENTIAL}")
app = firebase_admin.initialize_app(cred)
db = firestore.client()


def Config(users: str = "users", messages: str = "messages"): 
    return {
        "users": users,
        "messages": messages,
    }


# all methods inside this module will only belong to the business you have initialized using init_business!
# USE WITH CAUTION!


#! Remember to get credentials from Firebase Console save it in the same directory as this file, put its name to an .env file, and name it as FIREBASE_CREDENTIAL.
#! Also remember to remove your credential from 

"""
Businesses can have existing databases with different names for their users and messages databases.
"""

class FirestoreDB():
    def __init__(self, business_name: str, collection_config: Config = Config(), auto_init: bool = False) -> None:
        self.business_name = business_name
        self.collections = {
            "users": "users",
            "messages": "messages",
        }

        self._business_db = None
        self._users_collection_ref = None
        self._emails_collection_ref = None
        self.is_initialized = False
        self._auto_init = auto_init

        
        self.info = self.business_exists(business_name)

        if self.info is None:
            if self._auto_init:
                self.init_business(self.business_name)
                print(f"Warning: No business found under the name '{business_name}'! However, auto_init is set to True so wae already initialized the business for you!")
            else:
                print(f"Warning: No business found under the name '{business_name}'! Please initialize the business using the 'init_business' method first!")
        else:
            self.info = {
                "id": self.info.id,
                "name": business_name,
                "created_on": self.info.to_dict().get("created_on", None),
            }
            self._business_id = self.info["id"]
            self.is_initialized = True

        if self.is_initialized:
            self.load_data()


    def timeit(func):
        def wrapper(self, *args, **kwargs):
            start = datetime.now()
            print(f"Start running function [green]{func.__name__}[/]")
            result = func(self, *args, **kwargs)        
            print(f"Function: [green]{func.__name__}[/], execution time: {(datetime.now() - start).seconds} s.")
            return result
        return wrapper

    @timeit
    def load_data(self):
        if self.is_initialized:
            self._business_db = db.collection("businesses").document(self._business_id)
            self._users_collection_ref = self._business_db.collection(self.collections["users"])
            self._emails_collection_ref = self._business_db.collection(self.collections["messages"])
            self._report_doc = self._business_db.collection("reports").document("reports")


    def initialize_required(func):
        def wrapper(self, *args, **kwargs):
            if not self.is_initialized:
                raise ValueError("Business is not initialized!")
            return func(self, *args, **kwargs)
        return wrapper
        

    def business_exists(self, business_name) -> None | Query: 
        query = (
            db.collection("businesses")
            .where(filter=FieldFilter("name", "==", business_name))
            .limit(1)
            .stream()
        )

        if self.empty_query(query):
            return None
        else:
            return next(query, None)

    @timeit
    def init_business(self, business_name: str) -> None:
        if self.is_initialized:
            raise Warning("Business is already initialized!")
            return

        (_, data) = db.collection("businesses").add({
            "name": business_name,
            "created_on": datetime.now(),
        })

        data = data.get()

        self.info = {
            "id": data.id,
            "name": business_name,
            "created_on": data.to_dict().get("created_on", None),
        }
        self._business_id = self.info["id"]
        self.is_initialized = True
        self.load_data()


    def empty_query(self, query, error: Exception = None) -> bool:
        if query is None:
            if error != None:
                raise error
            return True

        return False


    def validate_field(self, field, field_name: str) -> None:
        if field is None:
            raise ValueError(f"Field {field_name} cannot be None")
        
    @timeit
    def get_gmail_token(self) -> Dict:
        query = self._emails_collection_ref.document("token").get()
        return query.to_dict()
    
    @timeit
    def save_gmail_token(self, token: Dict):
        self._emails_collection_ref.document("token").set(token)
        

    @initialize_required
    def add_messages(self, emails_list: List[Message]) -> None:
        if len(emails_list) == 0:
            return
        new_message_ids = {}
        for email in emails_list:
            self._emails_collection_ref.document(email["id"]).set({
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
            new_message_ids[email["id"]] = datetime.now()

        self._emails_collection_ref.document("existing_message_ids").update(new_message_ids)
        print(f"Add/Update new {len(emails_list)} message(s) to the database!")

    @timeit
    def get_existing_message_ids(self) -> List[str]:
        doc = self._emails_collection_ref.document("existing_message_ids").get()
        if not doc.exists:
            if self._auto_init:
                self._emails_collection_ref.document("existing_message_ids").st({})
                return {}
            else:
                raise RuntimeError("File 'existing_message_ids' does not exist!")
        return doc.to_dict()


    @initialize_required
    @timeit
    def get_all_messages(self) -> List[Message]:
        output = []
        # create reference to email collection in db
        emails = (self._emails_collection_ref.stream())
        
        for email in emails:
            output.append(email.to_dict())
        return output


    @initialize_required
    @timeit
    def delete_messages_by_id(self, query_id: str) -> None:
        emails_to_delete = (
            self._emails_collection_ref
            .where("id", "==", query_id)
            .limit(1)
            .stream()
        )

        for email in emails_to_delete:
            email.reference.delete()


    @initialize_required
    @timeit
    def get_message_by_id(self, query_id: str) -> Union[Message, None]:
        email_with_id = (
            self._emails_collection_ref
            .where("id", "==", query_id)
            .limit(1)
            .stream()
        )
        
        if not email_with_id:
            return None
        return email_with_id[0]
            

    @initialize_required
    @timeit 
    def update_message_by_id(self, query_id: str, new_email: Message) -> None:
        emails_to_update = (
            self._emails_collection_ref
            .where("id", "==", query_id)
            .limit(1)
            .stream()
        )
        
        for email in emails_to_update:
            email.reference.update(new_email)
        
        
    @initialize_required
    @timeit
    def get_message_by_date(self, query_date: datetime) -> List[Message]:
        # Query returning every messages sent during query_date, from 00:00:00 am to 11:59:59 pm
        output = []
        date_begin = query_date.timestamp()
        date_end = (query_date + timedelta(days=1))
        # formatted_query_date = query_date.strftime("%m/%d/%Y")
        emails_collection = (
            self._emails_collection_ref
            .where(filter=FieldFilter("send_date", ">=", date_begin))
            .where(filter=FieldFilter("send_date", "<", date_end))
            .stream()
        )
        
        for email in emails_collection:
            output.append(email)
        return output


    @initialize_required
    @timeit
    def get_email_by_range(self, start_query_date: datetime, end_query_date: datetime) -> List[Message]:
        output = []
        start_date = start_query_date.timestamp()
        end_date = end_query_date.timestamp()

        emails_collection = (
            self._emails_collection_ref
            .where(filter=FieldFilter("send_date", ">=", start_date))
            .where(filter=FieldFilter("send_date", "<=", end_date))
        )
        
        for email in emails_collection:
            output.append(email)
        return output
    
    @timeit
    def load_new_reports(self, reports: Dict[str, List[Report]]):
        """
        Overwrite the old feedback reports
        """
        self._report_doc.set(reports)

    @timeit
    def get_reports(self) -> Dict[str, List[Report]]:
        """
        Get all feedbacl reports
        """
        doc = self._report_doc.get()
        return doc.to_dict()

    @initialize_required
    @timeit
    def user_exists(self, email: str):
        self.validate_field(email, "email")
        
        query = (
            self._users_collection_ref
            .where(filter=FieldFilter("email", "==", email))
            .limit(1)
            .stream()
        )
        
        return False if query is None else next(query)


    @initialize_required
    @timeit
    def register_new_user(self, email: str, password: str, is_admin: bool = False) -> bool | Exception:
        self.validate_field(email, "email")
        self.validate_field(password, "password")

        if self.user_exists(email):
            return ValueError(f"User with email {email} already exists!")

        self._users_collection_ref.add({
            "email": email,
            "password": password,
            "created_on": datetime.now(),
            "is_admin": is_admin,
        })


    @initialize_required
    @timeit
    def authenticate_user(self, email: str, password: str) -> bool | Exception:
        user = self.user_exists(email)
        if not user:
            return ValueError(f"No user found under email {email}")

        if user.to_dict()["password"] != password: # Need to use hash later
            return ValueError(f"Password is incorrect!")

        return True    


if __name__ == "__main__":
    print("Test getting email")
import firebase_admin
from datetime import datetime
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter
from rich import print
from api.types import Message, User
from typing import List
from dotenv import load_dotenv
import os


PERMISSION_API_KEY = os.getenv('FIREBASE_AGENT_API_KEY')


class BusinessDBAgent():
    def __init__(self, business_name=None, users="users", messages="messages"):
        """
        Remember to put your business name exactly like what you have putted in the database
        """
        load_dotenv()
        # self.cred = credentials.Certificate('path/to/serviceAccount.json')
        self._app = firebase_admin.initialize_app()
        """
        Should only use self._business_ref when accessing data,
        Avoid using self._db, which has access over the entire database
        """
        self._db = firestore.client()

        self._collection = {
            "users": users,
            "messages": messages,
        }

        self.business_name = None
        self._id = None
        self._business_ref = None
        self._users_ref = None
        self._messages_ref = None
        self.__access_mode = 'r'

        if business_name is not None:
            self.init_business(business_name)


    def _check_empty_query(self, query, error: Exception = None):
        if len(list(query)) == 0:
            if error != None:
                raise error
            return True
    
        return False

    def _validate(value, field):
        """
        Use to validate data and raise error if:
            - Value is None
            - ...incoming
        """
        if value is None:
            raise ValueError(f"{field} cannot be None!")
        

    def check_permission(self, permission: str):
        perm = {
            "r": "read",
            'w': "write",
        }
        for p in permission:
            if p not in self.__access_mode:
                raise PermissionError(f"This agent's method doesn't have {perm[p]} permission!")
            

    def change_permission(self, api: str, permission: str):
        if api != PERMISSION_API_KEY:
            raise ValueError("Agent APi is not correct!")
        
        self.__access_mode = permission
        return True


    def init_business(self, business_name):
        # Use to init a new agent or change the company that the agent is managing
        self.business_name = business_name
        query = self._db.collection("businesses").where(filter=FieldFilter("name", "==", business_name)).limit(1).stream()

        self._check_empty_query(query, ValueError(f"No business found under the name '{business_name}'!"))

        query = next(query, None)

        self._id = query.id
        self._business_ref = self._db.collection("businesses").document(query.id)
        
        self._users_ref = self._business_ref.collection(self._collection["users"])
        self._messages_ref = self._business_ref.collection(self._collection["messages"])


    @check_permission('r')
    def users(self):
        """
        Return a list of users registered for this business
        """
        docs = self._users_ref.stream()
        return [doc.to_dict() for doc in docs]


    @check_permission('r')
    def messages(self):
        """
        Return a list of messages of this business
        """
        docs = self._messages_ref.stream()
        return [(doc.id, doc.to_dict()) for doc in docs]
    

    @check_permission('w')
    def _add_new_message(self, msg: Message):
        """
        Add new message to the current business's messages database
        """
        self._messages_ref.add(msg)


    @check_permission('w')
    def add_new_messages(self, messages: List[Message]):
        """
        Public API to add new messages to the current business's messages database
        """
        for m in messages:
            self.add_new_messages(m)


    @check_permission('r')
    def _user_exists(self, email):
        """
        Check if an user exists in the current business's users database
        """
        self._validate(email, "email")
        
        query = self._users_ref.where(fitler=FieldFilter("email", "==", email)).limit(1).stream()
        
        return self._check_empty_query(query)

    
    @check_permission('w')
    def register_new_user(self, email, password, is_admin=False):
        """
        Register new user by adding to the current business's users database
        """
        self._validate(email, "email")
        self._validate(password, "password")

        query = self._users_ref.where(filter=FieldFilter("email", "==", email)).limit(1).stream()

        if not self._check_empty_query(query):
            raise ValueError("User already existed in the database!")

        self._users_ref.add(User(email, password, is_admin))
        
        return True
    
    @check_permission('r')
    def authenticate_user(self, email, password):
        self._validate(email, "email")
        self._validate(password, "password")

        query = self._users_ref.where(filter=FieldFilter("email", "==", email)).limit(1).stream()

        self._check_empty_query(query, ValueError(f"No user found with email address {email}!"))
    
        self._check_empty_query(query, ValueError(f"Incorrect password for email {email}!"))


        


        
    
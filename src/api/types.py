from datetime import datetime
from typing import List, Literal

def Message(id: str, sender: str, receiver: str, send_date: datetime, content_type: str, labels: List[str], subject: str, body: str):
    return {
        'type': 'Gmail Message',
        'id': id,
        'sender': sender,
        'receiver': receiver,
        'send_date': send_date,
        'content_type': content_type,
        'labels': labels,
        'subject': subject,
        'body': body
    }

def User(email: str, password: str, is_admin: bool, created_on: datetime=datetime.now()):
    return {
        "email": email,
        "password": password,
        "is_admin": is_admin,
        "created_on": created_on
    }

def Product(id: int, name: str, description: str):
    return {
        'id': id,
        'name': name,
        'description': description
    }

def ProductReport(id: str, name: str, status: Literal["mostly positive", "somewhat positive", "neutral",  "somewhat negative", "mostly negative"], summary: List[str]):

    pass

def Report(sender: str, products: List[dict]):
    pass

from datetime import datetime

def Message(id, sender, receiver, send_date, content_type, labels, subject, body):
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

def User(email, password, is_admin, created_on=datetime.now()):
    return {
        "email": email,
        "password": password,
        "is_admin": is_admin,
        "created_on": created_on
    }
from src.api.types import Message, Product
from typing import List

def messages_format(messages: List[Message]):
    return '\n'.join([f'Sender: {msg.get("sender", {}).get('email', "Anonymous")}\n{msg.get("body", "")}' for msg in messages if msg.get("body", "") != ""])

def filter_spam_prompt(ref_products: List[Product], ref_company: str, messages: List[Message]) -> str:
    return f'''
Analyze messages from random people if they are valuable feedback from users or not related to the listed products of the company '{ref_company}. You should return True if a message is a legit feedback and False if it is potentially a spam email or an unrelated message.'
Your response should strictly be a string of boolean values (True or False) separated by commas.
For example, if there are three messages, the first and the third one are spams or unrelated, and the second one is a legit feedback from an user, your response should be like this:

False, True, False

Here is the list of products of company '{ref_company}' and their detailed descriptions:
{ref_products}
Here are the messages:
{messages_format(messages)}
'''
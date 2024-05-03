from src.api.types import Message, Product
from typing import List

def messages_format(messages: List[Message]) -> str:
    return '\n'.join([f"Sender: {msg.get('sender', {}).get('email', 'Anonymous')}\n{msg.get('body', 'This message has no body')}" for msg in messages if msg.get('body', '') != ""])
    return '\n'.join([f'Sender: {msg.get("sender", {}).get("email", "Anonymous")}\n{msg.get("body", "")}' for msg in messages if msg.get("body", "") != ""])


def sample_messages_format(messages: List[Message]) -> str:
    return '\n'.join([f"Sender: {msg.get('sender', {}).get('name', 'Our Precious Customer')}\n{msg.get('body', '')}" for msg in messages if msg.get('body', '') != ""])

    return '\n'.join([f'Sender: {msg.get("sender", {}).get("name", " Our Precious Customer")}\n{msg.get("body", "")}' for msg in messages if msg.get("body", "") != ""])

def product_format(product: Product) -> str:
    return f"Product: id: {product['id']}, name: {product['name']}, description: {product['description']}"


def products_format(products: List[Product]) -> str:
    return [f"{'-' * 15} Begin of message {'-' * 15}\n{product_format(product)}\n{'-' * 15} End of message {'-' * 15}" for product in products]

    return [f"{'-' * 15 + 'Begin of message' + '-' * 15}\n{product_format(product)}\n{'-' * 15 + 'End of message' + '-' * 15}" for product in products]
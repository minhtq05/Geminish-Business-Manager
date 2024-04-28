from typing import List
import re
def json_clean(text: str):
    json_match = re.search(r"```json\s*(.*?)\s*```", text, re.DOTALL)
    if json_match:
        return json_match.group(1)
    else:
        return "Something went wrong when cleaning json!"

def messages_format(messages: List) -> str:
    return '\n'.join([f'Message {i}:\nSender: {msg.get("sender", {}).get('name', " Our Precious Customer")}\n\n{msg.get("body", "")}.\n' for i, msg in enumerate(messages) if msg.get("body", "") != ""])


def sample_messages_format(messages: List) -> str:
    return '\n'.join([f'Sender: {msg.get("sender", {}).get('name', " Our Precious Customer")}\n{msg.get("body", "")}' for msg in messages if msg.get("body", "") != ""])
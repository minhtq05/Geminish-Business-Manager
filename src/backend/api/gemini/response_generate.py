from typing import List

def messages_format(messages: List[dict]):
    return '\n'.join([f'Sender: {msg.get("sender", {}).get('name', " Our Precious Customer")}\n{msg.get("body", "")}' for msg in messages if msg.get("body", "") != ""])

def response_generate_prompt(ref_products, messages):
    return '''
Generate responses to the users' feedback emails based on the products each user mentioned from the below list of products with their description.
Use friendly tone and be as concise as possible.
Each response should be formated in JSON and has 3 attributes: receiver - the sender of the feedback we received earlier, subject - the subject of the response, and body - the body of the feedback.
Here is a sample response:
{
    "responses": [
        {
            "receiver": "emailofthesender1@gmail.com",
            "subject": "Thank you for your feedback",
            "body": "Dear Our Precious Customer,\n\nThank you for your feedback about the black and white coffee of your shop. We appreciate your support and look forward to continuing our relationship with you.\nBest regards,\nThe Coffee House"
        }
    ]
}
Here is a list of products:
''' + f'''
{ref_products}
And here are the users' feedback:
{messages_format(messages)}
'''
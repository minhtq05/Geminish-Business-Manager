from typing import List

def messages_format(messages: List[dict]):
    return '\n'.join([f'Sender: {msg.get("sender", {}).get('email', "Anonymous")}\n{msg.get("body", "")}' for msg in messages if msg.get("body", "") != ""])

def feedback_report_prompt(ref_products, messages):
    return '''
Analyse users' feedback emails and generate reports based on the products each user mentioned from the below list of products with their description.
The reports should be formated in JSON.
Each report should have the following attributes: sender - the email address of the sender, products - a list of objects representing products that the user mentioned. For each object inside the products is a dictionary with 4 attributes: the ID of the product, the name of the product, the status of the feedback for this product (mostly positive, somewhat positive, neutral, somewhat negative, and mostly negative), and the short summary of the feedback about this product written in third person.
If the message is not related to any of the products and their description, it should have an empty products list.
Here is a sample report:
{
    "reports": [
        {
            "sender": "emailofthesender1@gmail.com",
            "products": [
                {
                    "id": 1234,
                    "name": "Product 1",
                    "status": "mostly positive",
                    "summary": "Product is great!"
                },
                {
                    "id": 5678,
                    "name": "Product 2",
                    "status": "mostly negative",
                    "summary": "Have a lot of bugs. The color is too bright and has no dark mode."
                },
                {
                    "id": 1357,
                    "name": "Product 3",
                    "status": "neutral",
                    "summary": "The documentation is hard to read. However, still readable and can be improved."
                }
            ]
        },
        {
            "sender": "emailofthesender2@gmail.com",
            "products": [
                {
                    "id": 5678,
                    "name": "Product 3",
                    "status": "somewhatnegative",
                    "summary": "Doesn't seem working after booted up"
                },
                {
                    "id": 1357,
                    "name": "Product 7",
                    "status": "somewhat negative",
                    "summary": "Didn't run after hours of booting up"
                }
            ]
        }
    ]
}
''' + f'''
Here is a list of products:
{ref_products}
And here are the users' feedback:
{messages_format(messages)}
'''
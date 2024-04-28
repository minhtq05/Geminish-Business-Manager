import time
from rich import print
from src.api.gmail.service import GmailService
from src.api.gemini.agents import GeminiCustomerFeedbackAgent
from src.api.firestore.firestore import FirestoreDB
'''
Test flow: all messages -> filter messages -> print filtered messages
'''
def main(business_name, background, products):

    filter_agent = GeminiCustomerFeedbackAgent(
        business_name=business_name,
        background=background,
        products=products
    )
    token = FirestoreDB()
    gmail = GmailService(business_name, token.get_gmail_token())
    messages = gmail.get_all_messages()
    print(messages)

    print('Lenght',len(messages))
    filtered_messages = filter_agent.filter_messages(messages)
    print(filtered_messages)

if __name__ == "__main__":
    start = time.perf_counter()

    business_name = 'The Coffee House',
    background = 'You are a professional at filtering messages',
    products = ['Black Coffee', 'White Coffee']
    main(business_name, background, products)

    end = time.perf_counter()
    print(f'Finished in {end - start} seconds.')
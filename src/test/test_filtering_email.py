import time
from rich import print, print_json
from src.api.gmail.service import GmailService
from src.api.gemini.agents import GeminiCustomerFeedbackAgent
from src.backend.business import BusinessAgent
from src.api.firestore.firestore import FirestoreDB
from src.api.types import Product
'''
Test flow: all messages -> filter messages -> print filtered messages
'''
def main(business_name, background, products):

    filter_agent = BusinessAgent(
        business_name=business_name,
        products=products
    )
    filter_agent.get_filtered_messages()
    # token = FirestoreDB(business_name)
    # gmail = GmailService(business_name, token.get_gmail_token())
    # messages = gmail.get_all_messages()
    #
    # print('Lenght',len(messages))
    # filtered_messages = filter_agent.filter_messages(messages)
    # print(filtered_messages)

if __name__ == "__main__":
    start = time.perf_counter()

    business_name = 'The Coffee House',
    background = 'You are a professional at filtering messages',
    products = [Product(1000,'Black Coffee', 'A coffee that is black'),
                Product(10000, 'White Coffee', 'A coffee that is white')]
    main(business_name, background, products)

    end = time.perf_counter()
    print(f'Finished in {end - start} seconds.')
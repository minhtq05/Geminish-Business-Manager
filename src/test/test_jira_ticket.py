import time
from src.backend.business import BusinessAgent
from src.api.types import Product
'''
Test flow: all messages -> filter messages 
-> improvements option -> upload all option to Jira

Refer to this video to learn how to use the Jira for testing: 
https://youtu.be/oPbr8eLC4dE?si=hQKplOxCQX3N-ao4
'''

def main(business_name, products, key):
    agent = BusinessAgent(
        business_name=business_name,
        products=products
    )
    payload = agent.get_all_issue(key)
    print(payload)
    res = agent.upload_issue(payload)
    print(res)

if __name__ == "__main__":
    start = time.perf_counter()
    key = 'ARP'
    business_name = 'The Coffee House',
    products =  [Product(1000,'Black Coffee', 'A coffee that is black'),
                Product(10000, 'White Coffee', 'A coffee that is white')]

    main(business_name, products, key)

    end = time.perf_counter()
    print(f'Finished in {end - start} seconds.')

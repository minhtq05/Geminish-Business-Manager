import time
from src.backend.business import BusinessAgent
'''
Test flow: all messages -> filter messages -> get report 
-> improvements option -> upload all option to Jira

Refer to this video to learn how to use the Jira for testing: 
https://youtu.be/oPbr8eLC4dE?si=hQKplOxCQX3N-ao4
'''

def main(business_name, products, key):
    agent = BusinessAgent(
        business_name=business_name,
        products=products
    )
    agent.upload_issue(key)


if __name__ == "__main__":
    start = time.perf_counter()
    key = 'ARP'
    business_name = 'The Coffee House',
    products = ['Black Coffee', 'White Coffee']

    main(business_name, products, key)

    end = time.perf_counter()
    print(f'Finished in {end - start} seconds.')

import time
from rich import print
from src.api.firestore.firestore import FirestoreDB
from src.backend.business import BusinessAgent
from src.api.types import Product
'''
Test flow: all messages -> filter messages 
-> improvements option -> upload all option to Jira

Refer to this video to learn how to use the Jira for testing: 
https://youtu.be/oPbr8eLC4dE?si=hQKplOxCQX3N-ao4
'''

def main(business_name):
    # agent = BusinessAgent(
    #     business_name=business_name,
    #     products=products
    # )
    mock_data = [{'sender': {'email': 'literallyjust4fun@gmail.com', 'name': 'Michael John'}, 'subject': 'Coffee Experience Feedback 1', 'body': "Dear The Coffee House,\nI wanted to share my thoughts on your coffee offerings. Firstly, I must express my admiration for your black coffee. Its rich, bold flavor takes me back to the cafes of my hometown. However, I found the white coffee to be lacking in comparison. It's a bit too sweet for my taste, resembling more of a dessert drink than a coffee. Nevertheless, overall, I appreciate the quality of both options.\nWarm regards, "}, {'sender': {'email': 'literallyjust4fun@gmail.com', 'name': 'Michael John'}, 'subject': 'Coffee Experience Feedback 1', 'body': "Dear The Coffee House,\nI wanted to share my thoughts on your coffee offerings. Firstly, I must express my admiration for your black coffee. Its rich, bold flavor takes me back to the cafes of my hometown. However, I found the white coffee to be lacking in comparison. It's a bit too sweet for my taste, resembling more of a dessert drink than a coffee. Nevertheless, overall, I appreciate the quality of both options.\nWarm regards, "}, {'sender': {'email': 'literallyjust4fun@gmail.com', 'name': 'Michael John'}, 'subject': 'Coffee Experience Feedback 2', 'body': 'Dear The Coffee House,\nWhat is wrong with the black coffee of this shop, very bland. But the white coffee is very good though. It has enough milk and has a very delightful taste. Good job on the white coffee.\nThanks for your service. '}, {'sender': {'email': 'literallyjust4fun@gmail.com', 'name': 'Michael John'}, 'subject': 'Coffee Experience Feedback 2', 'body': 'Dear The Coffee House,\nWhat is wrong with the black coffee of this shop, very bland. But the white coffee is very good though. It has enough milk and has a very delightful taste. Good job on the white coffee.\nThanks for your service. '}, {'sender': {'email': 'literallyjust4fun@gmail.com', 'name': 'Michael John'}, 'subject': 'Coffee Experience Feedback 3', 'body': "Dear The Coffee House,\nI couldn't resist sharing my thoughts on your coffee selection. Your black coffee is a masterpiece, boasting a depth of flavor that's hard to come by. Conversely, while your white coffee is creamy and luxurious, it falls short in terms of coffee intensity. Nonetheless, I'm grateful for the opportunity to enjoy your delicious black brew.\nSincerely, "}, {'sender': {'email': 'literallyjust4fun@gmail.com', 'name': 'Michael John'}, 'subject': 'Coffee Experience Feedback 3', 'body': "Dear The Coffee House,\nI couldn't resist sharing my thoughts on your coffee selection. Your black coffee is a masterpiece, boasting a depth of flavor that's hard to come by. Conversely, while your white coffee is creamy and luxurious, it falls short in terms of coffee intensity. Nonetheless, I'm grateful for the opportunity to enjoy your delicious black brew.\nSincerely, "}, {'sender': {'email': 'literallyjust4fun@gmail.com', 'name': 'Michael John'}, 'subject': 'Coffee Experience Feedback 4', 'body': 'Dear The Coffee House,\nI wanted to take a moment to provide feedback on your coffee offerings. Your black coffee is undeniably superb, with its rich, bold flavor awakening my senses with each sip. However, I found your white coffee to be overly sweet, masking the delicate coffee notes I crave. Nonetheless, I appreciate the variety you offer and will continue to enjoy your black coffee.\nBest regards, '}, {'sender': {'email': 'literallyjust4fun@gmail.com', 'name': 'Michael John'}, 'subject': 'Coffee Experience Feedback 4', 'body': 'Dear The Coffee House,\nI wanted to take a moment to provide feedback on your coffee offerings. Your black coffee is undeniably superb, with its rich, bold flavor awakening my senses with each sip. However, I found your white coffee to be overly sweet, masking the delicate coffee notes I crave. Nonetheless, I appreciate the variety you offer and will continue to enjoy your black coffee.\nBest regards, '}, {'sender': {'email': 'literallyjust4fun@gmail.com', 'name': 'Michael John'}, 'subject': 'Coffee Appreciation Feedback 5', 'body': "Dear The Coffee House,\nI just had to commend you on your black coffee—it's truly exceptional, with its deep, complex flavors satisfying even the most discerning coffee lover. However, I found your white coffee to be a bit too sweet for my liking, lacking the balance I seek in a good cup. Nevertheless, I remain a loyal fan and will continue to savor your delightful black brew.\nSincerely, "}, {'sender': {'email': 'literallyjust4fun@gmail.com', 'name': 'Michael John'}, 'subject': 'Coffee Appreciation Feedback 5', 'body': "Dear The Coffee House,\nI just had to commend you on your black coffee—it's truly exceptional, with its deep, complex flavors satisfying even the most discerning coffee lover. However, I found your white coffee to be a bit too sweet for my liking, lacking the balance I seek in a good cup. Nevertheless, I remain a loyal fan and will continue to savor your delightful black brew.\nSincerely, "}]
    database = FirestoreDB(business_name)
    #database.add_filtered_messages(mock_data)
    database.get_filled_messages()
if __name__ == "__main__":
    start = time.perf_counter()
    business_name = 'The Coffee House',

    main(business_name)

    end = time.perf_counter()
    print(f'Finished in {end - start} seconds.')

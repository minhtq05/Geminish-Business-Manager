def sample_feedback_emails_prompt(ref_products, ref_company_name = None, num_feedbacks = 5):
    return f'''
Generate {num_feedbacks} sample feedback emails from the below list of products with their descriptions from company named '{ref_company_name}'.
Each feedback email has to mention a random number of products from the list (don't nessarily mention all of them) with random status (mostly positive, somewhat positive, neutral, somewhat negative, and mostly negative), and random reason for those status. Most importantly, each message has to have idea, feedback, tone, context, style, and reasons.
Your responses need to be a single JSON object and messages body should be formatted as strings. Here are two feedback examples generated for a company A selling products B and C:
''' + '''
{
    "messages": [
        {
            "sender": "emailofthesender1@gmail.com",
            "subject": "Disappointed with [Product B] Performance",
            "body": Dear Company A,\n\nI am writing to express my disappointment with the recent purchase of your [Product B]. I bought it specifically for [reason for purchase], but unfortunately, it has fallen short of my expectations in several ways.\n\nHere are the main issues I've encountered:\n\n[Specific problem 1 with Product B]: This has made it [explain how the problem affects usage].\n\n[Specific problem 2 with Product B]: I was particularly surprised by this, as [explain your expectation based on product description or reviews].\n\nOverall, the performance of [Product B] has been frustrating and hasn't lived up to the claims advertised. While [Product C] (which I also purchased) has been working well, I'm hesitant to recommend Company A based on this experience.\n\nI would appreciate it if you could look into these issues and potentially offer a solution. Perhaps a replacement or a store credit for [Product B] would be a fair resolution.\n\nThank you for your time and attention to this matter.\n\nSincerely,\nRandom User
        },
        {
            "sender": "emailofthesender2@gmail.com",
            "subject": "Delighted with [Product C]!",
            "body": "Dear Company A,\n\nI'm writing to express my sincere satisfaction with your [Product C]. I recently purchased it for [reason for purchase], and it has been an absolute game-changer!\n\nHere's what I particularly love about it:\n\n[Specific positive aspect 1 of Product C]: This has made [explain how the aspect improves your experience].\n\n[Specific positive aspect 2 of Product C]: I wasn't expecting this feature, but it's a delightful surprise and adds a lot of value.\n\nOverall, [Product C] has exceeded my expectations and has become an essential part of [how you use the product]. The quality and functionality are top-notch, and I would highly recommend it to anyone looking for [what the product helps with].\n\nThank you for creating such an impressive product. I look forward to exploring what else Company A has to offer in the future.\n\nSincerely,\nRandom User"
        }
    ]
}
''' + f'''
Here are the products:
{ref_products}
'''
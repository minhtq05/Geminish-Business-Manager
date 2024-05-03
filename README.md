# Agilizer

## Overview
Agilizer is an ambitious project created for the Google AI Hackathon. Inspired by the need for a comprehensive B2B platform, this powerful tool aims to revolutionize the way businesses manage their day-to-day operations and workflows by automatically gather and act on customer feedback, empowering companies to quickly build, test, and iterate on new products and ideas.

## Key Features
* Email Feedback Scraping: Agilizer seamlessly integrates with your email inbox, automatically extracting valuable customer feedback from emails and organizing it into actionable insights.
* Intelligent Task Generation: The platform's AI-powered algorithms analyze customer feedback and automatically generate targeted tasks, to-do lists, and prioritized action items for your team.
* Rapid Prototyping and Testing: Agilizer enables businesses to quickly transform customer insights into tangible prototypes, allowing for instant testing and validation of new product ideas.
* Collaborative Ideation: The platform fosters collaboration among team members, facilitating the open exchange of ideas and the collective refinement of innovative concepts.
* Robust Analytics and Reporting: Agilizer provides comprehensive analytics and reporting tools, empowering businesses to track the impact of their customer-driven initiatives and make data-informed decisions.

## Usage
To get started with Agilizer, please follow these steps:

1. Sign Up: Visit our website and create an account to access the platform.
2. Explore the Dashboard: Familiarize yourself with the intuitive dashboard and explore the various modules and features.
3. Customize Your Settings: Tailor Agilizer to your specific business needs by configuring preferences and integrating with your existing systems.
4. Embrace the Power of Automation: Leverage the platform's workflow automation capabilities to streamline your operations and boost efficiency.
5. Leverage Data-Driven Insights: Leverage the advanced analytics tools to gain valuable insights and make informed decisions.

## Usage for Developers
To start running Agilizer, you simply need to run this command:
```bash
uvicorn driver:app --reload --host 0.0.0.0 --port 5000
```

Here are things you need to know to start working with Agilizer as a developer:

1. **Databases:**
* Agilizer will mainly use Firebase for all of its data management processes. Therefore, you need to have a working Firebase project with Firestore enabled. Agilizer will store its data in a single "collection" inside your Firebase Firestore database. If you don't have one, you can create a new project by following this instruction: 

    https://firebase.google.com/docs/firestore/quickstart

    Now you have just finished initializing the database for Agilizer. See! It's that simple.

    The structure of Agilizer's database is as follow:
```
    agilizer_database
    ├── businesses
    │   ├── businesses_id_1
    │   │   ├── messages
    │   │   │   ├── message_id_1
    │   │   │   ├── message_id_2
    │   │   │   ├── message_id_3
    │   │   │   ├── ...
    │   │   │   ├── existing_message_ids
    │   │   │   └── token
    │   │   ├── reports
    │   │   │   └── reports
    │   │   └── users
    │   │       ├── user_id_1
    │   │       ├── user_id_2
    │   │       ├── user_id_3
    │   │       └── ...
    │   ├── businesses_id_2
    │   ├── businesses_id_3
    │   └── ...      
    └── users
        ├── business_user_id_1
        ├── business_user_id_2
        └── business_user_id_3

```
Note: Here are some key elements that you need to know about this structure:
* businesses: A collection that stores information about businesses.
    * business_id: Collections within the 'businesses' collection, containing data specific to a single business, including:
        * messages: A subcollection that stores all messages for the business.
            * messages_id: Documents within the 'messages' subcollection, containing data specific to a single message with the following fields:
                ```
                {
                    "id": string - The ID of the message,
                    "sender": string - The email address of the sender,
                    "receiver": string - sThe email address of the receiver,
                    "send_date": timestamp - The date and time the message was sent,
                    "type": string - The type of the message,
                    "content_type": string - The content type of the message,
                    "subject": string - The subject of the message,
                    "labels": string - A list of labels associated with the message,
                    "body": string - The content of the message
                }
                ```
            * existing_message_ids: A list of message IDs that have already been processed and stored in the database.
            * token: A Gmail API token created and used by the business to access and manage their messages. 
        * reports: A subcollection that stores all reports generated from feedback emails for the business.
            * reports: Documents within the 'reports' subcollection, containing data specific to a single report with a list of objects having the following fields:
            ```
            {
                "sender": string - The email address of the sender,
                "products": List[Dict] - [
                    A list of objects having the following fields:
                    {
                        "id": int | string - The ID of the product,
                        "name": string - The name of the product,
                        "status": string - The status of the feedback for this product (mostly positive, somewhat positive, neutral, somewhat negative, and mostly negative),
                        "summary": List[string] - A list of feedback sentences about this product written by the user.
                    }
                ]
            }
            ```
        * users: A subcollection that stores information about users associated with the business.
            * user_id: Documents within the 'users' subcollection, containing data specific to a single user with the following fields:
                ```
                {
                    "email": string - The email address of the user,
                    "password": string - The hashed password of the user
                    "created_on": timestamp - The date and time the user was created,
                    "is_admin": boolean - Whether the user is an admin or not
                }
                ```
* users: A collection that stores information about users of Agilizer.
    * user_id: A document within the 'users' collection, containing data specific to a single user of Agilizer.


2. **Email Management:**
* Next one, in order to read email feedback from customers, you will need to use the official Gmail API to access customers data. If you haven't done so, you can follow this instruction to enable your email API, configure your OAuth settings, and create credentials for your own:

    https://developers.google.com/gmail/api/quickstart/python

    At the moment, Agilizer is letting businesses creating their own Gmail API tokens. Each business will store their token inside their business database, under the *"token"* document we show you above.

    After setting up all the above steps, Agilizer will automatically help you manage businesses' feedback emails using Gmail API.

3. **Gemini Assistant:**
* The mission of Gemini in this project is to help you with analyzing users' feedback, generate tasks, manage to-do lists, and prioritize action items for your team.

    ### Coming soon...



Support and Feedback
* We are committed to providing our users with exceptional support and continuously improving Agilizer. If you have any questions, suggestions, or feedback, please don't hesitate to reach out to our dedicated support team at placeholder@gmail.com.

Thank you for choosing Agilizer. We look forward to supporting your business success!

## Contributors
[@ball2004244](https://github.com/ball2004244)
[@minhtq05](https://github.com/minhtq05)

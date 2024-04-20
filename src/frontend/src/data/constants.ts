import * as Type from "./types";

export const data: Type.Email[] = [
  {
    id: "m5gr84i9",
    date: "3/15/2024",
    email: "ken99@yahoo.com",
    content:
      "Hello Ken, Thank you for reaching out. I'm glad to hear that you're interested in our services. Could you please provide more details about your specific requirements? This will help us tailor our solution to best meet your needs. Looking forward to your response. Best regards, [Your Name]",
    category: "feedback",
  },
  {
    id: "3u1reuv4",
    date: "5/10/2024",
    email: "Abe45@gmail.com",
    content:
      "Dear Abe, I hope this email finds you well. I wanted to follow up on our recent conversation regarding the upcoming project. Attached you will find the latest version of the proposal document. Please review it and let me know if you have any feedback or questions. Thank you and have a great day! Regards, [Your Name]",
    category: "client",
  },
  {
    id: "derv1ws0",
    date: "7/21/2024",
    email: "Monserrat44@gmail.com",
    content:
      "Hi Monserrat, Thank you for your interest in our products. We're excited to announce that we've just launched a new line of accessories that I believe would complement your existing collection perfectly. Please find attached our latest catalog for your review. Let me know if you have any questions or if you'd like to place an order. Best regards, [Your Name]",
    category: "spam",
  },
  {
    id: "5kma53ae",
    date: "9/5/2024",
    email: "Silas22@gmail.com",
    content:
      "Hi Silas, I hope you're doing well. I wanted to inform you about the upcoming maintenance schedule for our online platform. We'll be performing scheduled maintenance on [Date] from [Time] to [Time]. During this time, the platform will be temporarily unavailable. We apologize for any inconvenience this may cause and appreciate your understanding. Regards, [Your Name]",
    category: "others",
  },
  {
    id: "bhqecj4p",
    date: "11/30/2024",
    email: "carmella@hotmail.com",
    content:
      "Dear Carmella, Thank you for your recent purchase. We're excited to hear that you're satisfied with our product. If you have any further questions or need assistance, feel free to reach out to us anytime. We're here to help! Best regards, [Your Name]",
    category: "feedback",
  },
  // 10 more objects
  {
    id: "i2n0ewt8",
    date: "1/15/2024",
    email: "jonathan93@yahoo.com",
    content:
      "Hey Jonathan, I hope you're doing well. I wanted to remind you about our upcoming meeting scheduled for [Date] at [Time]. Please confirm your availability at your earliest convenience. Looking forward to our discussion. Regards, [Your Name]",
    category: "client",
  },
  {
    id: "v7u9dbq3",
    date: "2/20/2024",
    email: "Lea77@gmail.com",
    content:
      "Hi Lea, Thank you for your inquiry. Attached you will find the requested documents. Let me know if you need any further assistance. Regards, [Your Name]",
    category: "feedback",
  },
  {
    id: "w3q1opi5",
    date: "4/5/2024",
    email: "catherine_84@hotmail.com",
    content:
      "Dear Catherine, I'm writing to inform you about the latest updates to our terms and conditions. Please review the attached document and let me know if you have any questions or concerns. Best regards, [Your Name]",
    category: "spam",
  },
  {
    id: "p6y2kfn9",
    date: "6/18/2024",
    email: "Harvey20@yahoo.com",
    content:
      "Hello Harvey, Thank you for your interest in our services. We've received your inquiry and will get back to you shortly with more information. In the meantime, feel free to explore our website for additional details. Regards, [Your Name]",
    category: "others",
  },
  {
    id: "t9l4zsc2",
    date: "8/12/2024",
    email: "Eleanor62@gmail.com",
    content:
      "Hi Eleanor, I wanted to follow up on our recent conversation about the upcoming project. Could you please provide an update on the status? Let me know if you need any assistance. Regards, [Your Name]",
    category: "client",
  },
];
export const NavLinks: Type.NavLink[] = [
  {
    name: "Feedbacks",
    url: "/feedback",
  },
  {
    name: "Summary",
    url: "/summary",
  },
  {
    name: "Jira",
    url: "/jira",
  },
  {
    name: "Insights",
    url: "/insights",
  },
];
export const analyticsTexts: Type.AnalyticText[] = [
  {
    heading: "Positive Feedback Summary",
    subheading: "Analysis of User Responses",
    content:
      "Based on the recent influx of user emails, it's evident that our product has been positively received. Users are particularly appreciative of the intuitive user interface and the seamless experience it offers. Many users have highlighted the convenience and efficiency our product brings to their daily workflow. Overall, the sentiment among users is overwhelmingly positive, indicating a strong satisfaction with our product.",
  },
  {
    heading: "Feature Enhancement Requests",
    subheading: "Insights from User Feedback",
    content:
      "Through user emails, we've gathered valuable insights regarding potential feature enhancements. A common request among users is the addition of advanced customization options to tailor the product to their specific needs. Additionally, users have expressed interest in integrations with popular third-party tools to further streamline their workflow. By prioritizing these enhancements based on user feedback, we can ensure continuous improvement and meet the evolving needs of our users.",
  },
  {
    heading: "Bug Reports and Issue Resolution",
    subheading: "Addressing User Concerns",
    content:
      "Our team has diligently reviewed user emails reporting bugs and issues with our product. We've identified several critical issues affecting user experience, such as intermittent crashes and performance slowdowns. These reports have been invaluable in pinpointing areas for improvement and prioritizing bug fixes. By promptly addressing these issues, we aim to enhance the stability and reliability of our product, ensuring a seamless experience for all users.",
  },
];
export const feedbackData: Type.feedbackType[] = [
  {
    email: "john@example.com",
    id: "feedback_a1b2c3d4e5f6",
    time: "2023-04-19T10:30:00Z",
    content:
      "I've been using your product for a few months now, and I must say, I'm quite impressed. The ease of use and intuitive interface make it a pleasure to work with. However, I did encounter a few minor issues with the reporting feature. It would be great if you could add more customization options and export formats to cater to different user needs. Overall, a solid product that has significantly streamlined my workflow.",
    user: { name: "John Doe", imgHref: "https://example.com/john.png" },
    tags: ["product", "feedback"],
  },
  {
    email: "jane@example.com",
    id: "feedback_f6e5d4c3b2a1",
    time: "2023-04-18T14:45:00Z",
    content:
      "I absolutely love your product! It has revolutionized the way our team collaborates and manages projects. The real-time updates and notifications have been a game-changer, ensuring everyone stays on the same page. One suggestion I have is to improve the mobile app experience, as it can be a bit clunky on smaller screens. Perhaps optimizing the interface for better touch interactions would make it even more convenient for on-the-go use. Overall, a fantastic tool that has significantly boosted our productivity.",
    user: { name: "Jane Smith", imgHref: "https://example.com/jane.png" },
    tags: ["product", "feedback", "review", "mobile"],
  },
  {
    email: "bob@example.com",
    id: "feedback_9a8b7c6d5e4f",
    time: "2023-04-17T09:15:00Z",
    content:
      "I've been a loyal customer of your product for years, and I must commend you on the constant improvements and updates. The latest release has addressed several pain points I've had, particularly with the integration capabilities. Being able to seamlessly connect with other tools in my workflow has been a game-changer. The only area I feel could use some improvement is the onboarding process for new users. Perhaps a more interactive tutorial or guided setup would make it easier for newcomers to hit the ground running. Keep up the great work!",
    user: { name: "Bob Johnson", imgHref: "https://example.com/bob.png" },
    tags: ["product", "feedback", "review", "onboarding"],
  },
  {
    email: "alice@example.com",
    id: "feedback_3c2d1e0f9a8b",
    time: "2023-04-16T18:00:00Z",
    content:
      "As a small business owner, your product has been an absolute lifesaver. The affordability and scalability have allowed me to streamline my operations without breaking the bank. The customer support team deserves a special mention - they've been incredibly responsive and helpful whenever I've had a query or issue. One area for improvement could be the documentation and knowledge base. While comprehensive, it can be a bit overwhelming for newcomers. Perhaps breaking it down into more bite-sized, easy-to-follow guides would make it more accessible. Overall, a fantastic value proposition that has exceeded my expectations.",
    user: { name: "Alice Williams", imgHref: "https://example.com/alice.png" },
    tags: ["product", "feedback", "review", "small business", "support"],
  },
];

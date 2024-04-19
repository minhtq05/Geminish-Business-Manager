import { Routes, Route, BrowserRouter } from "react-router-dom";
import Dashboard from "./pages/home";
import EmailTable from "./components/emailTable";
import DashboardLayout from "./components/layout/dashboardLayout";
import FeedbackPage from "./pages/feedback";
import User from "./components/user";
import { feedbackType } from "./data/types";
import Home from "./pages/home";

const feedbackData: feedbackType[] = [
  {
    email: 'john@example.com',
    id: 'feedback_a1b2c3d4e5f6',
    time: '2023-04-19T10:30:00Z',
    content: "I've been using your product for a few months now, and I must say, I'm quite impressed. The ease of use and intuitive interface make it a pleasure to work with. However, I did encounter a few minor issues with the reporting feature. It would be great if you could add more customization options and export formats to cater to different user needs. Overall, a solid product that has significantly streamlined my workflow.",
    user: <User fallBack="John Doe" imgHref="https://example.com/john.png" />,
    tags: ['product', 'feedback', 'review'],
  },
  {
    email: 'jane@example.com',
    id: 'feedback_f6e5d4c3b2a1',
    time: '2023-04-18T14:45:00Z',
    content: "I absolutely love your product! It has revolutionized the way our team collaborates and manages projects. The real-time updates and notifications have been a game-changer, ensuring everyone stays on the same page. One suggestion I have is to improve the mobile app experience, as it can be a bit clunky on smaller screens. Perhaps optimizing the interface for better touch interactions would make it even more convenient for on-the-go use. Overall, a fantastic tool that has significantly boosted our productivity.",
    user: <User fallBack="Jane Smith" imgHref="https://example.com/jane.png" />,
    tags: ['product', 'feedback', 'review', 'mobile'],
  },
  {
    email: 'bob@example.com',
    id: 'feedback_9a8b7c6d5e4f',
    time: '2023-04-17T09:15:00Z',
    content: "I've been a loyal customer of your product for years, and I must commend you on the constant improvements and updates. The latest release has addressed several pain points I've had, particularly with the integration capabilities. Being able to seamlessly connect with other tools in my workflow has been a game-changer. The only area I feel could use some improvement is the onboarding process for new users. Perhaps a more interactive tutorial or guided setup would make it easier for newcomers to hit the ground running. Keep up the great work!",
    user: <User fallBack="Bob Johnson" imgHref="https://example.com/bob.png" />,
    tags: ['product', 'feedback', 'review', 'onboarding'],
  },
  {
    email: 'alice@example.com',
    id: 'feedback_3c2d1e0f9a8b',
    time: '2023-04-16T18:00:00Z',
    content: "As a small business owner, your product has been an absolute lifesaver. The affordability and scalability have allowed me to streamline my operations without breaking the bank. The customer support team deserves a special mention - they've been incredibly responsive and helpful whenever I've had a query or issue. One area for improvement could be the documentation and knowledge base. While comprehensive, it can be a bit overwhelming for newcomers. Perhaps breaking it down into more bite-sized, easy-to-follow guides would make it more accessible. Overall, a fantastic value proposition that has exceeded my expectations.",
    user: <User fallBack="Alice Williams" imgHref="https://example.com/alice.png" />,
    tags: ['product', 'feedback', 'review', 'small business', 'support'],
  },
];


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route
          path="/dashboard"
          element={
            <DashboardLayout>
              <p>Test</p>
            </DashboardLayout>
          }
        />
        <Route path="/feedback" element={<DashboardLayout><FeedbackPage feedbackData={feedbackData}/></DashboardLayout>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;

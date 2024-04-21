import { Routes, Route, BrowserRouter } from "react-router-dom";
import DashboardLayout from "./components/layout/dashboardLayout";
import FeedbackPage from "./pages/feedback";
import Home from "./pages/home";
import { EmailData } from "./data/constants";

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
        <Route
          path="/feedback"
          element={
            <DashboardLayout>
              <FeedbackPage feedbackData={EmailData} />
            </DashboardLayout>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

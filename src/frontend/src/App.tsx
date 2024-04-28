import { Routes, Route, BrowserRouter } from "react-router-dom";
import DashboardLayout from "./components/layout/dashboardLayout";
import FeedbackPage from "./pages/feedback";
import Home from "./pages/home";
import { EmailData } from "./data/constants";
import SummaryPage from "./pages/summary";
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
              <FeedbackPage />
            </DashboardLayout>
          }
        />
        <Route
          path="/summary"
          element={
            <DashboardLayout>
              <SummaryPage />
            </DashboardLayout>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

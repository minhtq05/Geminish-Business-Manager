import { Routes, Route, BrowserRouter } from "react-router-dom";
import Dashboard from "./pages/home";
import EmailTable from "./components/emailTable";
import DashboardLayout from "./components/layout/dashboardLayout";
import Home from "./pages/home";
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
      </Routes>
    </BrowserRouter>
  );
}

export default App;

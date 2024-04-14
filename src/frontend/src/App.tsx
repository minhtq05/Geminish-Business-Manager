import { Routes, Route, BrowserRouter } from "react-router-dom";
import Dashboard from "./pages/dashboard";
import EmailTable from "./components/emailTable";
import DashboardLayout from "./components/layout/dashboardLayout";
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<p>ditmemay</p>} />
        <Route path="/dashboard" element={<DashboardLayout><Dashboard/></DashboardLayout>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

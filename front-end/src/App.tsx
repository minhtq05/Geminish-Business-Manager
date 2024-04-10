import { Routes, Route, BrowserRouter } from "react-router-dom";
import Dashboard from "./pages/dashboard";
import EmailTable from "./components/emailTable";
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<EmailTable />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

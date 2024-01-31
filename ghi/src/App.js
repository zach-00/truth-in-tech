import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import "./App.css";
import LoginForm from "./login.js";

function App() {
  return (
    <BrowserRouter>
    <div className="container">
        <AuthProvider baseUrl={process.env.REACT_APP_API_HOST}>

      <Routes>
        <Route index element={<LoginForm />} />
        {/* <Route path="/reviews"></Route> */}

      </Routes>

        </AuthProvider>
    </div>
    </BrowserRouter>
  );
}

export default App;

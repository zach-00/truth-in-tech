import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import "./App.css";
import LoginForm from "./login.js";
import CreateCompanyForm from "./CreateCompany.js";

function App() {
  const basename=process.env.PUBLIC_HOST
  const baseUrl=process.env.REACT_APP_API_HOST
  return (
    <BrowserRouter basename={basename}>
    <div className="container">
      <AuthProvider baseUrl={baseUrl}>

        <Routes>
          <Route path="login" element={<LoginForm />} />
          {/* <Route path="/reviews"></Route> */}
          <Route path="companies">
            <Route path="create" element={<CreateCompanyForm/>}/>
          </Route>
        </Routes>

      </AuthProvider>
    </div>
    </BrowserRouter>
  );
}

export default App;

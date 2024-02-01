import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import "./App.css";
import LoginForm from "./login.js";
import CreateCompanyForm from "./CreateCompany.js";
import CreateReview from "./CreateReview.js";

function App() {
  const basename=process.env.PUBLIC_HOST
  const baseUrl=process.env.REACT_APP_API_HOST
  return (
    <BrowserRouter basename={basename}>
    <div className="container">
      <AuthProvider baseUrl={baseUrl}>

      <Routes>
        <Route path="login" element={<LoginForm />} />

        <Route path="companies">
          <Route path="create" element={<CreateCompanyForm/>}/>
        </Route>

        <Route path="reviews">
          <Route path="create" element={<CreateReview />} />
        </Route>

      </Routes>

      </AuthProvider>
    </div>
    </BrowserRouter>
  );
}

export default App;

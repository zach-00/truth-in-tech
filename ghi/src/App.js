import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import "./App.css";
import LoginForm from "./login.js";
import CreateCompanyForm from "./CreateCompany.js";
import CreateReview from "./CreateReview.js";
import CompaniesList from "./CompaniesList.js";
import CreateAccount from "./CreateAccount.js";
import MainPage from "./MainPage.js";

function App() {
  const basename=process.env.PUBLIC_HOST
  const baseUrl=process.env.REACT_APP_API_HOST
  return (
    <BrowserRouter basename={basename}>
    <div className="container">
      <AuthProvider baseUrl={baseUrl}>

      <Routes>
        <Route index element={<MainPage />} />
        <Route path="login" element={<LoginForm />} />

        <Route path="accounts">
          <Route path="create" element={<CreateAccount />} />
        </Route>

        <Route path="companies">
          <Route path="create" element={<CreateCompanyForm/>}/>
          <Route path="list" element={<CompaniesList />} />
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

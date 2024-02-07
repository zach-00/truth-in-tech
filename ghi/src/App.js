import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import "./App.css";
import CreateCompanyForm from "./CreateCompany.js";
import UpdateAccountForm from "./AccountPage.js";
import CreateReview from "./CreateReview.js";
import CompaniesList from "./CompaniesList.js";
import CreateAccount from "./CreateAccount.js";
import CustomNav from "./Nav.js";
import CompanyPage from "./CompanyPage.js";
import Review from "./Review.js"
import MainPage from "./MainPage.js";
import Footer from "./Footer.js";


function App() {
  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, '');
  const baseUrl = process.env.REACT_APP_API_HOST;
  return (
    <BrowserRouter basename={basename}>
      <div className="container">
        <AuthProvider baseUrl={baseUrl}>
          <CustomNav />
          <Routes>

            <Route index element={<MainPage/>} />

            <Route path="accounts">
              <Route path="create" element={<CreateAccount />} />
              <Route path="update" element={<UpdateAccountForm/>}/>
            </Route>
            <Route path="companies">
              <Route path="create" element={<CreateCompanyForm />} />
              <Route path="list" element={<CompaniesList />} />
            </Route>

            <Route path="reviews">
              <Route path="create" element={<CreateReview />} />
              <Route path=":id" element={<CompanyPage />} />
            </Route>
            <Route path="review">
              <Route path=":id" element={<Review />} />
            </Route>

          </Routes>
          <Footer />
        </AuthProvider>
      </div>
    </BrowserRouter>
  );
}

export default App;

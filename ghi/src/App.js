import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import "./App.css";
import LoginForm from "./login.js";

function App() {
  return (
    <div>
      <AuthProvider baseUrl={process.env.REACT_APP_API_HOST}>
        <LoginForm/>
      </AuthProvider>
    </div>
  );
}

export default App;

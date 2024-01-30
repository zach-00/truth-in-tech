import useToken from "@galvanize-inc/jwtdown-for-react";
import { useState } from 'react';


const LoginForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const { login } = useToken();



  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
        login(username, password);

        e.target.reset();

    } catch (error) {
        console.error('Error fetching data:', error);

    }
  };

  return (
    <div className="card text-bg-light mb-3">
      <div className="dropdown">
        <button type="button" className="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside">
            Login
        </button>
        <form className="dropdown-menu p-4" onSubmit={(e) => handleSubmit(e)}>
          <div className="mb-3">
            <label className="form-label">Username:</label>
            <input
              name="username"
              type="text"
              className="form-control"
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Password:</label>
            <input
              name="password"
              type="password"
              className="form-control"
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div>
            <button type="submit" className="btn btn-primary">Login</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginForm;

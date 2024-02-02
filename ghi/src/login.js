import useToken from "@galvanize-inc/jwtdown-for-react";
import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';


const LoginForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const { login } = useToken();


    const handleUsernameChange = (event) => {
      const value = event.target.value;
      setUsername(value);
    }

    const handlePasswordChange = (event) => {
      const value = event.target.value;
      setPassword(value);
    }



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
              onChange={handleUsernameChange}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Password:</label>
            <input
              name="password"
              type="password"
              className="form-control"
              onChange={handlePasswordChange}
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

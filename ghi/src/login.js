import useToken from "@galvanize-inc/jwtdown-for-react";
import { useState } from 'react';
import NavDropdown from 'react-bootstrap/NavDropdown';
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

    const handleKey = e => {
      if (e.keyCode === 13) {
        try {
          login(username, password);

          setUsername('');
          setPassword('');

      } catch (error) {
          console.error('Error fetching data:', error);

      }
      }
  }

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
        login(username, password);

        setUsername('');
        setPassword('');

    } catch (error) {
        console.error('Error fetching data:', error);

    }
  };

  return (
    <button type="button" className="btn btn-outline-light btn-sm">
      <NavDropdown id="login-button" title="Login">
        <div className="form-group">
        <Form className="max form-padding">
          <div className="row">

          <InputGroup className="container-fluid">
            <Form.Control
              placeholder="Username"
              aria-label="text"
              className="form-control"
              onChange={handleUsernameChange}
              onKeyDown={handleKey}
            />
          </InputGroup>
          </div>

          <div className="row">

          <InputGroup>
            <Form.Control
              type="password"
              placeholder="Password"
              aria-label="password"
              className="form-control"
              onChange={handlePasswordChange}
              onKeyDown={handleKey}
            />
          </InputGroup>
          </div>
          <div className="d-grid gap-2">
          <div onClick={handleSubmit} type="submit" className="btn btn-primary">Login</div>
          </div>
        </Form>
        </div>
    </NavDropdown></button>
  );
};

export default LoginForm;

// width: max-content

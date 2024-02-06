import useToken from "@galvanize-inc/jwtdown-for-react";
import { useState } from 'react';
import NavDropdown from 'react-bootstrap/NavDropdown';
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
    <NavDropdown title="Login" id="navbarScrollingDropdown">
        <Form className="d-flex" onSubmit={(e) => handleSubmit(e)}>
          <InputGroup>
            <InputGroup.Text id="basic-addon1">Username:</InputGroup.Text>
            <Form.Control
              placeholder="Username"
              aria-label="text"
              className="form-control"
              onChange={handleUsernameChange}
            />
          </InputGroup>
          <InputGroup>
            <InputGroup.Text id="basic-addon1">Password:</InputGroup.Text>
            <Form.Control
              type="password"
              placeholder="Password"
              aria-label="password"
              className="form-control"
              onChange={handlePasswordChange}
            />
          </InputGroup>
          <Button type="submit" className="btn btn-primary">Login</Button>
        </Form>
    </NavDropdown>
  );
};

export default LoginForm;

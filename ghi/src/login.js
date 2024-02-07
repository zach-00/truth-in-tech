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

        setUsername('');
        setPassword('');

    } catch (error) {
        console.error('Error fetching data:', error);

    }
  };

  return (
    <button type="button" className="btn btn-outline-light btn-sm"><NavDropdown title="Login">
        <div className="form-group">
        <Form className="max form-padding">
          <div className="row">

          <InputGroup className="container-fluid">
            {/* <InputGroup.Text className="form-control-lg" id="basic-addon1">Username:</InputGroup.Text> */}
            <Form.Control
              placeholder="Username"
              aria-label="text"
              className="form-control"
              onChange={handleUsernameChange}
            />
          </InputGroup>
          </div>

          <div className="row">

          <InputGroup>
            {/* <InputGroup.Text id="basic-addon1">Password:</InputGroup.Text> */}
            <Form.Control
              type="password"
              placeholder="Password"
              aria-label="password"
              className="form-control"
              onChange={handlePasswordChange}
            />
          </InputGroup>
          </div>
          <div className="d-grid gap-2">
          <div onClick={handleSubmit} className="btn btn-primary">Login</div>
          </div>
        </Form>
        </div>
    </NavDropdown></button>
  );
};

export default LoginForm;

// width: max-content

import React, { useState } from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";

const CreateAccount = () => {
  const [username, setUserName] = useState("");
  const [firstname, setFirstName] = useState("");
  const [lastname, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { register } = useToken();
  let navigate = useNavigate();
  const handleUserNameChange = async (e) => {
    const value = e.target.value;
    setUserName(value);
  };

  const handleFirstNameChange = async (e) => {
    const value = e.target.value;
    setFirstName(value);
  };

  const handleLastNameChange = async (e) => {
    const value = e.target.value;
    setLastName(value);
  };

  const handleEmailChange = async (e) => {
    const value = e.target.value;
    setEmail(value);
  };

  const handlePasswordChange = async (e) => {
    const value = e.target.value;
    setPassword(value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const userData = {
      username: username,
      first_name: firstname,
      last_name: lastname,
      email: email,
      password: password,
    };

    const url = `${process.env.REACT_APP_API_HOST}/accounts`;

    try {
      register(userData, url);

      e.target.reset();
      navigate(`/login`);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <>
      <h1>Create an Account</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <input
            onChange={handleUserNameChange}
            value={username}
            name="userName"
            placeholder="User Name..."
            required
            type="text"
            id="user_name"
            className="form-control"
          />
          <label htmlFor="user_name"></label>
        </div>
        <div>
          <input
            onChange={handleFirstNameChange}
            value={firstname}
            name="firstName"
            placeholder="First Name"
            required
            type="text"
            id="first_name"
            className="form-control"
          />
          <label htmlFor="first_name"></label>
        </div>
        <div>
          <input
            onChange={handleLastNameChange}
            value={lastname}
            name="LastName"
            placeholder="Last Name"
            required
            type="text"
            id="last_name"
            className="form-control"
          />
          <label htmlFor="last_name"></label>
        </div>
        <div>
          <input
            onChange={handleEmailChange}
            value={email}
            name="email"
            placeholder="Email"
            required
            type="email"
            id="email"
            className="form-control"
          />
          <label htmlFor="email"></label>
        </div>
        <div>
          <input
            onChange={handlePasswordChange}
            value={password}
            name="password"
            placeholder="Password..."
            required
            type="password"
            id="password"
            className="form-control"
          />
          <label htmlFor="password"></label>
        </div>

        <button className="btn btn-primary">Create</button>
      </form>
    </>
  );
};
export default CreateAccount;

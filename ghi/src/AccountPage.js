import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';


const UpdateAccountForm = () => {
    const [updateEmail, setupdateEmail] = useState('');
    const [updateUserName, setupdateUserName] = useState('');
    const [updateFirstname, setupdateFirstname] = useState('');
    const [updateLastname, setupdateLastname] = useState('');
    const navigate = useNavigate();
    const goToHomePage = () => navigate('/');


    const handleOldInfo = async () => {
        const response = await fetch(`${process.env.REACT_APP_API_HOST}/accounts/`, {
            method: 'GET',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        if (response.ok) {
            const info = await response.json()
            setupdateFirstname(info.first_name);
            setupdateLastname(info.last_name);
            setupdateUserName(info.username);
            setupdateEmail(info.email);

        }
    }


    const handleEmailChange = (event) => {
        const value = event.target.value;
        setupdateEmail(value);
    }

    const handleUserNameChange = (event) => {
        const value = event.target.value;
        setupdateUserName(value);
    }

    const handleFirstNameChange = (event) => {
        const value = event.target.value;
        setupdateFirstname(value);
    }

    const handleLastNameChange = (event) => {
        const value = event.target.value;
        setupdateLastname(value);
    }

    const handleDelete = async () => {
        const response = await fetch(`${process.env.REACT_APP_API_HOST}/accounts/`, {
            method: 'DELETE',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        if (response.ok) {goToHomePage();}

    };

    const buttonContainerStyle = {
        display: 'flex',
        justifyContent: 'space-between',
    };

  const handleUpdate = async (e) => {
    e.preventDefault();

    try {

        const response = await fetch(`${process.env.REACT_APP_API_HOST}/accounts/`, {
            method: 'PUT',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: updateUserName,
            first_name: updateFirstname,
            last_name: updateLastname,
            email: updateEmail,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

        if (response.ok){
            const data = await response.json();
            console.log('Account updated:', data);
        }

    } catch (error) {
      console.error('Error updating account:', error.message);
    }
  };
    useEffect(() => {
        handleOldInfo();
    }, [] );

  return (
    <div className="was-validated">
      <div className="mb-3">
        <label htmlFor="updateEmail" className="form-label">
          Email:
        </label>
        <input
          type="text"
          className="form-control"
          id="updateEmail"
          value={updateEmail}
          onChange={handleEmailChange}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="updateUserName" className="form-label">
          Username:
        </label>
        <input
          type="text"
          className="form-control"
          id="updateUserName"
          value={updateUserName}
          onChange={handleUserNameChange}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="updateFirstname" className="form-label">
          First name:
        </label>
        <input
          type="text"
          className="form-control"
          id="updateFirstname"
          value={updateFirstname}
          onChange={handleFirstNameChange}
        />
      </div>
      <div className="mb-3">
        <label htmlFor="updateLastname" className="form-label">
          Last name:
        </label>
        <input
          type="text"
          className="form-control"
          id="updateLastname"
          value={updateLastname}
          onChange={handleLastNameChange}
        />
      </div>
      <div style={buttonContainerStyle}>
      <div className="mb-3">
        <button type="submit" className="btn btn-primary" onClick={handleUpdate}>
          Update
        </button>
      </div>
      <div className="mb-3">
        <button type="delete" className="btn btn-danger" onClick={handleDelete}>
          Delete
        </button>
      </div>
      </div>
    </div>
  );
};

export default UpdateAccountForm;

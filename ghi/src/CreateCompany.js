import React, { useState } from 'react';
import { useAuthContext } from '@galvanize-inc/jwtdown-for-react';

const CreateCompanyForm = () => {
  const [companyName, setCompanyName] = useState('');
  const [companyLogo, setCompanyLogo] = useState('');
  const { token } = useAuthContext()

    const handleNameChange = (event) => {
        const value = event.target.value;
        setCompanyName(value);
    }

    const handleLogoChange = (event) => {
        const value = event.target.value;
        setCompanyLogo(value);
    }

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {

        const response = await fetch(`${process.env.REACT_APP_API_HOST}/companies`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
            company_name: companyName,
            company_logo: companyLogo,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

        if (response.ok){
            const data = await response.json();
            console.log('Company created:', data);

            setCompanyName('');
            setCompanyLogo('')
        }

    } catch (error) {
      console.error('Error creating company:', error.message);
    }
  };

  return (
    <form className="was-validated" onSubmit={handleSubmit}>
      <div className="mb-3">
        <label htmlFor="companyName" className="form-label">
          Company Name:
        </label>
        <input
          type="text"
          className="form-control"
          id="companyName"
          value={companyName}
          onChange={handleNameChange}
          required
        />
      </div>
      <div className="mb-3">
        <label htmlFor="companyLogo" className="form-label">
          Company Logo:
        </label>
        <input
          type="text"
          className="form-control"
          id="companyLogo"
          value={companyLogo}
          onChange={handleLogoChange}
          required
        />
      </div>
      <div className="mb-3">
        <button type="submit" className="btn btn-primary" >
          Create Company
        </button>
      </div>
    </form>
  );
};

export default CreateCompanyForm;

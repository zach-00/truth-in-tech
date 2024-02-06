import { useState, useEffect } from 'react';
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from 'react-router-dom';

function CreateReview() {

    const [anonymous, setAnonymous ] = useState(false);
    const [ jobTitle, setJobTitle ] = useState('');
    const [ salary, setSalary ] = useState('');
    const [ location, setLocation ] = useState('');
    const [ body, setBody ] = useState('');
    const [ companies, setCompanies ] = useState([]);
    const [ company, setCompany ] = useState('');
    const [ username, setUsername ] = useState('');
    const [ triedSubmit, setTriedSubmit ] = useState(false);
    const errorMessage = (!triedSubmit) ? 'alert alert-danger mb-0 d-none' : 'alert alert-danger mb-0';
    const { token } = useAuthContext();
    const navigate = useNavigate();


    const handleToggleChange = () => {
        setAnonymous(!anonymous)
    }

    const handleJobTitleChange = (e) => {
        const value = e.target.value;
        setJobTitle(value);
    }

    const handleSalaryChange = (e) => {
        const value = e.target.value;
        setSalary(value);
    }

    const handleLocationChange = (e) => {
        const value = e.target.value;
        setLocation(value);
    }

    const handleBodyChange = (e) => {
        const value = e.target.value;
        setBody(value);
    }

    const handleCompanyChange = (e) => {
        const value = e.target.value;
        setCompany(value);
    }

    const fetchToken = async () => {
        try {
        const tkn = await fetch(`${process.env.REACT_APP_API_HOST}/token`, {
            credentials: 'include'
        }
        );
            const account_data = await tkn.json();
            setUsername(account_data.account.username);
        } catch (err) {
            console.error(err);
        }
    }

    const fetchCompanies = async (e) => {
        const url = `${process.env.REACT_APP_API_HOST}/companies`;

        try {
            const response = await fetch(url);

            if (response.ok) {
                const data = await response.json();
                setCompanies(data.companies);
            }
        } catch (err) {
            console.error(err);
            }

    }

    useEffect(() => {
        fetchCompanies();
        fetchToken();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (token === null) {
            setTriedSubmit(true);
        }

        const url = `${process.env.REACT_APP_API_HOST}/reviews`;

        const data = {
            anonymous: anonymous,
            salary: salary.replace(',', ''),
            job_title: jobTitle,
            location: location,
            body: body,
            company_id: company
        }

        const fetchOptions = {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                Authorization: `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        };
        try {
            const response = await fetch(url, fetchOptions);

            if (response.ok) {
                await response.json();
                setAnonymous(false);
                setSalary('');
                setJobTitle('');
                setLocation('');
                setCompany('');
                setBody('');
                navigate(`/reviews/${company}`);
            }
        } catch (err) {
            console.error(err);
        }
    }


    return (
        <div className="row">
            <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                <form onSubmit={handleSubmit}>
                    <div className="form-check form-switch">
                        <input
                        className="form-check-input"
                        onChange={handleToggleChange}
                        type="checkbox"
                        role="switch"
                        id="flexSwitchCheckDefault"
                        />
                        <label
                        className="form-check-label"
                        htmlFor="flexSwitchCheckDefault">
                            Anonymous</label>
                    </div>
                    {anonymous
                    ? null
                    : <div><h2>{username}</h2></div>
                    }
                    <div className="input-group mb-3">
                        <span
                        className="input-group-text">
                            💼</span>
                        <input
                        type="text"
                        className="form-control"
                        onChange={handleJobTitleChange}
                        value={jobTitle}
                        id="jobTitle"
                        required
                        placeholder="Job Title"
                        />
                    </div>
                    <div className="input-group mb-3">
                        <span
                        className="input-group-text">
                            💲</span>
                        <input
                        type="text"
                        className="form-control"
                        onChange={handleSalaryChange}
                        value={salary}
                        placeholder="Salary"
                        aria-label="Amount (to the nearest dollar)"
                        />
                        <span
                        className="input-group-text">
                            .00</span>
                    </div>
                    <div className="input-group mb-3">
                        <span
                        className="input-group-text">
                            🗺️</span>
                        <input
                        type="text"
                        className="form-control"
                        onChange={handleLocationChange}
                        value={location}
                        id="location"
                        placeholder="Location"
                        />
                    </div>

                    <div className="form-floating mb-3">
                        <select
                        className="form-select"
                        id="floatingSelect"
                        value={company}
                        required
                        onChange={handleCompanyChange}
                        >
                            <option value="">{company}</option>
                            {companies.map(company => {
                                return (
                                <option
                                value={company.id}
                                key={company.id}
                                >{company.company_name}</option>
                                );
                            })}
                        </select>
                        <label htmlFor="floatingSelect">Select Your Company</label>
                    </div>

                    <div className="form-floating">
                        <textarea
                        className="form-control mb-3"
                        onChange={handleBodyChange}
                        value={body}
                        placeholder="Write a review..."
                        id="body"
                        required
                        style={{height: 300}}>
                        </textarea>
                        <label htmlFor="body">Review...</label>
                    </div>

                    <button
                    className="btn btn-outline-primary mb-3"
                    >
                        Create
                    </button>

                    <div className={errorMessage}>
                        You must be logged in to post a review.
                    </div>

                </form>
                </div>
            </div>
        </div>
    );
}

export default CreateReview;

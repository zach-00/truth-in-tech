import React, {useState, useEffect} from 'react';
import { NavLink } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import Form from 'react-bootstrap/Form';


function CompaniesList() {

    const [ companies, setCompanies] = useState([]);
    const [filteredData, setFilteredData] = useState([]);

    async function getCompanies() {
        const response = await fetch(`${process.env.REACT_APP_API_HOST}/companies`)

        if (response.ok) {
            const data = await response.json();
            setCompanies(data.companies)
        }
    }

    const handleFilter = (event) => {
    const searchCompany = event.target.value
    setFilteredData(searchCompany)
    };

    let filter = companies;
    if (filteredData.length > 0) {
        filter = companies.filter((company) =>
            company.company_name.toUpperCase().includes(filteredData.toUpperCase())
        )
    }


    useEffect(() => {
        getCompanies();
    }, []);


    let navigate = useNavigate()
    const writeReview = () => {
        navigate(`/reviews/create/`)
    }

    return(
        <div>
            <h1>Technology Companies</h1>
            <Form className="d-flex">
                <Form.Control
                type="search"
                placeholder="Search"
                className="me-2"
                aria-label="Search"
                onChange={handleFilter}
                />
            </Form>
            <table className="table table-striped" margin-left="auto">
                <thead>
                    <tr>
                        <th>Company</th>
                        <th></th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {filter.map( (company) => {
                        return (
                            <tr key={company.id}>
                                <td className="nav-item">
                                    <NavLink className="nav-link" to={`/reviews/${company.id}`}><h3 className="company-links">{company.company_name}</h3></NavLink>
                                </td>
                                <td className="text-center">
                                    <img
                                    alt=""
                                    src = {`${company.company_logo}`}
                                    className = "img-thumbnail" width="10%"
                                    />
                                </td>
                                <td>
                                    <button type="button" id={company.id} onClick={() => writeReview(company.id)} className="btn btn-success">Write a Review</button>
                                </td>
                            </tr>
                        )
                    })};
                </tbody>
            </table>
        </div>
    )
}

export default CompaniesList

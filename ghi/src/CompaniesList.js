import {useState, useEffect} from 'react';
import { NavLink } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';



function CompaniesList() {

    const [ companies, setCompanies] = useState([])

    async function getCompanies() {
        const response = await fetch(`${process.env.REACT_APP_API_HOST}/companies`)

        if (response.ok) {
            const data = await response.json();
            setCompanies(data.companies)
        }
    }

    useEffect(() => {
        getCompanies();
    }, []);


    let navigate = useNavigate()
    const writeReview = (id) => {
        navigate(`/reviews/create/${id}`)
    }

    return(
        <div>
            <h1>Technology Companies</h1>
            <table className="table table-striped" margin-left="auto">
                <thead>
                    <tr>
                        <th>Company</th>
                        <th></th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {companies.map( company => {
                        return (
                            <tr key={company.id}>
                                <td className="nav-item">
                                    <NavLink className="nav-link" to={`/reviews/${company.id}`}>{company.company_name}</NavLink>
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
                    })}
                </tbody>
            </table>
        </div>
    )
}

export default CompaniesList

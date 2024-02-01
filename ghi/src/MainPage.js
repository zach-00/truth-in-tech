import { Link } from "react-router-dom";
import { useEffect, useState } from "react";

function MainPage() {

    const [ companies, setCompanies ] = useState([]);
    const [ company, setCompany ] = useState('');


    const fetchCompanies = async () => {
        const url = `${process.env.REACT_APP_API_HOST}/companies/top10`;

        const response = await fetch(url);
        if (response.ok) {
            const data = await response.json();
            setCompanies(data);
        }
    }

    useEffect(() => {
        fetchCompanies();
    }, []);


    return (
        <>
        <h1 className="display-1 text-center">Truth-In-Tech</h1>





        <div className="container-fluid text-center g-0">
            <div className="row">
                <div className="col">

                    <span className="placeholder col-12"></span>
                    <span className="placeholder col-12 bg-primary"></span>
                    <span className="placeholder col-12 bg-secondary"></span>
                    <span className="placeholder col-12 bg-success"></span>
                    <span className="placeholder col-12 bg-danger"></span>
                    <span className="placeholder col-12 bg-warning"></span>
                    <span className="placeholder col-12 bg-info"></span>
                    <span className="placeholder col-12 bg-light"></span>
                    <span className="placeholder col-12 bg-dark"></span>
                    <div className="d-grid gap-2 col mx-auto">


                    <span className="placeholder col-6"></span>
                    <span className="placeholder w-75"></span>



                        <button className="btn btn-outline-primary"
                        type="button" data-bs-toggle="offcanvas"
                        data-bs-target="#offcanvasWithBothOptions"
                        aria-controls="offcanvasWithBothOptions"
                        >
                            10 Most Reviewed Companies
                            </button>
                    </div>
                </div>
                <div className="col-6">
                Column
                </div>
                <div className="col">
                    <div className="card">
                        <img src="background.png" className="card-img-top" />
                        <div className="card-body">
                            <h5 className="card-title">Share your experience!</h5>
                            <p className="card-text">Review your current or former company and job</p>
                            <Link to="#" className="btn btn-primary">Write a Review</Link>
                        </div>
                    </div>


                </div>
            </div>
        </div>











        <div className="offcanvas offcanvas-start"
            data-bs-scroll="true"
            tabIndex="-1"
            id="offcanvasWithBothOptions"
            aria-labelledby="offcanvasWithBothOptionsLabel">
                <div className="offcanvas-header">
                    <h4 className="offcanvas-title"
                    id="offcanvasWithBothOptionsLabel"
                    >
                    Most Reviewed Companies
                    </h4>
                    <button type="button"
                    className="btn-close"
                    data-bs-dismiss="offcanvas"
                    aria-label="Close"></button>
                </div>
            <div className="offcanvas-body">
                <div className="btn-group-vertical" role="group" aria-label="Vertical button group">
                    {companies.map(company => {
                        return (
                            <button key={company.id} type="button" className="btn btn-outline-danger mb-1"><h3>{company.company_name}</h3></button>
                            );
                        })}
                </div>

            </div>
        </div>
</>
    );
}

export default MainPage;




<div className="btn-group-vertical" role="group" aria-label="Vertical button group">
  <button type="button" className="btn btn-primary">Button</button>
</div>

import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { Link } from "react-router-dom";

function CompanyPage() {
  const [reviews, setReviews] = useState([]);
  const { id } = useParams();


    async function getReviews() {
      const url = `${process.env.REACT_APP_API_HOST}/reviews/companies/${id}`;
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setReviews(data);
      }
    }
    useEffect(() => {
    getReviews();
  }, []);

  const companyInfo =
    reviews.length > 0
      ? reviews[0]
      : {company_name: "There are no reviews for this company yet ",
          company_logo:
          "https://upload.wikimedia.org/wikipedia/commons/3/37/Sad-face.png",
        };

  return (
    <>

      <div>
        <h1>{companyInfo.company_name}</h1>
        <h2>
          <img
            src={`${companyInfo.company_logo}`}
            className="img-thumbnail"
            width="10%"
          />
        </h2>
        {reviews.map((review) => (
          <div key={review.id}>
            <h3>
              {review.anonymous === true ? "" : `${review.username}--`}$
              {review.salary}/yr--{review.location}
              <Link to={`/review/${review.id}`} className="btn btn-primary">
                → Check this review out
              </Link>
            </h3>
            <p>{review.body}</p>
          </div>
        ))}
      </div>
    </>
  );
}

export default CompanyPage;

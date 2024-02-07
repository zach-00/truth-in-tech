import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Card from "react-bootstrap/Card";
import Badge from "react-bootstrap/Badge";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Image from "react-bootstrap/Image";
import Row from "react-bootstrap/Row";
import { Link } from "react-router-dom";

function CompanyPage() {
  const [reviews, setReviews] = useState([]);
  const { id } = useParams();

    useEffect(() => {
    async function getReviews() {
      const url = `${process.env.REACT_APP_API_HOST}/reviews/companies/${id}`;
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setReviews(data);
      }
    }
    getReviews(id);
  }, [id]);

  const companyInfo =
    reviews.length > 0
      ? reviews[0]
      : {
          company_name: "There are no reviews for this company yet... ",
          company_logo:
            "https://upload.wikimedia.org/wikipedia/commons/3/37/Sad-face.png",
        };

  return (
    <>
      <div>
        <h1>
          {companyInfo.company_name} <br></br>{" "}
          <Badge bg="secondary">Reviews</Badge>
        </h1>
      </div>
      <div>
        <br></br>
        <Container>
          <Row>
            <Col xs={6} md={4}>
              <Image src={`${companyInfo.company_logo}`} thumbnail />
            </Col>
          </Row>
        </Container>
        <br></br>
        {reviews.map((review) => (
          <div key={review.id}>
            <Card style={{ width: "64rem" }}>
              <Card.Body>
                <Card.Title>
                  {review.anonymous === true ? "" : `${review.username}`} $
                  {review.salary}/yr {review.job_title}
                </Card.Title>
                <Card.Subtitle className="mb-2 text-muted">
                  {review.location}
                </Card.Subtitle>
                <Card.Text>{review.body}</Card.Text>
                <Card.Link as={Link} to={`/review/${review.id}`}>
                  Check this review out
                </Card.Link>
              </Card.Body>
            </Card>
            <br></br>
          </div>
        ))}
      </div>
    </>
  );
}

export default CompanyPage;

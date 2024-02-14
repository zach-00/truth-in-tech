import React, { useState, useEffect, Fragment } from "react";
import { useParams } from "react-router-dom";
import Card from "react-bootstrap/Card";
import Badge from "react-bootstrap/Badge";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Image from "react-bootstrap/Image";
import Row from "react-bootstrap/Row";
import { Link } from "react-router-dom";
import Button from 'react-bootstrap/Button';
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";

function CompanyPage() {
  const {token} = useAuthContext()
  const { id } = useParams();
  const [reviews, setReviews] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [ rerender, setRerender ] = useState(1);
  const [userID, setID] = useState();
  const [likedReviews, setLikedReviews] = useState([]);

  const fetchToken = async () => {
    const tkn = await fetch(`${process.env.REACT_APP_API_HOST}/token`, {
        credentials: 'include'
    })

    const response = await tkn.json()
    setID(response.account.id)
  }

  useEffect(() => {
    async function getReviews() {
      const url = `${process.env.REACT_APP_API_HOST}/reviews/companies/${id}`;
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        const single_review = []
        const i_id = []
        const likedReviewsID = []

        for (let i in data) {


          if (!i_id.includes(data[i].id)) {
          i_id.push(data[i].id)
          single_review.push(data[i])
          }

          if (data[i].liked_id === userID) {
            likedReviewsID.push(data[i].id)
          }
        }

        setReviews(single_review);
        setLikedReviews(likedReviewsID)
        setRerender(2)
      }

    }

    getReviews(id);
    fetchToken();
  }, [id, rerender, userID]);

  const handleSearchInputChange = (event) => {
    setSearchQuery(event.target.value.toLowerCase());
  };

  const filteredReviews = reviews.filter((review) => {
    const body = review.body.toLowerCase();
    const bodySearch = body.includes(searchQuery)
    const username = review.username.toLowerCase();
    const usernameSearch = username.includes(searchQuery);
    const location = review.location.toLowerCase();
    const locationSearch = location.includes(searchQuery);
    const jobtitle = review.job_title.toLowerCase();
    const jobtitleSearch = jobtitle.includes(searchQuery);
    const salary = review.salary.toString();
    const salarySearch = salary.includes(searchQuery);

    if(bodySearch) {
      return true;
    }
    if(usernameSearch && review.anonymous === false) {
      return true
    ;
    }
    if(locationSearch) {
      return true;
    }
    if(jobtitleSearch) {
      return true;
    }
    if(salarySearch) {
      return true;
    }

    return false;
  });

  async function addLike(review_id) {
    const url = `${process.env.REACT_APP_API_HOST}/reviews/${review_id}/like`
    const fetchConfig = {
      method: "PUT",
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      }
    }
    const response = await fetch(url, fetchConfig)

    if (response.ok) {
      const like_url = `${process.env.REACT_APP_API_HOST}/like/${review_id}`

      const likeFetchConfig = {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        }
      }

      const likeResponse = await fetch(like_url, likeFetchConfig)

      if (likeResponse.ok) {
        setRerender(3)
      }
    }
  }


  return (
    <>
      <div className="row">
        <div className="offset-2 col-6">
          <div>
            {reviews.length ? (
              <>
                <h1>
                  {reviews[0].company_name}
                  <br></br>
                  <Badge bg="secondary">Reviews</Badge>
                </h1>
                <br></br>
              </>
            ) : (
              <>
                <h1>
                  <Badge bg="secondary">Reviews</Badge>
                  <p>There are no reviews for this company yet.......</p>
                </h1>
              </>
            )}
          </div>
          <div className="input-group">
            <input
              type="search"
              placeholder="Search (use lowercase)..."
              className="form-control"
              value={searchQuery}
              onChange={handleSearchInputChange}
            />
          </div>
          <div>
            {reviews.length ? (
              <>
                <br></br>
                <Container>
                  <Row>
                    <Col xs={6} md={4}>
                      <Image src={reviews[0].company_logo} thumbnail />
                    </Col>
                  </Row>
                </Container>
              </>
            ) : (
              <>
                <br></br>
                <Container>
                  <Row>
                    <Col xs={6} md={4}>
                      <Image
                        src={
                          "https://upload.wikimedia.org/wikipedia/commons/3/37/Sad-face.png"
                        }
                        thumbnail
                      />
                    </Col>
                  </Row>
                </Container>
              </>
            )}
            <br></br>
            {filteredReviews.map((review) => (
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
                      { token && (!likedReviews.includes(review.id)) ?
                          <div className="d-flex flex-row-reverse">
                            <Button variant="primary" onClick={() => addLike(review.id)}>
                              <i className="bi bi-heart">{review.likes}</i>
                            </Button>
                          </div>
                      :
                          <div className="d-flex flex-row-reverse">
                          <Button disabled variant="primary" onClick={() => addLike(review.id)}>
                              <i className="bi bi-heart">{review.likes}</i>
                            </Button>
                          </div>
                      }
                  </Card.Body>
                </Card>
                <br></br>
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}


export default CompanyPage;

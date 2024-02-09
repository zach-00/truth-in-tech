import { useState, useEffect } from "react";
import { useParams } from "react-router";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import Card from "react-bootstrap/Card";
import { useNavigate } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import { Fragment } from "react";


function Review() {
  let { id } = useParams();
  const { token } = useAuthContext();
  const [review, setReview] = useState({});
  const [username, setUsername] = useState("");
  const [comments, setComments] = useState([]);
  const navigate = useNavigate();
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const [newComment, setNewComment] = useState("");
  const [postedComment, setPostedComment] = useState(false);
  const [ triedComment, setTriedComment ] = useState(false);
  const errorMessage = (!triedComment) ? 'alert alert-danger mb-0 d-none' : 'alert alert-danger mb-0';

  const fetchToken = async () => {
    const tkn = await fetch(`${process.env.REACT_APP_API_HOST}/token`, {
      credentials: "include",
    });

    const response = await tkn.json();
    setUsername(response.account.username);
  };

  useEffect(() => {
    async function getReview() {
      const response = await fetch(
        `${process.env.REACT_APP_API_HOST}/reviews/${id}`
      );

      if (response.ok) {
        const data = await response.json();
        setReview(data);
      }
    }

    const fetchComments = async () => {
    const url = `${process.env.REACT_APP_API_HOST}/reviews/${id}/comments`;
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      setComments(data);
    }
  };
    getReview();
    fetchToken();
    fetchComments();
    setTriedComment(false);

  }, [id, token, postedComment]);

  const deleteReview = async () => {
    const url = `${process.env.REACT_APP_API_HOST}/reviews/${id}`;
    const fetchConfig = {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    };
    const response = await fetch(url, fetchConfig);

    if (response.ok) {
      navigate(`/reviews/${review.company_id}`);
    }
  };

  const handleShow = () => {
    if (token === null) {
        setTriedComment(true);
    } else {
    setShow(true);
    }
  }

  const handleCommentChange = (e) => {
    const value = e.target.value;
    setNewComment(value);
  }

  const handleSubmit = async () => {
    const url = `${process.env.REACT_APP_API_HOST}/reviews/${id}/comments`;


    try {
        if (newComment.length > 0) {
            const commentData = {
                body: newComment
        }

    const fetchConfig = {
      method: "POST",
      body: JSON.stringify(commentData),
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    };


    const response = await fetch(url, fetchConfig);
    if (response.ok) {
        await response.json();
        setNewComment("");
        setShow(false);
        setPostedComment(true);
    }
}
} catch (err) {
    console.error(err);
}
  }

  return (
    <div className="row">
      <div className="offset-1 col-6">
        <div>
          <br></br>
          <Card style={{ width: "60rem" }}>
            <Card.Body>
              <Card.Title>
                <img
                  alt=""
                  src={`${review.company_logo}`}
                  className="img-thumbnail"
                  width="10%"
                />
              </Card.Title>
              {review.anonymous ? (
                ""
              ) : (
                <Card.Text> Reviewer: {review.username}</Card.Text>
              )}

              <Card.Subtitle className="mb-2 text-muted">
                Job Title: {review.job_title}
              </Card.Subtitle>
              <Card.Text>{review.body}</Card.Text>
              {username === review.username ? (
                <button
                  type="button"
                  className="btn btn-danger"
                  onClick={deleteReview}
                >
                  Delete
                </button>
              ) : (
                ""
              )}
            </Card.Body>
          </Card>
        </div>

        <div>
            <br></br>
          {" "}
          <>
            <Button className="mb-3" variant="primary" onClick={handleShow}>
              Add a comment
            </Button>

            <div className={errorMessage}>
                You must be logged in to post a comment.
            </div>

            <Form>
                <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>Add Comment</Modal.Title>
                </Modal.Header>
                <Modal.Body>

                    <InputGroup>
                        <Form.Control onChange={handleCommentChange} value={newComment} as="textarea" aria-label="With textarea" />
                    </InputGroup>

                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                    Close
                    </Button>
                    <Button variant="primary" onClick={handleSubmit}>
                    Submit
                    </Button>
                </Modal.Footer>
                </Modal>
             </Form>
          </>
          <br></br>
          <br></br>
          <h2>Comments</h2>
          {comments.map((comment, index) => {
                return (
                    <Fragment key={index}>
                <Card key={comment.id} border="primary">
                    <Card.Header className="d-flex header" as="h5">
                        <div><p>{comment.username}</p></div>
                        <div><p>{comment.date_created}</p></div>
                    </Card.Header>
                    <Card.Body>
                        <Card.Text>
                        {comment.body}
                        </Card.Text>

                    </Card.Body>
                </Card>
                <br></br>
                </Fragment>
                );
          })}
          <br></br>
        </div>
      </div>
    </div>
  );
}

export default Review;

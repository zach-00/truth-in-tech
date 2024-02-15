import { useState, useEffect } from "react"
import { useParams } from "react-router"
import { useGetReviewQuery, useDeleteReviewMutation, useGetCommentsQuery, usePostCommentMutation } from "./store/reviewsApi";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import Card from "react-bootstrap/Card";
import { useNavigate } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import { Fragment } from "react";


function Review() {

    let {id} = useParams()
    const {token} = useAuthContext()
    const [username, setUsername] = useState('')
    const navigate = useNavigate()
    const { data: reviewData } = useGetReviewQuery(id);
    const [deleteReview] = useDeleteReviewMutation();
    const { data: commentData, isLoading: commentsLoading } = useGetCommentsQuery(id);
    const  [postComment, result] = usePostCommentMutation();


    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const [newComment, setNewComment] = useState("");
    const [postedComment, setPostedComment] = useState(false);
    const [triedComment, setTriedComment] = useState(false);
    const errorMessage = (!triedComment) ? 'alert alert-danger mb-0 d-none' : 'alert alert-danger mb-0';


  const fetchToken = async () => {
    const tkn = await fetch(`${process.env.REACT_APP_API_HOST}/token`, {
      credentials: "include",
    });

    const response = await tkn.json();
    setUsername(response.account.username);
  };

    useEffect(() => {
        fetchToken();
        setTriedComment(false);
    }, [id, token, reviewData, commentData, postedComment]);

    const handleDeleteReview = async () => {
        const result = await deleteReview(id).unwrap();
        if (result) {
            navigate(`/reviews/${reviewData.company_id}`);
        }
    }

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

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        if (newComment.length > 0) {
            const params = {
                body: {body: newComment},
                id: id,
        }

          await postComment(params);
        }

    } catch (err) {
      console.error(err);
    }
}

useEffect(() => {
  if (result.isSuccess) {
        setNewComment("");
        setShow(false);
        setPostedComment(true);
    } else if (result.isError) {
     console.error("Failed to submit comment successfully")
    }
}, [result]);


    return (
        <div className="row">
            <div className="offset-1 col-6">
                <div>
                <br></br>
                {reviewData ?
                    <Card style={{ width: '60rem' }}>
                        <Card.Body>
                            <Card.Title>
                                <img
                                alt=""
                                src={reviewData.company_logo}
                                className = "img-thumbnail" width="10%"
                                />

                            </Card.Title>
                            {reviewData.anonymous
                            ? "Anonymous"
                            : <Card.Text> Reviewer:  {reviewData.username}</Card.Text>}

                        <Card.Subtitle className="mb-2 text-muted">Job Title:  {reviewData.job_title}</Card.Subtitle>
                        <Card.Text>
                            {reviewData.body}
                        </Card.Text>
                        {reviewData.username === username ?
                            <button type="button" className="btn btn-danger" onClick={handleDeleteReview} >Delete</button>
                            : ""
                            }
                    </Card.Body>
                </Card>
                : null
                }
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
                        <Form.Control style={{height: 200}} onChange={handleCommentChange} value={newComment} as="textarea" aria-label="With textarea" />
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

            {!commentsLoading && commentData.length
              ? <h2>Comments</h2>
              : null
            }

              {!commentsLoading && commentData.length ?
               commentData.map((comment, index) => {
                    return(
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
               })
               : null
              }

            <br></br>
            </div>
        </div>
    </div>
  );
}

export default Review;

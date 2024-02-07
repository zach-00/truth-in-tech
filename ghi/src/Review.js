import { useState, useEffect } from "react"
import { useParams } from "react-router"
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import Card from 'react-bootstrap/Card';
import { useNavigate } from 'react-router-dom';


function Review() {

    let {id} = useParams()
    const {token} = useAuthContext()
    const [review, setReview] = useState({});
    const [username, setUsername] = useState('')
    const navigate = useNavigate()

    const fetchToken = async () => {
        const tkn = await fetch(`${process.env.REACT_APP_API_HOST}/token`, {
            credentials: 'include'
        })

        const response = await tkn.json()
        setUsername(response.account.username)
    }

    useEffect(() => {
        async function getReview() {

            const response = await fetch(`${process.env.REACT_APP_API_HOST}/reviews/${id}`)

            if (response.ok) {
                const data = await response.json();
                setReview(data)
            }

        }

        getReview();
        fetchToken();
    }, [id, token]);

    const deleteReview = async () => {
        const url = `${process.env.REACT_APP_API_HOST}/reviews/${id}`
        const fetchConfig = {
            method: "DELETE",
            headers: {
                Authorization: `Bearer ${token}`,
                'Content-Type': 'application/json',
            },
        }
        const response = await fetch(url, fetchConfig)

        if (response.ok) {
            console.log(review.company_id)
            navigate(`/reviews/${review.company_id}`)
        }
    }


    return (
        <div className="row">
            <div className="offset-1 col-6">
                <div>
                <br></br>
                    <Card style={{ width: '60rem' }}>
                        <Card.Body>
                            <Card.Title>
                                <img
                                alt=""
                                src={`${review.company_logo}`}
                                className = "img-thumbnail" width="10%"
                                />

                            </Card.Title>
                            {review.anonymous
                            ? ""
                            : <Card.Text> Reviewer:  {review.username}</Card.Text>}

                        <Card.Subtitle className="mb-2 text-muted">Job Title:  {review.job_title}</Card.Subtitle>
                        <Card.Text>
                            {review.body}
                        </Card.Text>
                        {username===review.username ?
                            <button type="button" className="btn btn-danger" onClick={deleteReview} >Delete</button>
                            : ""
                            }
                    </Card.Body>
                </Card>
            </div>
        </div>
    </div>
    )
}

export default Review

import { useState, useEffect } from "react"
import { useParams } from "react-router"
import Card from 'react-bootstrap/Card';


function Review() {

    let {id} = useParams()

    const [review, setReview] = useState({});

    useEffect(() => {
        async function getReview() {

            const response = await fetch(`${process.env.REACT_APP_API_HOST}/reviews/${id}`)

            if (response.ok) {
                const data = await response.json();
                setReview(data)
            }

        }

        getReview();
    }, [id]);


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
                    </Card.Body>
                </Card>
            </div>
        </div>
    </div>
    )
}

export default Review

import { useState, useEffect } from "react"
import { useParams } from "react-router"
import Card from 'react-bootstrap/Card';


function Review() {

    let {id} = useParams()

    const [review, setReview] = useState({});

    async function getReview() {

        const response = await fetch(`${process.env.REACT_APP_API_HOST}/reviews/${id}`)

        if (response.ok) {
            const data = await response.json();
            setReview(data)
        }

    }

    useEffect(() => {
        getReview();
    }, []);


    return (
           <div>
            <br></br>
            <Card style={{ width: '60rem' }}>
                <Card.Body>
                    <Card.Title>
                        <img
                        src={`${review.company_logo}`}
                        className = "img-thumbnail" width="10%"
                        />

                    </Card.Title>
                    {review.anonymouns === true ? "" :
                    <Card.Text> Reviewer:  {review.username}</Card.Text>}

                    <Card.Subtitle className="mb-2 text-muted">Job Title:  {review.job_title}</Card.Subtitle>
                    <Card.Text>
                        {review.body}
                    </Card.Text>
                </Card.Body>
            </Card>
        </div>
    )
}

export default Review

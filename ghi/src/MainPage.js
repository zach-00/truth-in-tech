import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import logo from './images/Truth-In-Tech-Logo.png';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Image from 'react-bootstrap/Image';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Placeholder from 'react-bootstrap/Placeholder';
import Offcanvas from 'react-bootstrap/Offcanvas';
import Carousel from 'react-bootstrap/Carousel';


function MainPage() {

    const [ companies, setCompanies ] = useState([]);
    const [ reviews, setReviews ] = useState([]);
    const [ show, setShow ] = useState(false);
    const [ index, setIndex ] = useState(0);

    const handleClose = () => setShow(false);
    const toggleShow = () => setShow((s) => !s);

    const navigate = useNavigate();


    const fetchCompanies = async () => {
        const url = `${process.env.REACT_APP_API_HOST}/companies/top10`;

        try {
            const response = await fetch(url);
            if (response.ok) {
                const data = await response.json();
                setCompanies(data);
            }
        } catch (err) {
            console.error(err);
        }
    }

    const fetchReviews = async () => {
        const url = `${process.env.REACT_APP_API_HOST}/reviews/top10/`;

        try {
            const response = await fetch(url);
            if (response.ok) {
                const data = await response.json();
                setReviews(data);
            }
        } catch (err) {
            console.error(err);
        }
    }

    const handleCompanyClick = (e) => {
        navigate(`reviews/${e.target.value}`);
    }

    const handleWriteReviewClick = (e) => {
        navigate('reviews/create');
    }

    const handleSelect = (selectedIndex) => {
        setIndex(selectedIndex);
    };

    useEffect(() => {
        fetchCompanies();
        fetchReviews();
    }, []);


    return (
        <>
        <h1 className="text-center title">Truth-In-Tech</h1>
            <Container>
                <Row>
                    <Col className="padding">
                        <>
                            <Placeholder xs={6} />
                            <Placeholder className="w-75" /> <Placeholder style={{ width: '25%' }} />
                        </>

                        <>
                        <div className="d-grid gap-2 padding-top">
                            <Button variant="outline-primary" onClick={toggleShow} size="lg">
                                10 Most Reviewed Companies
                            </Button>
                        </div>

                        <Offcanvas show={show} onHide={handleClose}>
                            <Offcanvas.Header closeButton>
                            <Offcanvas.Title><h3>10 Most Reviewed Companies</h3></Offcanvas.Title>
                            </Offcanvas.Header>
                            <Offcanvas.Body>
                            {companies.map((company, index) => {
                                return (
                                    <ListGroup key={index}>
                                        <ListGroup.Item onClick={handleCompanyClick} key={company.id} value={company.id} action variant="primary">{company.company_name}</ListGroup.Item>
                                    </ListGroup>
                                    );
                                })}
                            <br></br>
                            This list stays up to date with our most reviewed companies.
                            Click a company to be navigated to their list of reviews.
                            </Offcanvas.Body>
                        </Offcanvas>
                        </>

                    </Col>

                    <Col className="padding" xs={6} >
                        <h2 className="text-center">Featured Reviews</h2>
                        <Carousel className="carousel-inner text-center" activeIndex={index} onSelect={handleSelect}>
                            {reviews.map((review, index) => {
                                return (
                                <Carousel.Item key={index}>
                                    <Image src={review.company_logo} width="50%" alt=""/>
                                    <Carousel.Caption>
                                    </Carousel.Caption>
                                        <Card className="offset-2" style={{ width: '27rem' }}>
                                            <Card.Body >
                                                <Card.Title>{review.job_title}</Card.Title>
                                                <Card.Subtitle className="mb-2 text-muted">{review.location}</Card.Subtitle>
                                                <Card.Text>
                                                {review.body}
                                                </Card.Text>
                                                <br></br>
                                            </Card.Body>
                                        </Card>
                                </Carousel.Item>
                                );
                            })}

                        </Carousel>

                    </Col>

                    <Col className="padding">
                        <Card border="primary" style={{ width: '20rem' }}>
                            <Card.Img variant="top" src={logo} />
                            <Card.Body>
                                <Card.Title>Share your experience!</Card.Title>
                                <Card.Text>
                                Leave a review of your employer
                                or your job at that company
                                </Card.Text>
                                <Button onClick={handleWriteReviewClick} variant="outline-primary">Write a Review</Button>
                            </Card.Body>
                        </Card>
                        <Placeholder xs={12} />
                        <Placeholder xs={12} bg="primary" />
                        <Placeholder xs={10} bg="secondary" />
                        <Placeholder xs={8} bg="success" />
                        <Placeholder xs={12} bg="danger" />
                        <Placeholder xs={12} bg="warning" />
                        <Placeholder xs={11} bg="info" />
                        <Placeholder xs={12} bg="light" />
                        <Placeholder xs={12} bg="dark" />
                    </Col>
                </Row>
            </Container>
        </>
    );
}

export default MainPage;

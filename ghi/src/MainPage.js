import { Link } from "react-router-dom";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Image from 'react-bootstrap/Image';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Placeholder from 'react-bootstrap/Placeholder';
import Offcanvas from 'react-bootstrap/Offcanvas';

function MainPage() {

    const [ companies, setCompanies ] = useState([]);
    const [ reviews, setReviews ] = useState([]);
    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const toggleShow = () => setShow((s) => !s);

    const navigate = useNavigate();


    const fetchCompanies = async () => {
        const url = `${process.env.REACT_APP_API_HOST}/companies/top10`;

        const response = await fetch(url);
        if (response.ok) {
            const data = await response.json();
            setCompanies(data);
        }
    }

    const fetchReviews = async () => {
        const url = `${process.env.REACT_APP_API_HOST}/reviews/top10/`;

        const response = await fetch(url);
        if (response.ok) {
            const data = await response.json();
            setReviews(data);
        }
    }

    const handleCompanyClick = (e) => {
        navigate(`reviews/companies/${e.target.value}`);
    }

    const handleWriteReviewClick = (e) => {
        navigate('reviews/create');
    }

    useEffect(() => {
        fetchCompanies();
        fetchReviews();
    }, []);


    return (
        <>
        <Navbar collapseOnSelect expand="lg" className="bg-body-tertiary" bg="dark" data-bs-theme="light">
        <Container>
            <Navbar.Brand href="#home">Truth-In-Tech</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="me-auto">
                <Nav.Link href="#features">Features</Nav.Link>
                <Nav.Link href="#pricing">Pricing</Nav.Link>
                <NavDropdown title="Dropdown" id="collapsible-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">
                    Another action
                </NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.4">
                    Separated link
                </NavDropdown.Item>
                </NavDropdown>
            </Nav>
            <Nav>
                <Nav.Link href="#deets">More deets</Nav.Link>
                <Nav.Link eventKey={2} href="#memes">
                Dank memes
                </Nav.Link>
            </Nav>
            </Navbar.Collapse>
        </Container>
    </Navbar>
        <h1 className="text-center title">Truth-In-Tech</h1>
            <Container>
                <Row>
                    <Col className="padding" xs={6} md={4}>
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

                            Some text as placeholder. In real life you can have the elements you
                            have chosen. Like, text, images, lists, etc.
                            </Offcanvas.Body>
                        </Offcanvas>
                        </>

                    </Col>
                    <Col className="padding" xs={6} md={4}>
                        <Image src="holder.js/171x180" roundedCircle />
                    </Col>
                    <Col className="padding" xs={6} md={4}>
                        <Card border="primary" style={{ width: '25rem' }}>
                            <Card.Img variant="top" src="Truth-In-Tech-Logo.png" />
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

import LoginForm from "./login.js";
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import LogoutButton from "./logout.js";
import { useAuthContext } from "@galvanize-inc/jwtdown-for-react";
import Avvvatars from 'avvvatars-react'
import React, { useEffect, useState } from "react";
import { NavLink, Link } from "react-router-dom"



function CustomNav() {
    const [username, setUsername] = useState('')
    const {token} = useAuthContext();


    const fetchToken = async () => {
        try {
        const tkn = await fetch(`${process.env.REACT_APP_API_HOST}/token`, {
            credentials: 'include'
        }
        );
            const account_data = await tkn.json();
            setUsername(account_data.account.username);
        } catch (err) {
            console.error(err);
        }
    }


    useEffect(() => {
        fetchToken();
    }, [token]);


  return (
    <>
    <Navbar expand="lg" className="bg-body-tertiary">
      <Container fluid>
        <Navbar.Brand as={Link} to={'/'} style={{ color: "white" }} >TruthInTech</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0 d-flex flex-wrap space-between">
                <Nav
                    style={{ maxHeight: '75px', justifyContent: 'space-evenly' }}
                    navbarScroll
                >

                    {token
                    ? <>
                        <div><Avvvatars value={username} style={{shape: true}} /></div>
                        &nbsp;
                        &nbsp;
                        <div className="d-grid align-items-center" >Hello, {username}</div>
                        &nbsp;
                        &nbsp;
                        <div>
                            <li>
                            <LogoutButton/>
                            </li>
                        </div>
                        &nbsp;
                        &nbsp;
                        <div>
                            <li>
                                <NavLink to="accounts/update">
                                    <Button variant="dark">My account</Button>
                                </NavLink>
                            </li>
                        </div></>
                    :<> <div>
                            <li><LoginForm/></li>
                        </div>
                        &nbsp;
                        &nbsp;
                        <div>
                            <li>
                                <NavLink to="accounts/create">
                                    <Button variant="dark">Become A User</Button>
                                </NavLink>
                            </li>
                        </div></>
                    }
                    &nbsp;
                    &nbsp;
                    <NavLink to="Companies/list">
                        <Button variant="dark">Companies</Button>
                    </NavLink>
                </Nav>
            </ul>
        </Navbar.Collapse>
      </Container>
    </Navbar>
    </>
  )
}

export default CustomNav;

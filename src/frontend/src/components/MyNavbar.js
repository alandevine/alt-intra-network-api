import React from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import '../styles/navbar.css';

export default function MyNavbar() {
    return (
        <Navbar bg="dark" variant="dark">
            <Nav className="mr-auto">
                <Nav.Link href="/">Devices</Nav.Link>
                <Nav.Link href="/statistics">Statistics</Nav.Link>
                <Nav.Link href="/settings">Settings</Nav.Link>
            </Nav>
        </Navbar>
    );
}
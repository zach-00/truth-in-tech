import useToken from "@galvanize-inc/jwtdown-for-react";
import Button from 'react-bootstrap/Button';
import { useNavigate } from 'react-router-dom';


const LogoutButton = () => {
    const { logout } = useToken();
    const navigate = useNavigate();
    const goToHomePage = () => navigate('/');


    const handleLogout = async (e) => {
        e.preventDefault();

        try {
            console.log('Logging out...');
            await logout();
            goToHomePage();
            console.log('Logout successful');


        } catch (error) {
            console.error('Error loging out:', error);

        }
    };
    return (
        <Button variant="dark" type="button" className="btn btn-primary" onClick={handleLogout}>Logout</Button>
    );
};

export default LogoutButton;

import React, { useState } from 'react';

const LoginPage = ({ onLogin }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [loginMessage, setLoginMessage] = useState('');
    const [errorMessage, setErrorMessage] = useState(''); // Added error message state

    const handleLogin = (event) => {
        event.preventDefault();

        // Clear messages before login
        setLoginMessage('');
        setErrorMessage('');

        // Call the onLogin prop to handle the login logic in App.js
        onLogin(username, password, setLoginMessage, setErrorMessage);
    };

    return (
        <div className="login-container">
            <h2>Login</h2>
            <form onSubmit={handleLogin}>
                <label>
                    Username:
                    <input
                        type="text"
                        id="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </label>
                <br />
                <label>
                    Password:
                    <input
                        type="password"
                        id="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </label>
                <br />
                <button type="submit" id="login-button">Login</button>
            </form>
            
            {/* Display login or error message */}
            {loginMessage && <div id="success-message">{loginMessage}</div>}
            {errorMessage && <div id="error-message">{errorMessage}</div>}
        </div>
    );
};

export default LoginPage;

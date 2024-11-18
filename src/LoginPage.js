import React, { useState } from 'react';

const LoginPage = ({ onLogin }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [loginMessage, setLoginMessage] = useState('');

    const handleLogin = (event) => {
        event.preventDefault();
        
        // Call the onLogin prop to handle the login logic in App.js
        onLogin(username, password, setLoginMessage);
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
            
            {/* Display login message */}
            {loginMessage && (
                <div id="success-message">{loginMessage}</div>
            )}
        </div>
    );
};

export default LoginPage;

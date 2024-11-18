import React, { useState } from 'react';
import LoginPage from './LoginPage';

function App() {
    const [loginMessage, setLoginMessage] = useState('');

    const handleLogin = (username, password, setMessage) => {
        console.log(`Login attempted with username: ${username} and password: ${password}`);
        
        // Simple login validation for testing
        if (username === 'testuser' && password === 'testpass') {
            setMessage('Login successful');
        } else {
            setMessage('Invalid username or password');
        }
    };

    return (
        <div className="App">
            <LoginPage onLogin={handleLogin} />
        </div>
    );
}

export default App;

// src/App.js
import React from 'react';
import LoginPage from './LoginPage';

function App() {
    const handleLogin = (username, password) => {
        console.log(`Login attempted with username: ${username} and password: ${password}`);
    };

    return (
        <div className="App">
            <LoginPage onLogin={handleLogin} />
        </div>
    );
}

export default App;

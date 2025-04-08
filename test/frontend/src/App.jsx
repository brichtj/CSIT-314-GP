import React, { useState } from 'react';
import './App.css';

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const login = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username,
          password,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        alert('Login Success');
        console.log('Login detail(JSON):' + JSON.stringify(data, null, 2));
        localStorage.setItem('user', JSON.stringify(data.user)); // Save if needed
      } else {
        alert(data.error || 'Login failed');
      }
    } catch (err) {
      console.error('Network error:', err);
      alert('Something went wrong.');
    }
  };

  return (
    <div className="App">
      <header>
        Home Cleaning System
      </header>

      <main>
        <div className="form-container">
          <p className="title">Welcome back</p>
          <form className="form">
            <input type="email" className="input" id="email_input" placeholder="Email"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <input type="password" className="input" id="password_input" placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button className="form-btn" onClick={login}>
              <span className="form-btn-content">Log in</span>
            </button>
          </form>
          {/* <p className="sign-up-label">
            Don't have an account?<span className="sign-up-link">Sign up</span>
          </p> */}
        </div>
      </main>
    </div>
  );
}

export default App;

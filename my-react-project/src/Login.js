import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import styles from './Login.module.css';
import backgroundImage from './bg.png';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        const url = 'http://127.0.0.1:5000/authenticate';

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ id: username, password: password })
            });

            const data = await response.json();

            if (response.ok && data.success) {
                switch (data.role) {
                    case 'student':
                        navigate('/student', { state: { user: data.user, role: data.role } });
                        break;
                    case 'tutor': 
                        console.log(data);
                        const floorData = await sendTutorID(data.user[0]);  // Retrieve floor data for the tutor
                        if (floorData) {
                            navigate('/tutor', { state: { user: data.user, role: data.role, room: data.room, floorData: floorData.data } });
                        } else {
                            alert('Failed to retrieve floor data. Please try again.');
                        }
                        break;
                    case 'admin':
                        navigate('/supervisor', { state: { user: data.user, role: data.role } });
                        break;
                    case 'supervisor':
                        navigate('/manager', { state: { user: data.user, role: data.role } });
                        break;
                    default:
                        alert('Invalid user type!');
                        break;
                }
            } else {
                alert('Invalid username or password!');
            }
        } catch (error) {
            alert('Error logging in: ' + error.message);
        }
    };

    // Function to send tutor's ID and retrieve floor data
const sendTutorID = async (tutorId) => {
    try {
        const response = await fetch('http://127.0.0.1:5000/view_floor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ "Tutor_ID": tutorId } ) // Adjusted to match backend expectation
        });
        console.log("Sending Tutor ID: ", tutorId);
        if (!response.ok) {
            throw new Error('Failed to send tutor ID. Status: ' + response.status);
        }

        return await response.json();  // Return the JSON data received from the server
    } catch (error) {
        console.error('Error sending tutor ID:', error);
        alert('Error sending tutor information: ' + error.message);
        return null;  // Return null if there's an error
    }
};


    return (
        <div className={styles.rootContainer} style={{ backgroundImage: `url(${backgroundImage})` }}>
            <div className={styles.container}>
                <h2 className={styles.title}>宿舍管理系统登录</h2>
                <form onSubmit={handleSubmit} className={styles.form}>
                    <div className={styles.formGroup}>
                        <label htmlFor="username" className={styles.label}>用户名</label>
                        <input
                            type="text"
                            id="username"
                            placeholder="请输入用户名"
                            value={username}
                            onChange={e => setUsername(e.target.value)}
                            className={styles.input}
                        />
                    </div>
                    <div className={styles.formGroup}>
                        <label htmlFor="password" className={styles.label}>密码</label>
                        <input
                            type="password"
                            id="password"
                            placeholder="请输入密码"
                            value={password}
                            onChange={e => setPassword(e.target.value)}
                            className={styles.input}
                        />
                    </div>
                    <button type="submit" className={styles.btnPrimary}>登录</button>
                </form>
            </div>
        </div>
    );
}

export default Login;

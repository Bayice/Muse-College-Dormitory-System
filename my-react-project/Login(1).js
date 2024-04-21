// Login.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import styles from './Login.module.css';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleSubmit = (event) => {
        event.preventDefault();
        if (password === '123456') {
            switch (username) {
                case 'student':
                    navigate('/student');
                    break;
                case 'mentor':
                    navigate('/mentor');
                    break;
                case 'manager':
                    navigate('/manager');
                    break;
                case 'supervisor':
                    navigate('/supervisor');
                    break;
                default:
                    alert('Invalid user type or password!');
            }
        } else {
            alert('Invalid username or password!');
        }
    };

    return (
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
    );
}

export default Login;
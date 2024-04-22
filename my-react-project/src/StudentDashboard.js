import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import styles from './StudentDashboard.module.css';
import backgroundImage from './bg.png';

function StudentDashboard() {
    const location = useLocation();
    const navigate = useNavigate();
    const userData = location.state ? location.state.user : null;

    const handleSelectClick = () => {
        navigate('/selection', { state: { user: userData } });
        console.log(userData); // Log user data when navigating
    };

    return (
        <div className={styles.pageContainer} style={{ backgroundImage: `url(${backgroundImage})`, backgroundSize: 'cover', backgroundPosition: 'center center', backgroundRepeat: 'no-repeat' }}>
            <div className={styles.containerStyle}>
                <h1 className={styles.mb3}>学生信息面板</h1>
                {userData ? (
                    <div className={`${styles.card} ${styles.divMargin}`}>
                        <div className="card-body">
                            <h5 className="card-title">个人详情</h5>
                            <table className="table">
                                <tbody>
                                    <tr>
                                        <th scope="row">姓名</th>
                                        <td>{userData[1]}</td>
                                    </tr>
                                    <tr>
                                        <th scope="row">学位</th>
                                        <td>{userData[2]}</td>
                                    </tr>
                                    <tr>
                                        <th scope="row">宿舍(床位)</th>
                                        <td>{userData[9]}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                ) : (
                    <div className={`${styles.alert} ${styles.alertWarning} ${styles.alertMargin}`} role="alert">
                        无用户数据
                    </div>
                )}
                <button className={`${styles.btn} ${styles.btnPrimary} ${styles.mt3} ${styles.buttonStyle}`} onClick={handleSelectClick}>选择/修改</button>
            </div>
        </div>
    );
}

export default StudentDashboard;

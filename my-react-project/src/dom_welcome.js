import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import styles from './Dom_welcome.module.css';
import backgroundImage from './bg.png';

function Dom_welcome() {
  const location = useLocation();
  const { roomid, userData } = location.state || {};

  const [studentInfo, setStudentInfo] = useState({
    name: userData ? userData[0] : "Unknown",
    studentNumber: userData ? userData[1] : "000000000",
  });

  const [introduction, setIntroduction] = useState('');

  const handleInputChange = (event) => {
    setIntroduction(event.target.value);
  };

  const handleFinishClick = () => {
    sendIntroductionToServer();
  };

  const sendIntroductionToServer = async () => {
    const introductionData = {
      id: userData[0], // user's ID from userData
      introduction: introduction // user's introduction text
    };

    console.log(introductionData)

    try {
      const response = await fetch('http://localhost:5000/update_student_introduction', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(introductionData)
      });

      if (response.ok) {
        console.log('Introduction updated successfully!');
        alert('介绍更新成功');
      } else {
        console.error('Failed to update introduction:', response.status);
        alert('更新失败');
      }
    } catch (error) {
      console.error('Error updating introduction:', error);
      alert('发送错误');
    }
  };

  return (
    <div className={styles.supervisorDashboard} style={{ backgroundImage: `url(${backgroundImage})` }}>

    <div className={styles.container}>
      <div className={styles.card}>
        <h1 className={styles.title}>Welcome to Dorm {roomid || "Unknown"}</h1>
        <p className={styles.information}>{studentInfo.name} - {studentInfo.studentNumber}</p>
        <div>
          <label htmlFor="introduceInput" className={styles.introductionLabel}>Introduce yourself:</label>
          <input
            id="introduceInput"
            type="text"
            className={styles.introductionInput}
            value={introduction}
            onChange={handleInputChange}
          />
        </div>
        <button className={styles.finishButton} onClick={handleFinishClick}>Finish</button>
      </div>
    </div>
    </div>
  );
}

export default Dom_welcome;

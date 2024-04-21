import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import styles from './Dom_welcome.module.css';

function Dom_welcome() {
  const location = useLocation();
  const { roomid, userData } = location.state || {}; // Ensure defaults are set if no state is provided

  // Initialize studentInfo with values from userData
  const [studentInfo, setStudentInfo] = useState({
    name: userData ? userData[0] : "Unknown",
    studentNumber: userData ? userData[1] : "000000000",
  });

  const [introduction, setIntroduction] = useState('');

  const handleInputChange = (event) => {
    setIntroduction(event.target.value);
  };

  const handleFinishClick = () => {
    console.log(introduction);
  };

  return (
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
  );
}

export default Dom_welcome;

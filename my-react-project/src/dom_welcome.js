import React, { useState } from 'react';
import './dom_welcome.css';

function dom_welcome() {
  // 假设这些数据是从数据库获取的
  const [studentInfo, setStudentInfo] = useState({
    name: "John Doe",
    studentNumber: "123456789",
  });

  // 输入框状态
  const [introduction, setIntroduction] = useState('');

  // 处理输入框变化的函数
  const handleInputChange = (event) => {
    setIntroduction(event.target.value);
  };

  // 处理 Finish 按钮点击事件的函数
  const handleFinishClick = () => {
    // 这里可以执行一些操作，例如发送数据到后端等
    console.log(introduction);
  };

  return (
    <div className="supervisor-dashboard">
      <h1>Welcome</h1>
      <h2>Please fill your personal information</h2>
      <p>{studentInfo.name} - {studentInfo.studentNumber}</p>
      <div className="introduction">
        <label htmlFor="introduceInput">Introduce yourself:</label>
        <input
          id="introduceInput"
          type="text"
          value={introduction}
          onChange={handleInputChange}
        />
      </div>
      <div className="finish-button">
        <button onClick={handleFinishClick}>Finish</button>
      </div>
    </div>
  );
}

export default dom_welcome;

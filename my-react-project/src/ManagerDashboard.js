import React, { useState } from 'react';

import styles from './ManagerDashboard.module.css'; // 注意模块化 CSS 的导入方式
import { useLocation, useNavigate } from 'react-router-dom';

import backgroundImage from './bg.png';

function SelectionPage() {
  const location = useLocation();
  const userData = location.state ? location.state.user : null;
  const [infors, setInfors] = useState([]);
  const [floors, setFloors] = useState([]);
  const navigate = useNavigate(); // 使用 useNavigate hook 进行页面导航

  const handleFloorChange = (event) => {
    const selectedFloor = parseInt(event.target.value, 10);
    if (floors.includes(selectedFloor)) {
      setFloors(floors.filter(floor => floor !== selectedFloor));
    } else {
      setFloors([...floors, selectedFloor]);
    }
  };

  const handleInforChange = (event) => {
    const selectedInfor = event.target.value;
    if (infors.includes(selectedInfor)) {
      setInfors(infors.filter(infor => infor !== selectedInfor));
    } else {
      setInfors([...infors, selectedInfor]);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const postData = {
      floors,
      infors,
      Dormitory_Supervisor_ID: userData[0]
    };

    console.log("Submitting the following data to the backend:", postData);  // 打印提交的数据

    try {
      const response = await fetch('http://127.0.0.1:5000/view_building', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
      });

      if (response.ok) {
        const info = await response.json();
        console.log(info);
        alert('Rooms fetched successfully!');
        // 页面导航到新页面
        navigate('/man-select-output', { state: { info: info, role: postData.infors } });
      } else {
        throw new Error('Failed to fetch rooms. Status: ' + response.status);
      }
    } catch (error) {
      console.error('Error:', error);
      alert('Error fetching rooms: ' + error.message);
    }
  };

  return (
    <div className={styles.supervisorDashboard} style={{ backgroundImage: `url(${backgroundImage})` }}>
    <div className={styles.container}>
      <h1 className={styles.title}>舍监宿舍信息查询管理</h1>
      <form onSubmit={handleSubmit}>
        <div className={styles.formSection}>
          <strong>请选择您要查看的楼层:</strong>
          {[1, 2, 3, 4, 5, 6, 7, 8].map((floor) => (
            <div key={floor} className={styles.inputGroup}>
              <input
                type="checkbox"
                id={`floor-${floor}`}
                value={floor}
                onChange={handleFloorChange}
                checked={floors.includes(floor)}
                className={styles.input}
              />
              <label htmlFor={`floor-${floor}`} className={styles.label}>{floor}</label>
            </div>
          ))}
          <span className={styles.multiSelectTip}>(可多选)</span>
        </div>
  
        <div className={styles.formSection}>
          <strong>请选择您要查看的信息:</strong>
          {['Tutor', 'Student'].map((infor) => (
            <div key={infor} className={styles.inputGroup}>
              <input
                type="checkbox"
                id={`infor-${infor}`}
                value={infor}
                onChange={handleInforChange}
                checked={infors.includes(infor)}
                className={styles.input}
              />
              <label htmlFor={`infor-${infor}`} className={styles.label}>{infor}</label>
            </div>
          ))}
          <span className={styles.multiSelectTip}>(可多选)</span>
        </div>

        <button type="submit" className={styles.submitButton}>开始查询</button>
      </form>
    </div>
    </div>
  );
}  

export default SelectionPage;

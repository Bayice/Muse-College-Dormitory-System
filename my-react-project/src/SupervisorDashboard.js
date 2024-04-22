import React, { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import styles from './SupervisorDashboard.module.css'; // 注意模块化 CSS 的导入方式

function SupervisorDashboard() {
  // 从 location.state 中正确提取 userData
  const location = useLocation();
  const navigate = useNavigate();
  const userData = location.state ? location.state.user : null;
  const [buildings, setBuildings] = useState([]);
  const [infors, setInfors] = useState([]);
  const [floors, setFloors] = useState([]);
  console.log(userData[0]);
  const handleBuildingChange = (event) => {
    const selectedBuilding = event.target.value;
    if (buildings.includes(selectedBuilding)) {
      setBuildings(buildings.filter(building => building !== selectedBuilding));
    } else {
      setBuildings([...buildings, selectedBuilding]);
    }
  };

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
  
    // Extracting the supervisor ID, assuming it is at index 0 of userData
    const supervisorId = userData ? userData[0] : null; 
  
    const postData = {
      buildings,
      floors,
      infors,  // Using the state variable directly which holds the user-selected information types
    };
  
    console.log("Submitting the following data to the backend:", postData);  // Logging the data being submitted
  
    try {
      const response = await fetch('http://127.0.0.1:5000/admin_query', {  // Updated the API endpoint
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
        navigate('/Sup-select-output', { state: { info: info, role: postData.infors } });
      } else {
        throw new Error('Failed to fetch rooms. Status: ' + response.status);
      }
    } catch (error) {
      console.error('Error:', error);
      alert('Error fetching rooms: ' + error.message);
    }
  };

  return (
    <div className={styles.backgroundContainer}>
      <div className={styles.container}>
        <h1 className={styles.title}>信息查询管理</h1>
      <form onSubmit={handleSubmit}>
        <div className={styles.formSection}>
          <strong>选择楼栋:</strong>
          {['MuseCollege-A', 'MuseCollege-B', 'MuseCollege-C'].map((building) => (
            <div key={building} className={styles.inputGroup}>
              <input
                type="checkbox"
                id={`building-${building}`}
                value={building}
                onChange={handleBuildingChange}
                checked={buildings.includes(building)}
                className={styles.input}
              />
              <label htmlFor={`building-${building}`} className={styles.label}>{building} 栋</label>
            </div>
          ))}
          <span className={styles.multiSelectTip}>(可多选)</span>
        </div>
  
        <div className={styles.formSection}>
          <strong>选择楼层:</strong>
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
          <strong>选择信息:</strong>
          {['Dormitory_Supervisor', 'Tutor', 'Student'].map((infor) => (
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

export default SupervisorDashboard;

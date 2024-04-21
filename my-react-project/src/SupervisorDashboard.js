// SelectionPage.js
import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import styles from './SelectionPage.module.css'; // 注意模块化 CSS 的导入方式

function SelectionPage() {
  // 从 location.state 中正确提取 userData
  const location = useLocation();
  const userData = location.state ? location.state.user : null;
  const [buildings, setBuildings] = useState([]);
  const [infors, setInfors] = useState([]);
  const [floors, setFloors] = useState([]);
  const [infor, setInfor] = useState([]);

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

    const studentType = userData ? userData[2] : null; // Assuming the student type is at index 2
    const postData = {
      buildings,
      floors,
      infor,
      student_type: studentType
    };

    console.log("Submitting the following data to the backend:", postData);  // 打印提交的数据

    try {
      const response = await fetch('http://127.0.0.1:5000/search_rooms', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
      });

      if (response.ok) {
        const rooms = await response.json();
        console.log(rooms);
        alert('Rooms fetched successfully!');
      } else {
        throw new Error('Failed to fetch rooms. Status: ' + response.status);
      }
    } catch (error) {
      console.error('Error:', error);
      alert('Error fetching rooms: ' + error.message);
    }
  };

  return (
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
          {['Manager', 'Tutor', 'Student'].map((infor) => (
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
  );
}  

export default SelectionPage;

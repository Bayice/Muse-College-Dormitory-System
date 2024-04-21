import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import styles from './SelectionPage.module.css';
function SelectionPage() {

  const location = useLocation();
  const navigate = useNavigate();
  // 从 location.state 中正确提取 userData
  const userData = location.state ? location.state.user : null;
  const [buildings, setBuildings] = useState([]);
  const [floors, setFloors] = useState([]);
  const [gender, setGender] = useState('');
  const [roomTypes, setRoomTypes] = useState([]); // 新增状态用于房间类型

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

  const handleGenderChange = (event) => {
    setGender(event.target.value);
  };

  const handleRoomTypeChange = (event) => {
    const selectedRoomType = event.target.value;
    if (roomTypes.includes(selectedRoomType)) {
      setRoomTypes(roomTypes.filter(roomType => roomType !== selectedRoomType));
    } else {
      setRoomTypes([...roomTypes, selectedRoomType]);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const studentType = userData ? userData[2] : null; // Assuming the student type is at index 2
    const postData = {
      buildings,
      floors,
      gender,
      room_type: roomTypes,
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
        navigate('/selection-output', { state: { roomsData: rooms, user:userData } });  // Navigate and pass the rooms data
        console.log(userData)
      } else {
        throw new Error('Failed to fetch rooms. Status: ' + response.status);
      }
    } catch (error) {
      console.error('Error fetching rooms:', error);
      alert('Error fetching rooms: ' + error.message);
    }
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>宿舍筛选</h1>
      <form onSubmit={handleSubmit}>
        <div className={styles.formSection}>
          <strong>楼栋:</strong>
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
          <strong>楼层:</strong>
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
          <strong>性别:</strong>
          <div className={styles.inputGroup}>
            <input
              type="radio"
              id="gender-male"
              name="gender"
              value="男"
              onChange={handleGenderChange}
              checked={gender === '男'}
              className={styles.input}
            />
            <label htmlFor="gender-male" className={styles.label}>男</label>
            <input
              type="radio"
              id="gender-female"
              name="gender"
              value="女"
              onChange={handleGenderChange}
              checked={gender === '女'}
              className={styles.input}
            />
            <label htmlFor="gender-female" className={styles.label}>女</label>
          </div>
          <span className={styles.multiSelectTip}>(单选)</span>
        </div>
  
        <div className={styles.formSection}>
          <strong>房间类型:</strong>
          {['上床下桌', '上下铺'].map((roomType) => (
            <div key={roomType} className={styles.inputGroup}>
              <input
                type="checkbox"
                id={`room-type-${roomType}`}
                value={roomType}
                onChange={handleRoomTypeChange}
                checked={roomTypes.includes(roomType)}
                className={styles.input}
              />
              <label htmlFor={`room-type-${roomType}`} className={styles.label}>{roomType}</label>
            </div>
          ))}
          <span className={styles.multiSelectTip}>(可多选)</span>
        </div>
  
        <button type="submit" className={styles.submitButton}>开始筛选</button>
      </form>
    </div>
  );
}

export default SelectionPage;

import React, { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import styles from './SelectionOutput.module.css';

function SelectionOutput() {
  const location = useLocation();
  const navigate = useNavigate();
  const rooms = location.state && location.state.roomsData && Array.isArray(location.state.roomsData.rooms)
                 ? location.state.roomsData.rooms
                 : [];
  const userData = location.state ? location.state.user : null;
  const [selectedBuilding, setSelectedBuilding] = useState('');
  const [checkedRooms, setCheckedRooms] = useState({});

  // Resets the checkedRooms state and sets the selected building
  const handleBuildingSelection = (building) => {
    setSelectedBuilding(building);
    setCheckedRooms({});
  };

  if (rooms.length === 0) {
    return (
      <div className={styles.containerCentered}>
        <h2>没有符合的房间</h2>
      </div>
    );
  }

  const buildings = rooms.reduce((acc, room) => {
    const building = room[0].charAt(0);
    if (!acc.includes(building)) {
      acc.push(building);
    }
    return acc;
  }, []).sort();

  const filteredRooms = rooms.filter(room => room[0].charAt(0) === selectedBuilding);

  const handleSubmit = async () => {
    const selectedRoomEntry = Object.entries(checkedRooms).find(([key, value]) => value);
    if (selectedRoomEntry) {
      const [selectedRoomIndex] = selectedRoomEntry;
      const roomToSend = filteredRooms[parseInt(selectedRoomIndex)][0];

      try {
        const response = await fetch('http://localhost:5000/view_room', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ Room_ID: roomToSend })
        });

        if (response.ok) {
          const rooms_students = await response.json();
          navigate('/Dom_select', { state: { rooms_students: rooms_students.data, user: userData, roomid: roomToSend } });
        } else {
          console.error('Failed to send room data:', response.status);
        }
      } catch (error) {
        console.error('Error sending room data:', error);
      }
    } else {
      alert('Please select a room before submitting.');
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.sidebar}>
        <ul>
          {buildings.map((building, index) => (
            <li
              key={index}
              onClick={() => handleBuildingSelection(building)}
              className={`${styles.building} ${selectedBuilding === building ? styles.selectedBuilding : ''}`}
            >
              Muse {building}
            </li>
          ))}
        </ul>
      </div>
      <div className={styles.roomsDisplay}>
        <h1>欢迎来到思廷 {selectedBuilding}栋</h1>
        {selectedBuilding === '' ? (
          <p className={styles.noRooms}>请选择你的房间</p>
        ) : (
          filteredRooms.length > 0 ? filteredRooms.map((room, idx) => (
            <div className={styles.room} key={idx}>
              <input
                type="checkbox"
                id={`room-${idx}`}
                name={`room-${idx}`}
                checked={!!checkedRooms[idx]}
                onChange={() => setCheckedRooms(prev => ({ ...prev, [idx]: !prev[idx] }))}
              />
              <label htmlFor={`room-${idx}`}>{room[0]}</label>
            </div>
          )) : <p className={styles.noRooms}>No rooms available in this building.</p>
        )}
      </div>
      <button className={styles.submitButton} onClick={handleSubmit}>Submit</button>
    </div>
  );
}

export default SelectionOutput;

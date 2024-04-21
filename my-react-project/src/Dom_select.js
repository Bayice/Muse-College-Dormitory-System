import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import styles from './Dom_select.module.css';

function Dom_select() {
  const location = useLocation();
  const roomid = location.state ? location.state.roomid : null;
  const roomsStudentsData = location.state ? location.state.rooms_students : [];
  const userData = location.state ? location.state.user : null;

  // Changed to a string to hold the single selected room
  const [selectedRoom, setSelectedRoom] = useState('');

  const [roomAvailability, setRoomAvailability] = useState({
    A: true,
    B: true,
    C: true,
    D: true
  });

  useEffect(() => {
    const availability = { A: true, B: true, C: true, D: true };
    roomsStudentsData.forEach(student => {
      const occupiedBed = student[9].slice(-1);
      if (availability[occupiedBed] !== undefined) {
        availability[occupiedBed] = false;
      }
    });
    setRoomAvailability(availability);
  }, [roomsStudentsData]);

  const handleRoomSelection = (room) => {
    if (!roomAvailability[room]) return;
    setSelectedRoom(room); // Now we're setting a single room
  };

  const Room = ({ room }) => (
    <div
      className={`${styles.room} ${!roomAvailability[room] ? styles.unavailable : selectedRoom === room ? styles.selected : ''}`}
      onClick={() => handleRoomSelection(room)}
    >
      {room}
      {selectedRoom === room && roomAvailability[room] && <span className={styles.checkmark}>✓</span>}
    </div>
  );

  const sendDataToServer = async () => {
    const dormitory = selectedRoom ? `${roomid}${selectedRoom}` : roomid;
    const dataToSend = { id: userData[0], dormitory: dormitory };

    try {
      const response = await fetch('http://localhost:5000/AddAStudent', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(dataToSend)
      });

      if (response.ok) {
        console.log('Data sent successfully!');
        alert('成功修改');
      } else {
        console.error('Failed to send data:', response.status);
      }
    } catch (error) {
      console.error('Error sending data:', error);
    }
  };

  return (
    <div className={styles.supervisorDashboard}>
      <div className={styles.welcomeText}>Welcome</div>
      <div className={styles.content}>
        <div className={styles.houseLayout}>
          <div className={styles.house}>
            <div className={styles.row}>
              <Room room="A" />
              <Room room="B" />
            </div>
            <div className={styles.row}>
              <Room room="C" />
              <Room room="D" />
            </div>
          </div>
        </div>
        <div className={styles.welcomeAgainText}>Welcome again</div>
        <div className={styles.buttons}>
          <button onClick={() => console.log('Back')}>Back</button>
          <button onClick={sendDataToServer}>Submit</button>
        </div>
      </div>
    </div>
  );
}

export default Dom_select;

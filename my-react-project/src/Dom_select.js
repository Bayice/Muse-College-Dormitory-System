import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import styles from './Dom_select.module.css';
import { useNavigate } from 'react-router-dom';
import backgroundImage from './bg.png';

function Dom_select() {
  const location = useLocation();
  const navigate = useNavigate();
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
      className={`${styles.room} ${
        !roomAvailability[room] ? styles.unavailable : selectedRoom === room ? styles.selected : ''
      }`}
      onClick={() => handleRoomSelection(room)}
    >
      <div className={styles.door}></div> {/* Door element at the top */}
      {room}
      <div className={styles.window}></div> {/* Window element at the bottom */}
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
        navigate('/Dom_welcome', { state: { roomid, userData } });
      } else {
        console.error('Failed to send data:', response.status);
      }
    } catch (error) {
      console.error('Error sending data:', error);
    }
  };

  return (
    <div className={styles.supervisorDashboard} style={{
      backgroundImage: `url(${backgroundImage})`,
      backgroundSize: 'cover', // 确保图片覆盖整个元素
      backgroundPosition: 'center', // 居中图片
      backgroundRepeat: 'no-repeat', // 不重复图片
      minHeight: '100vh', // 至少高度为视窗高度
      width: '100vw' // 宽度为视窗宽度
    }}>

    <div className={styles.supervisorDashboard}>
      <div className={styles.welcomeText}>Dorm {roomid}</div>
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
        <div className={styles.welcomeAgainText}>Dorm</div>
        <div className={styles.buttons}>
          <button onClick={() => console.log('Back')}>Back</button>
          <button onClick={sendDataToServer}>Submit</button>
        </div>
      </div>
    </div>
    </div>
  );
}

export default Dom_select;

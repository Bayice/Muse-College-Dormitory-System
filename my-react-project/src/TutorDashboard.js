import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import './TutorDashboard.css'; // Ensure your CSS is still applied
import backgroundImage from './bg.png';

function TutorDashboard() {
    const location = useLocation();
    const navigate = useNavigate();
    const { user, role, room, floorData } = location.state || { user: null, role: null, room: null, floorData: [] };

    const [roomsInfo, setRoomsInfo] = useState({});

    // Parse floor data to organize students by room
    useEffect(() => {
        const rooms = {};
        if (Array.isArray(floorData)) {
            floorData.forEach(student => {
                const roomNumber = student[5]; // Assuming room number is the 6th item in the array
                if (!rooms[roomNumber]) {
                    rooms[roomNumber] = [];
                }
                rooms[roomNumber].push(student);
            });
            setRoomsInfo(rooms);
        }
    }, [floorData]); // Dependency ensures re-run if floorData changes

    return (
        <div className="container" style={{ backgroundImage: `url(${backgroundImage})` }}> {/* Inline style to apply background image */}

        <div className="container">
            <h1>Welcome, {user ? user[1] : 'User'}</h1>

            <div>
                <h2>Tutor宿舍信息</h2>
                <p>宿舍名称：{room}</p>
                <p>Tutor名称：{user ? user[1] : 'TBD'}</p>
            </div>

            <br />
             
            <div className="room-info">
                <h2>Tutor负责的楼层学生信息</h2>
                {Object.keys(roomsInfo).map(roomNumber => (
                    <div key={roomNumber} className="room-detail">
                        <button onClick={() => navigate(`/room/${roomNumber}`, { state: { students: roomsInfo[roomNumber] } })}>
                            Room {roomNumber}
                        </button>
                    </div>
                ))}
            </div>
        </div>
        </div>
    );
}

export default TutorDashboard;

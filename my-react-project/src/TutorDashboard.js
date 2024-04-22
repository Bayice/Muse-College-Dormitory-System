import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import './TutorDashboard.css'; // 确保你的 CSS 仍然被应用
import backgroundImage from './bg.png';

function TutorDashboard() {
    const location = useLocation();
    const navigate = useNavigate();
    const { user, role, room, floorData } = location.state || { user: null, role: null, room: null, floorData: [] };

    const [roomsInfo, setRoomsInfo] = useState({});

    // 解析楼层数据以按房间组织学生
    useEffect(() => {
        const rooms = {};
        if (Array.isArray(floorData)) {
            floorData.forEach(student => {
                const roomNumber = student[5]; // 假设房间号在数组中的第6个位置
                if (!rooms[roomNumber]) {
                    rooms[roomNumber] = [];
                }
                rooms[roomNumber].push(student);
            });
            setRoomsInfo(rooms);
        }
    }, [floorData]); // 依赖确保如果 floorData 发生变化，则重新运行

    return (
        <div className="outer-container" style={{ backgroundImage: `url(${backgroundImage})` }}>
            <div className="container">
                <h1>Welcome, {user ? user[1] : 'User'}</h1>

                <div>
                    <h2>Tutor Dorm Information</h2>
                    <p>Room Name: {user[3]}</p>
                    <p>Tutor Name: {user ? user[1] : 'TBD'}</p>
                </div>

                <br />

                <div className="room-info">
                    <h2>Student Information on Tutor's Floor</h2>
                    <div className="room-details">
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
        </div>
    );
}

export default TutorDashboard;

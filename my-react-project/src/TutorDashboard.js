import React from 'react';
import './TutorDashboard.css'; // 导入样式文件

function TutorDashboard() {
    // 模拟数据，宿舍信息和学生信息
    const dormInfo = {
        dormitory: "宿舍名称",
        tutor: "Tutor名称",
        floor: 3, // 假设Tutor负责的楼层是第3层
        rooms: [
            { roomNumber: 301, students: ["学生1", "学生2"] },
            { roomNumber: 302, students: ["学生3", "学生4"] },
            // 可以添加更多的房间信息
        ]
    };

    return (
        <div className="container"> {/* 应用样式 */}
            <h1>Welcome, Tutor!</h1>

            <div>
                <h2>Tutor宿舍信息</h2>
                <p>宿舍名称：{dormInfo.dormitory}</p>
                <p>Tutor名称：{dormInfo.tutor}</p>
            </div>

            <div className="room-info"> {/* 应用样式 */}
                <h2>Tutor负责的楼层学生信息</h2>
                <ul>
                    {dormInfo.rooms.map(room => (
                        <li key={room.roomNumber}>
                            <strong>房间号：{room.roomNumber}</strong>
                            <ul>
                                {room.students.map(student => (
                                    <li key={student}>{student}</li>
                                ))}
                            </ul>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default TutorDashboard;

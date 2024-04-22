import React from 'react';
import { useLocation, useParams } from 'react-router-dom';

function RoomDetails() {
    const { roomNumber } = useParams();
    const { state } = useLocation();
    const { students } = state;

    return (
        <div className="room-details">
            <h1>Room {roomNumber} Details</h1>
            <ul>
                {students.map((student, index) => (
                    <li key={index}>
                        {student[1]} ({student[2]}) - {student[5]}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default RoomDetails;

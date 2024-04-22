import React from 'react';
import { useLocation, useParams } from 'react-router-dom';
import styles from './RoomDetails.module.css'; // Adjust the import path as needed
import backgroundImage from './bg.png'; // Ensure you have the correct path to your background image

function RoomDetails() {
    const { roomNumber } = useParams();
    const { state } = useLocation();
    const { students } = state;

    return (
        <div className={styles.pageBackground}>
            <div className={styles.roomDetails}>
                <h1 className={styles.title}>Room {roomNumber} Details</h1>
                <ul className={styles.list}>
                    {students.map((student, index) => (
                        <li key={index} className={styles.listItem}>
                            {student[1]} ({student[2]}) - {student[5]}
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default RoomDetails;

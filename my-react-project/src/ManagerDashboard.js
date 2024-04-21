import React, { useState } from 'react';
import './ManagerDashboard.css';

function ManagerDashboard() {
  const [roomLocation, setRoomLocation] = useState("Bld. A, Room 101");
  const [selectedFloor, setSelectedFloor] = useState('');
  const [showFloors, setShowFloors] = useState(false);

  // 切换折叠面板展开/收起的函数
  const toggleFloors = () => {
    setShowFloors(prevShowFloors => !prevShowFloors);
  };

  // 选择楼层的函数
  const selectFloor = (floor) => {
    setSelectedFloor(floor);
    setShowFloors(false); // 选择楼层后自动收起面板
  };

  return (
    <div className="supervisor-dashboard">
      <p>Your dom is at {roomLocation}</p>
      <p>Please select the floor you want to check.</p>
      <div className="dropdown">
        <button className="dropdown-button" onClick={toggleFloors}>
          {selectedFloor ? `Floor: ${selectedFloor}` : 'Select Floor'}
        </button>
        {showFloors && (
          <div className="dropdown-content">
            {['1st', '2nd', '3rd', '4th', '5th', '6th'].map(floor => (
              <div key={floor} onClick={() => selectFloor(floor)}>
                {floor}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default ManagerDashboard;

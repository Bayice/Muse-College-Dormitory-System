import React from 'react';
import { useLocation } from 'react-router-dom';
import styles from './ManSelectOutput.module.css'; 

function ManSelectOutput() {
  const location = useLocation();
  const info = location.state?.info;  
  const role = location.state ? location.state.role : null;

  // 渲染学生信息
  const renderStudentInfo = () => {
    if (!info || !info.users || info.users.length === 0) {
      return <p>No information received.</p>;
    }

    return info.users.map((user, index) => (
      <div key={index} className={styles.userInfo}>
        <p>姓名: {user[1]}</p>
        <p>学号: {user[0]}</p>
        <p>宿舍名: {user[5]}</p>
        <hr /> 
      </div>
    ));
  };

  // 渲染导师信息
  const renderTutorInfo = () => {
    if (!info || !info.users || info.users.length === 0) {
      return <p>No information received.</p>;
    }

    return info.users.map((user, index) => (
      <div key={index} className={styles.userInfo}>
        <p>姓名: {user[1]}</p>
        <p>导师ID: {user[0]}</p>
        <p>宿舍名: {user[3]}</p>
        <hr /> 
      </div>
    ));
  };

  // 根据角色选择渲染函数
  const renderInfo = () => {
    if (!role) return <p>角色信息未知。</p>;

    switch (role[0]) {
      case 'Tutor':
        return renderTutorInfo();
      case 'Student':
        return renderStudentInfo();
      default:
        return <p>角色信息未知。</p>;
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        <h1 className={styles.title}>舍监查询结果</h1>
        <div className={styles.content}>
          {renderInfo()}
        </div>
      </div>
    </div>
  );
}

export default ManSelectOutput;

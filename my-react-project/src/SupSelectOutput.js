import React from 'react';
import { useLocation } from 'react-router-dom';
import styles from './SupSelectOutput.module.css'; // Adjust the import path as needed

function SupSelectOutput() {
  const location = useLocation();
  const info = location.state?.info;  // Accessing the passed 'info' from state

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        <h1 className={styles.title}>Received Information</h1>
        <div className={styles.content}>
          {info ? (
            <pre>{JSON.stringify(info, null, 2)}</pre>  // Formatting the info for display
          ) : (
            <p>No information received.</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default SupSelectOutput;

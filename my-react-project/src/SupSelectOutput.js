import React from 'react';
import { useLocation } from 'react-router-dom';

function SupSelectOutput() {
  const location = useLocation();
  const info = location.state?.info;  // Accessing the passed 'info' from state

  return (
    <div>
      <h1>Received Information</h1>
      <div>
        {info ? (
          <pre>{JSON.stringify(info, null, 2)}</pre>  // Formatting the info for display
        ) : (
          <p>No information received.</p>
        )}
      </div>
    </div>
  );
}

export default SupSelectOutput;

import React, { useState } from 'react';
import axios from 'axios';
import './styles.css';

function App() {
  const [file, setFile] = useState(null);
  const [log, setLog] = useState([]);
  const [checksum, setChecksum] = useState('');

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('errorRate', 0.1);
    const res = await axios.post('http://localhost:5000/upload', formData);
    setChecksum(res.data.checksum);
    setLog(res.data.transmission);
  };

  return (
    <div className="App">
      <h2>Error Detection and Recovery</h2>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload and Simulate</button>
      <h4>Checksum: {checksum}</h4>
      <ul>
        {log.map((entry, idx) => (
          <li key={idx} className={entry.status}>
            [{entry.index}] Sent: {entry.original} → {entry.transmitted} ({entry.status})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

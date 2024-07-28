import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [analysisResult, setAnalysisResult] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    const response = await axios.post('/api/upload/', formData);
    setAnalysisResult(response.data);
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload and Analyze</button>
      {analysisResult && <div>{JSON.stringify(analysisResult)}</div>}
    </div>
  );
};

export default FileUpload;

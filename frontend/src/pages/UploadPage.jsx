import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export default function UploadPage() {
  const [file, setFile] = useState(null);
  const navigate = useNavigate();

  const handleUpload = async () => {
    const presign = await axios.post("http://localhost:8000/presign", null, { params: { filename: file.name } });
    const { url, fields } = presign.data.presign;
    const formData = new FormData();
    Object.entries(fields).forEach(([k, v]) => formData.append(k, v));
    formData.append("file", file);
    await fetch(url, { method: "POST", body: formData });
    const process = await axios.post("http://localhost:8000/process/glue", { s3_key: presign.data.s3_key });
    navigate(`/visualize/${process.data.job_id}`);
  };

  return (
    <div style={{ padding: 20 }}>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload & Process</button>
    </div>
  );
}

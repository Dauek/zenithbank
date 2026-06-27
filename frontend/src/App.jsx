import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [status, setStatus] = useState(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/health")
      .then(response => setStatus(response.data.status));
  }, []);

  return (
    <div>
      <h1>Zenith Bank</h1>
      <p>Status do backend: {status}</p>
    </div>
  );
}

export default App;
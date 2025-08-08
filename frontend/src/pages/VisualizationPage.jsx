import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import RuleChart from "../components/RuleChart";

export default function VisualizationPage() {
  const { jobId } = useParams();
  const [rules, setRules] = useState([]);

  useEffect(() => {
    axios.get(`http://localhost:8000/results/${jobId}`).then(res => setRules(res.data.rules));
  }, [jobId]);

  return (
    <div style={{ padding: 20 }}>
      <h2>Association Rules</h2>
      <RuleChart rules={rules} />
    </div>
  );
}

import { Bar } from "react-chartjs-2";
import { Chart as ChartJS } from "chart.js/auto";

export default function RuleChart({ rules }) {
  const labels = rules.map(r => `${r.antecedents.join(",")}→${r.consequents.join(",")}`);
  const data = {
    labels,
    datasets: [{
      label: "Confidence",
      data: rules.map(r => r.confidence),
      backgroundColor: "rgba(75,192,192,0.6)"
    }]
  };
  return <Bar data={data} />;
}

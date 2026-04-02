import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

const data = [
  { month: "May", risk: 800 },
  { month: "Jun", risk: 750 },
  { month: "Jul", risk: 680 }
];

export default function RiskTrendChart() {
  return (
    <div style={{height:300}}>
      <h3>Risk Score Trend</h3>

      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data}>
          <XAxis dataKey="month" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="risk" />
        </LineChart>
      </ResponsiveContainer>

    </div>
  );
}
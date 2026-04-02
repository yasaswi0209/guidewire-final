import Card from "../common/Card";

export default function WeatherCard() {
  return (
    <Card title="Weather Alert">
      <p>Rain expected tomorrow</p>
      <small>Risk score may increase due to wet roads</small>
    </Card>
  );
}
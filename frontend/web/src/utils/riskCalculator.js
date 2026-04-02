export function calculateRisk(weather, pollution) {
  if (weather === "rain" && pollution > 150) return ["High", "Heavy rain + high pollution"];
  if (weather === "rain") return ["Medium", "Rain expected"];
  if (pollution > 150) return ["High", "Severe pollution"];
  if (weather === "heat") return ["Medium", "Extreme heat"];
  return ["Low", "Normal conditions"];
}
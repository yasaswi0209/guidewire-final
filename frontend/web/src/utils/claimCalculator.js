export function calculateClaim(hoursLost) {
  const weeklyIncome = 4200;
  const dailyIncome = weeklyIncome / 7;
  const hourlyIncome = dailyIncome / 8;

  let loss = hourlyIncome * hoursLost;

  return loss * 2; // peak multiplier
}
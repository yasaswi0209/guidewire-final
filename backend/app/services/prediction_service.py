def calculate_risk(weather, aqi):

    score = 0

    # 🌧️ Rain
    if weather["rain"] > 70:
        score += 40
    elif weather["rain"] > 40:
        score += 20

    # 🌡️ Temperature
    if weather["temp"] > 35:
        score += 20

    # 🌫️ AQI
    if aqi > 150:
        score += 30
    elif aqi > 100:
        score += 15

    return score


def classify_risk(score):

    if score > 70:
        return "HIGH"
    elif score > 40:
        return "MEDIUM"
    else:
        return "LOW"


def get_recommendation(risk):

    if risk == "LOW":
        return {
            "plan": "Basic",
            "reason": "Low environmental risk",
            "confidence": 82
        }

    elif risk == "MEDIUM":
        return {
            "plan": "Moderate",
            "reason": "Moderate fluctuations detected",
            "confidence": 88
        }

    elif risk == "HIGH":
        return {
            "plan": "Premium",
            "reason": "High risk due to weather & pollution",
            "confidence": 95
        }
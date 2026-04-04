from app.utils.weather_api import get_weather_data, get_aqi_data

def check_and_trigger_payout(location: str):

    weather = get_weather_data(location)
    aqi = get_aqi_data(location)

    rain = weather["rain"]

    # 🚨 Smart trigger logic
    if aqi > 300:
        trigger = True
    elif rain == 1 and aqi > 150:
        trigger = True
    else:
        trigger = False

    if trigger:
        days = 3 if rain == 1 else 1
        payout = 500 * days

        return {
            "trigger": True,
            "payout": payout,
            "aqi": aqi,
            "rain": rain,
            "message": "Auto payout triggered 🚀"
        }

    return {
        "trigger": False,
        "payout": 0,
        "aqi": aqi,
        "rain": rain
    }
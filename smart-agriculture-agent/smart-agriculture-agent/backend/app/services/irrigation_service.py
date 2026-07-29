def irrigation_recommendation(temperature, humidity, rainfall, soil_moisture):
    score = 0
    if soil_moisture < 30:
        score += 3
    elif soil_moisture < 50:
        score += 1
    if temperature > 30:
        score += 2
    if humidity < 40:
        score += 1
    if rainfall > 10:
        score -= 3

    if score >= 4:
        recommendation = "Irrigation may be required soon. Check soil conditions before watering."
    elif score >= 2:
        recommendation = "Moderate irrigation need. Monitor soil moisture."
    else:
        recommendation = "Irrigation may not be immediately necessary."

    return {"score": score, "recommendation": recommendation}

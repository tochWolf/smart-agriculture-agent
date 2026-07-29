import { useState } from "react";
import { getWeather } from "../services/api";

export default function WeatherCard() {
  const [city, setCity] = useState("Nagpur");
  const [weather, setWeather] = useState(null);

  async function handleSearch() {
    try { setWeather(await getWeather(city)); }
    catch { setWeather({ available: false, message: "Unable to fetch weather." }); }
  }

  return (
    <section className="card">
      <h2>🌦️ Weather Intelligence</h2>
      <input value={city} onChange={(e) => setCity(e.target.value)} placeholder="Enter city" />
      <button onClick={handleSearch}>Get Weather</button>
      {weather && (weather.available ? <div className="result">
        <h3>{weather.city}</h3>
        <p>Temperature: {weather.temperature}°C</p>
        <p>Humidity: {weather.humidity}%</p>
        <p>Conditions: {weather.weather}</p>
      </div> : <div className="result"><p>{weather.message}</p></div>)}
    </section>
  );
}

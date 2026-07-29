import Assistant from "./components/Assistant";
import CropRecommendation from "./components/CropRecommendation";
import DiseaseDetector from "./components/DiseaseDetector";
import WeatherCard from "./components/WeatherCard";
import "./styles.css";

export default function App() {
  return (
    <div className="app">
      <header>
        <span className="badge">AI AGRICULTURE PLATFORM</span>
        <h1>Smart Agriculture AI</h1>
        <p>Intelligent crop insights, disease detection, weather intelligence and AI-powered farming assistance.</p>
      </header>
      <main>
        <div className="grid">
          <CropRecommendation />
          <DiseaseDetector />
          <WeatherCard />
          <Assistant />
        </div>
      </main>
      <footer>Smart Agriculture AI • Built with AI/ML</footer>
    </div>
  );
}

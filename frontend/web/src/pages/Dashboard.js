import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { useContext, useEffect, useState } from "react";
import { AppContext } from "../utils/AppContext";
import axios from "axios";

// ✅ MAP
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const chartData = [
  { day: "Mon", earnings: 600, city: 650 },
  { day: "Tue", earnings: 500, city: 600 },
  { day: "Wed", earnings: 700, city: 720 },
  { day: "Thu", earnings: 400, city: 500 },
  { day: "Fri", earnings: 800, city: 850 }
];

function Dashboard() {

  const { plan, setPlan, premium, setPremium } = useContext(AppContext);
  const navigate = useNavigate();

  const [data, setData] = useState(null);
  const [position, setPosition] = useState([17.385, 78.4867]);

  const city = localStorage.getItem("city");

  // ✅ AI Recommendation Logic
  function getRecommendationDetails(risk){
    if(risk === "LOW"){
      return {
        plan: "Basic",
        reason: "Low risk detected. Minimal coverage is sufficient.",
        confidence: 82
      };
    }
    if(risk === "MEDIUM"){
      return {
        plan: "Moderate",
        reason: "Moderate environmental & demand fluctuations detected.",
        confidence: 88
      };
    }
    if(risk === "HIGH"){
      return {
        plan: "Premium",
        reason: "High risk due to weather, demand drops, or accidents.",
        confidence: 95
      };
    }
    return null;
  }

  const recommendation = getRecommendationDetails(data?.risk);

  // 🔥 FETCH DATA
  useEffect(() => {
    async function fetchData(){
      try{
        const res = await axios.get(
          `http://localhost:8000/risk?city=${city}`
        );
        setData(res.data);

        const token = localStorage.getItem("token");

        if(token){
          const ins = await axios.get(
            "http://localhost:8000/insurance/my",
            {
              headers:{ Authorization: `Bearer ${token}` }
            }
          );
          setPlan(ins.data.plan_name);
          setPremium(ins.data.premium);
        }

      }catch(err){
        console.error(err);
      }
    }
    fetchData();
  }, [city, setPlan, setPremium]);

  // 📍 LOCATION
  useEffect(() => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (pos) => {
          setPosition([pos.coords.latitude, pos.coords.longitude]);
        },
        (err) => console.error(err)
      );
    }
  }, []);

  return (

    <section className="scene active">

      <div className="scene-layout scene-2-layout">

        {/* HEADER */}
        <div style={{marginBottom:"20px"}}>
          <h2>Dashboard Overview</h2>
          <p className="muted">📍 {city}</p>
        </div>

        {/* STATS */}
        <div className="dash-stats-grid">

          <motion.div className="dash-stat-card">
            <p className="dsc-label">Risk Level</p>
            <h3 className={`risk-indicator ${data?.risk?.toLowerCase()}`}>
              {data?.risk || "Loading..."}
            </h3>
          </motion.div>

          <motion.div
            className="dash-stat-card clickable"
            onClick={() => navigate("/pool")}
          >
            <p className="dsc-label">Community Pool</p>
            <h3 className="dsc-value">₹1,50,000</h3>
          </motion.div>

          <motion.div className="dash-stat-card">
            <p className="dsc-label">Active Plan</p>
            <h3>{plan || "No Plan"}</h3>
          </motion.div>

          <motion.div className="dash-stat-card">
            <p className="dsc-label">Weekly Premium</p>
            <h3>₹{premium || 0}</h3>
          </motion.div>

        </div>

        {/* 🔥 AI RECOMMENDATION */}
        <motion.div className="dashboard-panel">
          <h3 className="dp-title">AI Recommendation</h3>

          {recommendation ? (
            <>
              <p><b>Plan:</b> {recommendation.plan}</p>
              <p><b>Reason:</b> {recommendation.reason}</p>
              <p><b>Confidence:</b> {recommendation.confidence}%</p>
            </>
          ) : (
            <p>Analyzing...</p>
          )}
        </motion.div>

        {/* GRAPH + MAP */}
        <div className="dashboard-bottom-grid">

          {/* GRAPH */}
          <motion.div className="dashboard-panel">
            <h3 className="dp-title">Income Disruption Trend</h3>

            <ResponsiveContainer width="100%" height={260}>
              <BarChart data={chartData}>
                <CartesianGrid stroke="#e5e7eb" />
                <XAxis dataKey="day" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="city" fill="#d1d5db" />
                <Bar dataKey="earnings" fill="#ef4444" />
              </BarChart>
            </ResponsiveContainer>
          </motion.div>

          {/* MAP */}
          <motion.div className="dashboard-panel" style={{ height: "300px" }}>
            <h3 className="dp-title">Your Location</h3>

            <MapContainer
              center={position}
              zoom={13}
              style={{ height: "100%", width: "100%" }}
            >
              <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
              <Marker position={position}>
                <Popup>You are here 📍</Popup>
              </Marker>
            </MapContainer>
          </motion.div>

        </div>

      </div>

    </section>
  );
}

export default Dashboard;
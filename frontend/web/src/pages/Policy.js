import { useContext, useState, useEffect, useMemo } from "react";
import { AppContext } from "../utils/AppContext";
import { motion } from "framer-motion";
import axios from "axios";

function Policy(){

  const { plan, setPlan, risk } = useContext(AppContext);

  const [selectedPlan, setSelectedPlan] = useState(null);

  // 🧠 AI LOGIC
  function getRecommendedPlan(risk){
    if(risk === "LOW") return "Basic";
    if(risk === "MEDIUM") return "Moderate";
    if(risk === "HIGH") return "Premium";
    return null;
  }

  const recommendedPlan = getRecommendedPlan(risk);

  // ⚡ STABLE DATA (NO RE-RENDER ISSUE)
  const plans = useMemo(() => [
    {
      name:"Basic",
      price:20,
      desc:"Low risk coverage",
      features:[
        "Rain protection",
        "Low demand cover",
        "UPI payout"
      ]
    },
    {
      name:"Moderate",
      price:30,
      desc:"Balanced coverage",
      features:[
        "Rain protection",
        "Pollution cover",
        "Demand drop cover",
        "UPI payout"
      ]
    },
    {
      name:"Premium",
      price:50,
      desc:"Full AI protection",
      features:[
        "Rain + heat cover",
        "Accident protection",
        "Demand drop cover",
        "Priority payout",
        "Peak bonus"
      ]
    }
  ], []);

  // 🤖 AUTO SELECT BASED ON AI
  useEffect(()=>{
    if(recommendedPlan){
      const autoPlan = plans.find(p => p.name === recommendedPlan);
      setSelectedPlan(autoPlan);
    }
  }, [recommendedPlan, plans]);

  // 🔥 CONFIRM API
  async function handleConfirm(){
  if(!selectedPlan){
    alert("Please select a plan first ⚠️");
    return;
  }

  const token = localStorage.getItem("token");

  // 🔴 ADD THIS CHECK
  if(!token){
    alert("Please login first ⚠️");
    return;
  }

  try{
    await axios.post(
      "http://localhost:8000/insurance",
      {
        plan_name: selectedPlan.name,
        premium: selectedPlan.price,
        coverage: selectedPlan.price * 1000
      },
      {
        headers:{
          Authorization: `Bearer ${token}`
        }
      }
    );

    setPlan(selectedPlan.name);
    alert("Plan activated ✅");

  }catch(err){
    console.error("FULL ERROR:", err.response?.data || err.message);

    // 🔥 BETTER ERROR MESSAGE
    if(err.response?.status === 401){
        localStorage.removeItem("token");  
      alert("Session expired. Please login again 🔑");
    } else if(err.response?.status === 400){
      alert(err.response.data.detail);
    } else {
      alert("Failed to select plan ❌");
    }
  }
}

  return(

    <section className="scene active">
      <div className="policy-container">

        <h1 className="page-title">
          Choose Protection Plan
        </h1>

        <div className="pricing-grid">

          {plans.map(p => {

            const active = selectedPlan?.name === p.name;
            const isRecommended = recommendedPlan === p.name;

            return(

              <motion.div
                key={p.name}
                className={`price-card 
                  ${active ? "active glow" : ""} 
                  ${isRecommended ? "highlight" : ""}
                `}
                whileHover={{scale:1.05}}
                initial={{opacity:0, y:30}}
                animate={{opacity:1, y:0}}
                transition={{duration:0.4}}
                onClick={()=>setSelectedPlan(p)}
              >

                {/* 🔥 AI BADGE */}
                {isRecommended && (
                  <div className="badge">
                    Recommended
                  </div>
                )}

                <h2>{p.name}</h2>

                <h1>
                  ₹{p.price}
                  <span>/week</span>
                </h1>

                <p className="muted">{p.desc}</p>

                <ul>
                  {p.features.map(f => (
                    <li key={f}>✔ {f}</li>
                  ))}
                </ul>

                <button className="btn" disabled={active}>
                  {active ? "Selected" : "Select Plan"}
                </button>

              </motion.div>
            )
          })}

        </div>

        {/* 🚀 CONFIRM BUTTON */}
        <div style={{textAlign:"center", marginTop:"20px"}}>
          <button className="btn-primary" onClick={handleConfirm}>
            Confirm Plan 🚀
          </button>
        </div>

        {/* 🏆 ACTIVE PLAN */}
        {plan && (
          <motion.div
            className="reward-box"
            initial={{opacity:0}}
            animate={{opacity:1}}
          >
            🏆 {plan} Plan Active
          </motion.div>
        )}

      </div>
    </section>
  );
}

export default Policy;
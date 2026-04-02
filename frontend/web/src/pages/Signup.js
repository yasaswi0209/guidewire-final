import { useState } from "react";
import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";
import axios from "axios";

function Signup(){

  const navigate = useNavigate();

  const [name,setName] = useState("");
  const [email,setEmail] = useState("");
  const [password,setPassword] = useState("");

  // ✅ NEW STATES
  const [platform,setPlatform] = useState("");
  const [location,setLocation] = useState("");
  const [income,setIncome] = useState("");

  async function handleSignup(){

    if(!name || !email || !password || !platform || !location || !income){
      alert("Please fill all fields");
      return;
    }

    try{
      const res = await axios.post(
        "http://localhost:8000/auth/signup",
        {
          name: name,
          email: email,
          password: password,

          // ✅ SEND EXTRA DATA
          platform: platform,
          location: location,
          weekly_income: Number(income)
        }
      );

      console.log(res.data);

      alert("Signup Successful 🎉");

      localStorage.setItem("user", JSON.stringify({
  name: name,
  email: email
}));
localStorage.setItem("city", location);

      navigate("/dashboard");

    }catch(err){
      console.error(err);
      alert("Signup failed ❌");
    }

  }

  return(

    <section className="auth-page">

      <div className="auth-container">

        {/* LEFT */}
        <div className="auth-left">

          <h1>
            Start protecting your income today
          </h1>

          <p>
            AI powered insurance for gig workers.
            Instant claim settlement.
          </p>

          <img
            src="https://cdn-icons-png.flaticon.com/512/2972/2972185.png"
            alt="bike"
          />

        </div>

        {/* RIGHT */}
        <motion.form
  className="auth-box"
  initial={{opacity:0, y:20}}
  animate={{opacity:1, y:0}}
  onSubmit={(e)=>{
    e.preventDefault();   // ✅ prevents duplicate calls
    handleSignup();
  }}
>

          <h2 className="auth-title">
            Create Account
          </h2>

          <p className="muted">
            Join GigShield AI protection
          </p>

          {/* BASIC INFO */}
          <input
            className="input"
            placeholder="Full Name"
            value={name}
            onChange={(e)=>setName(e.target.value)}
          />

          <input
            className="input"
            placeholder="Email"
            value={email}
            onChange={(e)=>setEmail(e.target.value)}
          />

          <input
            className="input"
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e)=>setPassword(e.target.value)}
          />

          {/* ✅ NEW FIELDS */}

          {/* Platform Dropdown */}
          <select
            className="input"
            value={platform}
            onChange={(e)=>setPlatform(e.target.value)}
          >
            <option value="">Select Platform</option>
            <option value="Zomato">Zomato</option>
            <option value="Swiggy">Swiggy</option>
            
          </select>

          {/* Location */}
          <input
            className="input"
            placeholder="Work Location (City)"
            value={location}
            onChange={(e)=>setLocation(e.target.value)}
          />

          {/* Weekly Income */}
          <input
            className="input"
            type="number"
            placeholder="Weekly Income (₹)"
            value={income}
            onChange={(e)=>setIncome(e.target.value)}
          />

          <button type="submit" className="btn-primary">
  Signup
</button>

          <p className="muted">
            Already have account?

            <span
              className="link"
              onClick={()=>navigate("/login")}
            >
              Login
            </span>

          </p>

        </motion.form> ✅

      </div>

    </section>

  );

}

export default Signup;
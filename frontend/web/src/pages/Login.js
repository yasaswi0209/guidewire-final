import { useState } from "react";
import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";
import axios from "axios";

function Login(){

  const navigate = useNavigate();

  const [email,setEmail] = useState("");
  const [password,setPassword] = useState("");

  async function handleLogin(){

    if(!email || !password){
      alert("Please enter email and password");
      return;
    }

    try{

      // 🔥 FIX: Use form-data instead of JSON
      const formData = new URLSearchParams();
      formData.append("username", email);   // MUST be username
      formData.append("password", password);

      const res = await axios.post(
        "http://127.0.0.1:8000/auth/login",
        formData,
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded"
          }
        }
      );

      console.log(res.data);

      // ✅ Save user
     localStorage.setItem("user", JSON.stringify({
  name: res.data.name,
  email: email
}));

      // 🔥 FIX: correct token key
      if(res.data.access_token){
        localStorage.setItem("token", res.data.access_token);
      }

      alert("Login Success 🚀");

      navigate("/dashboard");

    }catch(err){
      console.error(err.response?.data || err);
      alert("Invalid credentials ❌");
    }

  }

  return(

    <section className="auth-page">

      <div className="auth-container">

        {/* LEFT */}
        <div className="auth-left">

          <h1>
            Protect your income with AI
          </h1>

          <p>
            Insurance built for delivery workers.
            Instant protection against disruption.
          </p>

          <img
            src="https://cdn-icons-png.flaticon.com/512/2972/2972185.png"
            alt="bike"
          />

        </div>


        {/* RIGHT */}
        <motion.div
          className="auth-box"
          initial={{opacity:0, y:20}}
          animate={{opacity:1, y:0}}
        >

          <h2 className="auth-title">
            Welcome Back
          </h2>

          <p className="muted">
            Login to continue
          </p>

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

          <button
            className="btn-primary"
            onClick={handleLogin}
          >
            Login
          </button>

          <p className="muted">
            New user?

            <span
              className="link"
              onClick={()=>navigate("/signup")}
            >
              Create account
            </span>

          </p>

        </motion.div>

      </div>

    </section>

  );

}

export default Login;
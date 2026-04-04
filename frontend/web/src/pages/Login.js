import { useState } from "react";
import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useAuth } from "../pages/AuthContext"; // adjust path if moved

function Login() {

  const navigate = useNavigate();
  const { login } = useAuth(); // 🔥 use context

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleLogin() {

    if (!email || !password) {
      setError("Please enter email and password");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const formData = new URLSearchParams();
      formData.append("username", email);
      formData.append("password", password);

      const res = await axios.post(
        "https://guidewire-final.onrender.com/auth/login",
        formData,
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded"
          }
        }
      );

      // 🔥 use context instead of localStorage directly
      login(
        {
          name: res.data.user.name,
          email: email
        },
        res.data.access_token
      );

      navigate("/dashboard");

    } catch (err) {
      setError("Invalid credentials ❌");
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="auth-page">
      <div className="auth-container">

        {/* LEFT */}
        <div className="auth-left">
          <h1>Protect your income with AI</h1>
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
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
        >

          <h2 className="auth-title">Welcome Back</h2>
          <p className="muted">Login to continue</p>

          {/* 🔥 ERROR MESSAGE */}
          {error && (
            <div style={{
              background: "#ffe6e6",
              color: "#d8000c",
              padding: "10px",
              borderRadius: "6px",
              marginBottom: "10px"
            }}>
              {error}
            </div>
          )}

          <input
            className="input"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <input
            className="input"
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button
            className="btn-primary"
            onClick={handleLogin}
            disabled={loading}
          >
            {loading ? "Logging in..." : "Login"}
          </button>

          <p className="muted">
            New user?{" "}
            <span
              className="link"
              onClick={() => navigate("/signup")}
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
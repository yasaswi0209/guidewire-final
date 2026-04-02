import { Link, useLocation } from "react-router-dom";
import { Home, LayoutDashboard, Shield, FileText, Activity } from "lucide-react";
function Sidebar() {
  const location = useLocation();

  const menu = [
    { name: "Home", path: "/" },
    { name: "Dashboard", path: "/dashboard" },
    { name: "Policy", path: "/policy" },
    { name: "Claims", path: "/claims" },
    { name: "Risk", path: "/risk" }
  ];
  <Home size={18} />
  return (
    <div style={{
      width: "240px",
      height: "100vh",
      background: "linear-gradient(180deg, #020617, #1e293b)",
      padding: "20px"
    }}>
      <h2 style={{ color: "#6366f1" }}>GigShield AI</h2>

      <div style={{ marginTop: "30px" }}>
        {menu.map((item) => (
          <Link
            key={item.path}
            to={item.path}
            style={{
              display: "block",
              padding: "12px",
              borderRadius: "8px",
              marginBottom: "10px",
              textDecoration: "none",
              color: "#e2e8f0",
              background:
                location.pathname === item.path ? "#6366f1" : "transparent"
            }}
          >
            {item.name}
          </Link>
        ))}
      </div>
    </div>
  );
}

export default Sidebar;
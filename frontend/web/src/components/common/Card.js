function Card({ title, children }) {
  return (
    <div style={{
      background: "#ffffff",
      padding: "20px",
      borderRadius: "12px",
      boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
      marginBottom: "20px"
    }}>
      <h3>{title}</h3>
      {children}
    </div>
  );
}

export default Card;
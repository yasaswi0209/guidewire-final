import { createContext, useState, useEffect } from "react";

export const AppContext = createContext();

// ✅ Move outside (IMPORTANT FIX)
const premiumMap = {
  Basic: 20,
  Moderate: 30,
  Premium: 50
};

export function AppProvider({ children }) {

  const [plan, setPlan] = useState("Basic");
  const [premium, setPremium] = useState(20);

  useEffect(() => {
    setPremium(premiumMap[plan] || 0);
  }, [plan]); // ✅ now only plan is enough

  return (
    <AppContext.Provider
      value={{
        plan,
        setPlan,
        premium,
        setPremium
      }}
    >
      {children}
    </AppContext.Provider>
  );
}
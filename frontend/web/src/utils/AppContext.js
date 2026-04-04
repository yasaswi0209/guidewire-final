import { createContext, useState, useEffect } from "react";

export const AppContext = createContext();

export function AppProvider({ children }) {

  const [plan, setPlan] = useState("Basic");
  const [premium, setPremium] = useState(20); // ✅ NEW STATE

  const premiumMap = {
    Basic: 20,
    Moderate: 30,
    Premium: 50
  };

  // ✅ Auto update premium when plan changes
  useEffect(() => {
  setPremium(premiumMap[plan] || 0);
}, [plan, premiumMap]);

  return (
    <AppContext.Provider
      value={{
        plan,
        setPlan,
        premium,
        setPremium   // ✅ FIXED (no more error)
      }}
    >
      {children}
    </AppContext.Provider>
  );
}
import { createContext, useState } from "react";

export const AppContext = createContext();

export function AppProvider({children}){

const [plan,setPlan] = useState("Basic");

const premiumMap = {

Basic:20,

Moderate:30,

Premium:50

};

return(

<AppContext.Provider

value={{

plan,

setPlan,

premium: premiumMap[plan]

}}

>

{children}

</AppContext.Provider>

);

}
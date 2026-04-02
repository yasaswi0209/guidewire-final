import {
BrowserRouter,
Routes,
Route,
Navigate,
useLocation
} from "react-router-dom";
import { AnimatePresence } from "framer-motion";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import ProtectedRoute from "./utils/ProtectedRoute";
import Navbar from "./components/Navbar";
import Dock from "./components/Dock";
import "leaflet/dist/leaflet.css";
import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import Policy from "./pages/Policy";
import Claims from "./pages/Claims";
import RiskAnalysis from "./pages/RiskAnalysis";
import PoolDetails from "./pages/PoolDetails";

import { AppProvider } from "./utils/AppContext";


function AppWrapper(){

const location = useLocation();

return(

<div className="app">

<Navbar/>

<div className="content">

<AnimatePresence mode="wait">

<Routes location={location} key={location.pathname}>

<Route path="/" element={<Home/>} />

<Route path="/login" element={<Login/>} />

<Route path="/signup" element={<Signup/>} />


{/* PROTECTED */}

<Route path="/dashboard" element={
<ProtectedRoute>
<Dashboard/>
</ProtectedRoute>
} />

<Route path="/policy" element={
<ProtectedRoute>
<Policy/>
</ProtectedRoute>
} />

<Route path="/claims" element={
<ProtectedRoute>
<Claims/>
</ProtectedRoute>
} />

<Route path="/risk" element={
<ProtectedRoute>
<RiskAnalysis/>
</ProtectedRoute>
} />

<Route path="/pool" element={
<ProtectedRoute>
<PoolDetails/>
</ProtectedRoute>
} />


<Route path="*" element={<Navigate to="/"/>} />

</Routes>
</AnimatePresence>

</div>

<Dock/>

</div>

)

}



function App(){

return(

<BrowserRouter>

<AppProvider>

<AppWrapper/>

</AppProvider>

</BrowserRouter>

)

}

export default App;
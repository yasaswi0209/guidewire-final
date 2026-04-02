import { NavLink } from "react-router-dom";

function Dock(){

return(

<div className="dock">

<NavLink to="/" className="dock-item">

🏠

<span>

Home

</span>

</NavLink>


<NavLink to="/dashboard" className="dock-item">

📊

<span>

Dashboard

</span>

</NavLink>


<NavLink to="/policy" className="dock-item">

📄

<span>

Policy

</span>

</NavLink>


<NavLink to="/claims" className="dock-item">

💰

<span>

Claims

</span>

</NavLink>


<NavLink to="/risk" className="dock-item">

⚡

<span>

Risk

</span>

</NavLink>

</div>

);

}

export default Dock;
import { useState, useEffect, useRef } from "react";
import { motion } from "framer-motion";

import {
LineChart,
Line,
XAxis,
YAxis,
Tooltip,
CartesianGrid,
ResponsiveContainer
} from "recharts";


/* risk history */

const history = [

{ date:"Mon", risk:40 },

{ date:"Tue", risk:55 },

{ date:"Wed", risk:70 },

{ date:"Thu", risk:50 },

{ date:"Fri", risk:65 }

];


/* simulated live data */

const liveData = {

weather:"rain",
aqi:165

};


function RiskAnalysis(){

const [weather,setWeather] = useState("");
const [pollution,setPollution] = useState("");
const [risk,setRisk] = useState("");
const [reason,setReason] = useState("");
const [status,setStatus] = useState("");
const [open,setOpen] = useState(false);

const dropdownRef = useRef();


const options = [

{ value:"rain", label:"🌧 Rain" },

{ value:"heat", label:"🔥 Heat" },

{ value:"normal", label:"☀ Normal" }

];



/* simulate auto detection */

useEffect(()=>{

setTimeout(()=>{

setWeather(liveData.weather);
setPollution(liveData.aqi);

},800);

},[]);



function calculateRisk(){

if(!weather || !pollution){

setRisk("Error");
setReason("Missing input");
return;

}

setStatus("analyzing");


setTimeout(()=>{

let level="";
let reasonText="";




if(weather==="rain" && pollution>150){

level="High";
reasonText="Rain + poor air quality";

}

else if(weather==="rain"){

level="Medium";
reasonText="Rain disruption possible";

}

else if(weather==="heat"){

level="Medium";
reasonText="Extreme heat fatigue";

}

else if(pollution>150){

level="High";
reasonText="Severe pollution";

}

else{

level="Low";
reasonText="Normal environment";

}


setRisk(level);
setReason(reasonText);
setStatus("done");

},1200);

}



const color =

risk==="High" ? "#ef4444" :
risk==="Medium" ? "#f59e0b" :
"#22c55e";



return(

<section className="scene active risk-page">

<div className="scene-layout scene-2-layout">


{/* LEFT SIDE */}

<div>


{/* analytics cards */}

<div className="dash-stats-grid">

<StatCard title="Accuracy" value="91%"/>

<StatCard title="Data Sources" value="12"/>

<StatCard title="Prediction Time" value="1.2s"/>

</div>



{/* input panel */}

<motion.div
className="dashboard-panel"
initial={{opacity:0}}
animate={{opacity:1}}
>

<h3 className="dp-title">
Environment Inputs
</h3>



<div className="ai-suggestion">

AI detected:
<b> 🌧 Rain</b> | AQI <b>{pollution}</b>

</div>



<div className="risk-grid">


<div ref={dropdownRef}>

<label>
Weather
</label>


<div
className="dropdown"
onClick={()=>setOpen(!open)}
>

{weather

? options.find(o=>o.value===weather)?.label

: "Select weather"}

▾

</div>



{open && (

<div className="dropdown-list">

{options.map(opt=>(

<div
key={opt.value}
className="dropdown-item"
onClick={()=>{

setWeather(opt.value);
setOpen(false);

}}
>

{opt.label}

</div>

))}

</div>

)}

</div>



<div>

<label>
AQI
</label>


<input
className="input"
value={pollution}
onChange={e=>setPollution(e.target.value)}
/>

</div>


</div>



<button
className="btn"
onClick={calculateRisk}
>

Analyze Risk

</button>



</motion.div>



{/* trend */}

<div className="dashboard-panel">

<h3 className="dp-title">
Risk Trend
</h3>


<ResponsiveContainer width="100%" height={180}>

<LineChart data={history}>

<CartesianGrid stroke="#eee"/>

<XAxis dataKey="date"/>

<YAxis/>

<Tooltip/>


<Line
type="monotone"
dataKey="risk"
stroke="#ef4444"
strokeWidth={2}
/>

</LineChart>

</ResponsiveContainer>


</div>


</div>



{/* RIGHT SIDE */}

<div>


<motion.div
className="dashboard-panel"
initial={{opacity:0}}
animate={{opacity:1}}
>

<h3 className="dp-title">
AI Risk Decision
</h3>



{status==="" && (

<p className="muted">

System ready for analysis.

</p>

)}



{status==="analyzing" && (

<div className="status-card warn">

🤖 analyzing multi-source signals...

</div>

)}



{status==="done" && (

<motion.div
className="risk-result"
initial={{scale:0.9}}
animate={{scale:1}}
>

<h2>
Risk Level
</h2>


<h1 style={{color}}>
{risk}
</h1>


<p>
{reason}
</p>


<div className={`risk-pill ${risk.toLowerCase()}`}>
risk {risk}
</div>


<div className="ai-recommend">

AI recommends precaution for delivery workers.

</div>


</motion.div>

)}



</motion.div>



{/* history */}

<div className="dashboard-panel">

<h3 className="dp-title">
Risk History
</h3>


<div className="claim-history-item">

<span>Rain</span>

<span className="risk-pill high">
High
</span>

<span>Today</span>

</div>


<div className="claim-history-item">

<span>Heat</span>

<span className="risk-pill medium">
Medium
</span>

<span>Yesterday</span>

</div>


</div>


</div>



</div>

</section>

)

}



function StatCard({title,value}){

return(

<div className="dash-stat-card">

<p className="dsc-label">
{title}
</p>

<h3>
{value}
</h3>

</div>

)

}


export default RiskAnalysis;
import { useState, useRef, useEffect } from "react";
import { motion } from "framer-motion";


const history = [

{ type:"Rain", payout:310, date:"12 Mar" },

{ type:"Heat", payout:420, date:"3 Mar" },

{ type:"Pollution", payout:180, date:"25 Feb" }

];


function Claims(){

const [selected,setSelected] = useState("");
const [open,setOpen] = useState(false);
const [status,setStatus] = useState("");
const [payout,setPayout] = useState(null);
const [reason,setReason] = useState("");
const [confidence,setConfidence] = useState(null);
const [risk,setRisk] = useState(null);

const dropdownRef = useRef();


const options = [

{ value:"rain", label:"🌧 Heavy Rain" },

{ value:"pollution", label:"🌫 High Pollution" },

{ value:"heat", label:"🔥 Extreme Heat" },

{ value:"curfew", label:"🚫 Curfew" }

];



/* close dropdown outside click */

useEffect(()=>{

function close(e){

if(
dropdownRef.current &&
!dropdownRef.current.contains(e.target)
){

setOpen(false);

}

}

document.addEventListener("mousedown",close);

return ()=>document.removeEventListener("mousedown",close);

},[]);



/* auto suggestion */

useEffect(()=>{

setTimeout(()=>{

setSelected("rain");

},700);

},[]);



function handleApply(){

if(!selected){

setStatus("rejected");

setReason("Select disruption");

return;

}

setStatus("verifying");

setPayout(null);

setConfidence(null);



setTimeout(()=>{

const weeklyIncome = 4200;

const hourlyIncome = (weeklyIncome/7)/8;

let hoursLost = 0;

let msg = "";
let conf = 0.9;



switch(selected){

case "rain":
hoursLost = 3;
msg="Rain disruption verified";
conf=0.94;
break;

case "pollution":
hoursLost = 2;
msg="Pollution disruption verified";
conf=0.88;
break;

case "heat":
hoursLost = 4;
msg="Heat disruption verified";
conf=0.92;
break;

default:
setStatus("rejected");
setRisk("high");
return;

}



const loss = Math.round(hourlyIncome*hoursLost*2);

setReason(msg);
setPayout(loss);
setConfidence(Math.round(conf*100));
setRisk(conf>0.9 ? "low":"medium");

setStatus("approved");

},1400);

}



return(

<section className="scene active">

<div className="scene-layout scene-2-layout">



{/* LEFT SIDE */}

<div className="claims-left">


<motion.div
className="dashboard-panel"
initial={{opacity:0}}
animate={{opacity:1}}
>

<h3 className="dp-title">
AI Claim Engine
</h3>



<div className="workflow-box">

<WorkflowStep label="Submit" active/>

<WorkflowStep
label="AI Review"
active={status==="verifying"}
/>

<WorkflowStep
label="Payout"
active={status==="approved"}
/>

</div>



<div className="ai-suggestion">

AI detected disruption:
<b> 🌧 Heavy Rain</b>

</div>



<div
ref={dropdownRef}
className="dropdown-box"
>

<label>
Confirm disruption
</label>



<div
className="dropdown"
onClick={()=>setOpen(!open)}
>

<span>

{selected

? options.find(o=>o.value===selected)?.label

: "Choose disruption"}

</span>

<span>▾</span>

</div>



{open && (

<motion.div
className="dropdown-list"
initial={{opacity:0}}
animate={{opacity:1}}
>

{options.map(opt=>(

<div
key={opt.value}
className="dropdown-item"
onClick={()=>{

setSelected(opt.value);
setOpen(false);

}}
>

{opt.label}

</div>

))}

</motion.div>

)}

</div>



<motion.button
className="btn"
onClick={handleApply}
whileHover={{scale:1.05}}
>

Check Eligibility

</motion.button>



</motion.div>



{/* HISTORY */}

<motion.div
className="dashboard-panel"
initial={{opacity:0}}
animate={{opacity:1}}
>

<h3 className="dp-title">
Recent Claims
</h3>



{history.map((h,i)=>(

<div
key={i}
className="claim-history-item"
>

<span>{h.type}</span>

<span>₹{h.payout}</span>

<span className="muted">{h.date}</span>

</div>

))}



</motion.div>


</div>



{/* RIGHT SIDE */}

<div className="claims-right">

<motion.div
className="dashboard-panel decision-panel"
initial={{opacity:0}}
animate={{opacity:1}}
>

<h3 className="dp-title">
AI Decision
</h3>



{status==="" && (

<p className="muted">

Select disruption to estimate payout.

</p>

)}



{status==="verifying" && (

<div className="status-card warn">

🤖 analysing weather & demand signals...

</div>

)}



{status==="approved" && (

<motion.div
className="status-card success payout-card"
initial={{scale:0.9}}
animate={{scale:1}}
>

<h3>{reason}</h3>

<h1>₹{payout}</h1>

<p>AI confidence {confidence}%</p>

<p className={`risk-pill ${risk}`}>
risk level {risk}
</p>

<p>sent instantly via UPI</p>

</motion.div>

)}



{status==="rejected" && (

<div className="status-card danger">

claim not eligible

</div>

)}



</motion.div>

</div>



</div>

</section>

)

}



/* workflow component */

function WorkflowStep({label,active}){

return(

<div className={`workflow-step ${active?"active":""}`}>

<div className="dot"/>

{label}

</div>

)

}



export default Claims;
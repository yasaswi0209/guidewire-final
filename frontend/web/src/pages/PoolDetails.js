import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";

import { motion } from "framer-motion";
import { useState } from "react";


/* SAMPLE DATA */

const workers = [

  { name: "Ravi", city: "Hyderabad", contribution: 30, payout: 0 },

  { name: "Amit", city: "Hyderabad", contribution: 20, payout: 310 },

  { name: "Priya", city: "Hyderabad", contribution: 50, payout: 0 },

  { name: "Rahul", city: "Hyderabad", contribution: 30, payout: 120 },

  { name: "Sneha", city: "Hyderabad", contribution: 40, payout: 0 }

];


const payoutTrend = [

  { month: "Jan", contribution: 12000, payout: 8000 },

  { month: "Feb", contribution: 15000, payout: 6000 },

  { month: "Mar", contribution: 18000, payout: 9000 },

  { month: "Apr", contribution: 17000, payout: 4000 }

];



function PoolDetails(){

  const [search,setSearch] = useState("");

  const filteredWorkers = workers.filter(w =>
    w.name.toLowerCase().includes(search.toLowerCase())
  );


  return(

<section className="scene active">

<div className="scene-layout pool-layout">


{/* LEFT SIDE - STATS */}

<div>

<div className="dash-stats-grid">


<motion.div
className="dash-stat-card"
whileHover={{scale:1.05}}
>

<p className="dsc-label">
Pool Balance
</p>

<h3 className="dsc-value">
₹1,50,000
</h3>

<p className="muted">
community protection fund
</p>

</motion.div>



<motion.div
className="dash-stat-card"
whileHover={{scale:1.05}}
>

<p className="dsc-label">
Workers
</p>

<h3 className="dsc-value">
14,250
</h3>

</motion.div>



<motion.div
className="dash-stat-card"
whileHover={{scale:1.05}}
>

<p className="dsc-label">
Trust Score
</p>

<h3 className="green-text">
97%
</h3>

<p className="muted">
AI verified
</p>

</motion.div>



<motion.div
className="dash-stat-card"
whileHover={{scale:1.05}}
>

<p className="dsc-label">
Total Payout
</p>

<h3 className="dsc-value">
₹32,000
</h3>

</motion.div>


</div>

</div>



{/* RIGHT SIDE */}

<div>


{/* GRAPH */}

<motion.div
className="dashboard-panel"
initial={{opacity:0}}
animate={{opacity:1}}
>

<h3 className="dp-title">
Contribution vs Payout Trend
</h3>


<ResponsiveContainer width="100%" height={260}>

<BarChart data={payoutTrend}>

<CartesianGrid stroke="#e5e7eb"/>

<XAxis dataKey="month"/>

<YAxis/>

<Tooltip/>


<Bar
dataKey="contribution"
fill="#22c55e"
radius={[6,6,0,0]}
/>


<Bar
dataKey="payout"
fill="#ef4444"
radius={[6,6,0,0]}
/>


</BarChart>

</ResponsiveContainer>


<p className="df-label">
Pool remains stable with balanced contribution ratio.
</p>

</motion.div>



{/* SEARCH */}

<div className="search-box">

<input

placeholder="search worker..."

value={search}

onChange={(e)=>setSearch(e.target.value)}

/>

</div>



{/* MEMBER LIST */}

<motion.div
className="dashboard-panel"
initial={{opacity:0}}
animate={{opacity:1}}
>

<h3 className="dp-title">
Community Members
</h3>



<div className="pool-list">


{filteredWorkers.map(w=>(


<motion.div
key={w.name}
className="worker-card"
whileHover={{scale:1.02}}
>


<div>

<h3>
{w.name}
</h3>

<p className="muted">
{w.city}
</p>

</div>



<div className="contribution">

+₹{w.contribution}

</div>



<div>

{w.payout>0 ?

<span className="paid">

₹{w.payout} paid

</span>

:

<span className="safe">

Protected

</span>

}

</div>


</motion.div>


))}


</div>



<div className="dp-footer-row">

<div className="dp-footer-stat">

<span className="df-label">

AI Pool Logic

</span>

<span className="df-val">

Workers contribute small weekly premium.
AI detects disruption and releases payout instantly.

</span>

</div>

</div>



</motion.div>


</div>


</div>

</section>

)

}

export default PoolDetails;
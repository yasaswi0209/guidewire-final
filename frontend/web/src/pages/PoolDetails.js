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

{ name:"Ravi", city:"Hyderabad", area:"Nampally", contribution:30, payout:0 },

{ name:"Amit", city:"Hyderabad", area:"Ameerpet", contribution:20, payout:310 },

{ name:"Priya", city:"Hyderabad", area:"Kukatpally", contribution:50, payout:0 },

{ name:"Rahul", city:"Hyderabad", area:"Dilsukhnagar", contribution:30, payout:120 },

{ name:"Sneha", city:"Hyderabad", area:"Begumpet", contribution:40, payout:0 }

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

<div className="pool-container">


{/* COMMUNITY POOL INFO */}

<motion.div
className="dashboard-panel glass pool-info-card"
initial={{opacity:0}}
animate={{opacity:1}}
>

<h3 className="dp-title">

Community Pool – How it works

</h3>


<p className="muted">

The Community Pool is formed by gig workers located in the same nearby area or city.

People working in similar locations often face common risks such as rain, heat,
pollution, or low demand.

Each member contributes a small weekly premium into a shared fund.
When disruption affects workers in that location, payouts are released
from the same community pool.

This creates fair contribution, faster support, and stronger protection
for workers in your area.

</p>

</motion.div>



{/* TOP SECTION */}

<div className="pool-top">


{/* STATS */}

<div className="dash-stats-grid">

<motion.div
className="dash-stat-card glass"
whileHover={{scale:1.05}}
>

<p className="dsc-label">
Pool Balance
</p>

<h3 className="highlight-green">
₹1,50,000
</h3>

<p className="muted">
community protection fund
</p>

</motion.div>



<motion.div
className="dash-stat-card glass"
whileHover={{scale:1.05}}
>

<p className="dsc-label">
Workers
</p>

<h3>
14,250
</h3>

<p className="muted">
active members
</p>

</motion.div>



<motion.div
className="dash-stat-card glass"
whileHover={{scale:1.05}}
>

<p className="dsc-label">
Trust Score
</p>

<h3 className="highlight-green">
97%
</h3>

<p className="muted">
AI verified pool
</p>

</motion.div>



<motion.div
className="dash-stat-card glass"
whileHover={{scale:1.05}}
>

<p className="dsc-label">
Total Payout
</p>

<h3 className="highlight-red">
₹32,000
</h3>

<p className="muted">
released instantly
</p>

</motion.div>

</div>



{/* GRAPH */}

<motion.div
className="dashboard-panel glass graph-panel"
initial={{opacity:0}}
animate={{opacity:1}}
>

<h3 className="dp-title">

Contribution vs Payout Trend

</h3>


<ResponsiveContainer width="100%" height={320}>

<BarChart data={payoutTrend}>

<CartesianGrid strokeDasharray="3 3"/>

<XAxis dataKey="month"/>

<YAxis/>

<Tooltip/>


<defs>

<linearGradient id="greenGradient">

<stop offset="0%" stopColor="#22c55e"/>

<stop offset="100%" stopColor="#4ade80"/>

</linearGradient>


<linearGradient id="redGradient">

<stop offset="0%" stopColor="#ef4444"/>

<stop offset="100%" stopColor="#f87171"/>

</linearGradient>

</defs>


<Bar
dataKey="contribution"
fill="url(#greenGradient)"
radius={[8,8,0,0]}
/>


<Bar
dataKey="payout"
fill="url(#redGradient)"
radius={[8,8,0,0]}
/>


</BarChart>

</ResponsiveContainer>


<p className="muted">

Balanced contribution keeps the protection pool stable.

</p>

</motion.div>

</div>




{/* MEMBERS */}

<motion.div
className="dashboard-panel glass members-panel"
initial={{opacity:0}}
animate={{opacity:1}}
>

<div className="member-header">

<h3 className="dp-title">

Community Members

</h3>


<input
className="modern-search"
placeholder="🔍 search worker..."
value={search}
onChange={(e)=>setSearch(e.target.value)}
/>

</div>



<div className="pool-list">

{/* HEADER ROW */}

<div className="worker-card header-row grid-worker">

<div>Name</div>

<div>Area</div>

<div>Contribution</div>

<div>Status</div>

</div>



{filteredWorkers.map(w=>(

<motion.div
key={w.name}
className="worker-card modern-card grid-worker"
whileHover={{scale:1.02}}
>

{/* NAME */}

<div>

<h3>{w.name}</h3>

<p className="muted">{w.city}</p>

</div>


{/* AREA COLUMN */}

<div className="area-badge">

📍 {w.area}

</div>


{/* CONTRIBUTION */}

<div className="contribution">

+₹{w.contribution}

</div>


{/* STATUS */}

<div>

{w.payout>0 ?

<span className="paid">

₹{w.payout}

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


</motion.div>



</div>

</section>

  )

}

export default PoolDetails;
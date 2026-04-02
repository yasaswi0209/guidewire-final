import { useNavigate } from "react-router-dom";

function Home(){

const navigate = useNavigate();

return(

<section className="scene active">

<div className="scene-layout scene-0-layout">


{/* LEFT CONTENT */}

<div>

<p className="scene-label">

FOR GIG WORKERS

</p>



<h1 className="scene-headline">

Protect Your
<span className="headline-accent">

 Daily Income

</span>

</h1>



<p className="scene-sub">

AI-powered insurance for real-world delivery work.
Instant protection against rain, heat, pollution & demand drops.

</p>



<div className="scene-actions">

<button
className="btn-primary"
onClick={()=>navigate("/policy")}
>

Get Protected — ₹20/week

</button>


<button
className="btn-ghost"
onClick={()=>navigate("/dashboard")}
>

See Dashboard

</button>

</div>



{/* TRUST */}

<div className="trust-badges">

<div className="trust-badge">

<span className="badge-num">

2.4L+

</span>

<span className="badge-label">

Workers Protected

</span>

</div>


<div className="trust-divider"></div>


<div className="trust-badge">

<span className="badge-num">

₹18Cr+

</span>

<span className="badge-label">

Claims Paid

</span>

</div>


<div className="trust-divider"></div>


<div className="trust-badge">

<span className="badge-num">

99.1%

</span>

<span className="badge-label">

AI Accuracy

</span>

</div>

</div>



{/* FEATURES */}

<div className="mini-features">


<div className="mini-feature">

🌧 Weather protection

</div>


<div className="mini-feature">

🤖 AI fraud detection

</div>


<div className="mini-feature">

⚡ instant UPI payout

</div>


</div>



</div>



{/* RIGHT IMAGE */}

<div className="rider-illustration">

<img
src="https://cdn-icons-png.flaticon.com/512/2972/2972185.png"
width="340"
alt="delivery bike"
/>

</div>



</div>

</section>

);

}

export default Home;
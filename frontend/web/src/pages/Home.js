import { useNavigate } from "react-router-dom";
import deliveryImg from "../assets/delivery.png";
function Home(){

const navigate = useNavigate();

return(

<section className="scene active">

<div className="scene-layout scene-0-layout">

{/* LEFT */}

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



{/* FEATURES */}

<div className="mini-features">

<div className="mini-feature blue-pill">
🌧 Weather protection
</div>

<div className="mini-feature orange-pill">
🤖 AI fraud detection
</div>

<div className="mini-feature green-pill">
⚡️ instant UPI payout
</div>

</div>



{/* HOW IT WORKS */}

<div className="mini-features more-features">

<div className="mini-feature blue-pill">
📍 Detect risk
</div>

<div className="mini-feature orange-pill">
🤖 Predict impact
</div>

<div className="mini-feature green-pill">
💰 Instant payout
</div>

<div className="mini-feature grey-pill">
🛡 Stay protected
</div>

</div>


</div>



{/* RIGHT IMAGE */}

<div className="rider-illustration">

<img src={deliveryImg} alt="Delivery Workers" className="home-img" />

</div>

</div>

</section>

);

}

export default Home;
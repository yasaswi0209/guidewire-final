import { motion } from "framer-motion";

function Settings(){

function toggleDark(){

document.body.classList.toggle("dark");

localStorage.setItem(
"theme",
document.body.classList.contains("dark")
? "dark"
: "light"
);

}

return(

<section className="scene active">

<div className="scene-layout">

<div className="settings-header">

<h2>⚙️ Settings</h2>

<p className="muted">
Manage preferences & customize your experience
</p>

</div>



<div className="settings-grid">


{/* THEME */}

<motion.div
className="settings-card theme-card"
initial={{opacity:0,y:20}}
animate={{opacity:1,y:0}}
>

<div className="card-title">
🌙 Theme
</div>

<p className="muted">
Switch between light and dark appearance
</p>

<button
className="btn-primary"
onClick={toggleDark}
>

Toggle Dark Mode

</button>

</motion.div>



{/* NOTIFICATIONS */}

<motion.div
className="settings-card notify-card"
initial={{opacity:0,y:20}}
animate={{opacity:1,y:0}}
>

<div className="card-title">
🔔 Notifications
</div>

<label className="switch-row">
<input type="checkbox" defaultChecked/>
 Risk alerts
</label>

<label className="switch-row">
<input type="checkbox" defaultChecked/>
 Weekly report
</label>

<label className="switch-row">
<input type="checkbox"/>
 Offers & updates
</label>

</motion.div>



{/* SECURITY */}

<motion.div
className="settings-card security-card"
initial={{opacity:0,y:20}}
animate={{opacity:1,y:0}}
>

<div className="card-title">
🔒 Security
</div>

<button className="btn-ghost">
Change password
</button>

<button className="btn-ghost">
Enable 2FA
</button>

</motion.div>



{/* SUPPORT */}

<motion.div
className="settings-card support-card"
initial={{opacity:0,y:20}}
animate={{opacity:1,y:0}}
>

<div className="card-title">
💬 Support
</div>

<p>Email: support@gigshield.ai</p>

<p>Phone: +91 9876543210</p>

<button className="btn-ghost">
Contact support
</button>

</motion.div>



{/* APP INFO */}

<motion.div
className="settings-card info-card"
initial={{opacity:0,y:20}}
animate={{opacity:1,y:0}}
>

<div className="card-title">
📊 App Info
</div>

<p>Version 1.0</p>

<p className="muted">
AI powered income protection
</p>

</motion.div>



</div>

</div>

</section>

);

}

export default Settings;
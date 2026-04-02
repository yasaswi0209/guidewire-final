import { NavLink, useNavigate } from "react-router-dom";

function Navbar(){

const navigate = useNavigate();

let user = null;

try {
  user = JSON.parse(localStorage.getItem("user"));
} catch (err) {
  user = null;
}


function logout(){

localStorage.removeItem("user");

navigate("/");

}


return(

<header id="main-nav">

<div className="nav-inner">


{/* LOGO */}

<div
className="nav-logo"
onClick={()=>navigate("/")}
>

<span className="logo-text">

GeekShield <span className="logo-ai">AI</span>

</span>

</div>



{/* LINKS */}

<nav>

<ul className="nav-links">


<li>

<NavLink
to="/"
className={({isActive})=>
isActive ? "nav-link active" : "nav-link"
}
>

Home

</NavLink>

</li>



<li>

<NavLink
to="/dashboard"
className={({isActive})=>
isActive ? "nav-link active" : "nav-link"
}
>

Dashboard

</NavLink>

</li>



<li>

<NavLink
to="/policy"
className={({isActive})=>
isActive ? "nav-link active" : "nav-link"
}
>

Policy

</NavLink>

</li>



<li>

<NavLink
to="/claims"
className={({isActive})=>
isActive ? "nav-link active" : "nav-link"
}
>

Claims

</NavLink>

</li>



<li>

<NavLink
to="/risk"
className={({isActive})=>
isActive ? "nav-link active" : "nav-link"
}
>

Risk Analysis

</NavLink>

</li>


</ul>

</nav>



{/* RIGHT SIDE */}

<div className="nav-actions">


{/* show user email */}

{user && (

<span className="nav-user">

👤 {user.name}

</span>

)}



{/* login / logout */}

{user ?

<button
className="nav-cta"
onClick={logout}
>

Logout

</button>

:

<button
className="nav-cta"
onClick={()=>navigate("/login")}
>

Login

</button>

}


</div>



</div>

</header>

);

}

export default Navbar;
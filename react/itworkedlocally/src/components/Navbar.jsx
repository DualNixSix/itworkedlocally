import {useState} from "react"
import {Link} from "react-router-dom"
import {apiFetch,BASE} from "../api"

export default function Navbar(){

const [username,setUsername] = useState("")
const [password,setPassword] = useState("")
const [status,setStatus] = useState("")

const token = localStorage.getItem("token")

const handleLogin = async ()=>{

try{

const data = await apiFetch(`${BASE}/api/v1/accounts/token/`,{
method:"POST",
headers:{ "Content-Type":"application/json"},
body:JSON.stringify({username,password})
})

localStorage.setItem("token",data.token)
localStorage.setItem("username",username)

location.reload()

}catch(err){
setStatus(err.message)
}

}

const handleSignup = async ()=>{

try{

await apiFetch(`${BASE}/api/v1/accounts/signup/`,{
method:"POST",
headers:{ "Content-Type":"application/json"},
body:JSON.stringify({username,password})
})

handleLogin()

}catch{
setStatus("Invalid username or password.")
}

}

const handleLogout = ()=>{
localStorage.removeItem("token")
localStorage.removeItem("username")
location.reload()
}

return(

<header className="navbar">

<div className="nav-left">
<img src="/favicon.ico" className="logo"/>
<Link to="/" className="brand">IT Worked Locally</Link>
</div>

<nav className="nav-center">
<Link to="/">Home</Link>
{token && <Link to="/create">Create Thread</Link>}
</nav>

<div className="nav-right">

<div className="auth-controls">

{!token && (
<>
<input
placeholder="Username"
value={username}
onChange={e=>setUsername(e.target.value)}
/>

<input
type="password"
placeholder="Password"
value={password}
onChange={e=>setPassword(e.target.value)}
/>

<button onClick={handleSignup}>Signup</button>
<button onClick={handleLogin}>Login</button>
</>
)}

{token && (
<button onClick={handleLogout}>Logout</button>
)}

</div>

<p id="auth-status">{status}</p>

</div>

</header>

)

}
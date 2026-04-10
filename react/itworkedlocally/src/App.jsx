import {Outlet} from "react-router-dom"
import Navbar from "./components/Navbar"
import RandomFooter from "./components/RandomFooter"

export default function App(){

return(
<>
<Navbar/>

<main className="container">
<Outlet/>
</main>

<div className="container">
<RandomFooter/>
</div>
</>
)
}
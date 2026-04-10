import React from "react"
import ReactDOM from "react-dom/client"

import "./index.css"

import {
createBrowserRouter,
RouterProvider
} from "react-router-dom"

import App from "./App"
import Home from "./pages/Home"
import Create from "./pages/Create"
import Edit from "./pages/Edit"
import Post from "./pages/Post"

const router = createBrowserRouter([
{
path:"/",
element:<App/>,
children:[
{ path:"/", element:<Home/> },
{ path:"/create", element:<Create/> },
{ path:"/edit/:id", element:<Edit/> },
{ path:"/post/:id", element:<Post/> }
]
}
])

ReactDOM.createRoot(document.getElementById("root")).render(
<RouterProvider router={router}/>
)
import {useState,useEffect} from "react"
import {useNavigate} from "react-router-dom"
import {apiFetch,BASE} from "../api"

export default function Create(){

const navigate = useNavigate()

const [categories,setCategories] = useState([])
const [title,setTitle] = useState("")
const [repo,setRepo] = useState("")
const [body,setBody] = useState("")
const [category,setCategory] = useState(null)

useEffect(()=>{

const load = async ()=>{

const data = await apiFetch(`${BASE}/api/v1/categories/`)
setCategories(data)

if(data.length > 0){
setCategory(data[0].id)
}

}

load()

},[])

const handleSubmit = async (e)=>{

e.preventDefault()

const created = await apiFetch(`${BASE}/api/v1/posts/`,{
method:"POST",
headers:{ "Content-Type":"application/json"},
body:JSON.stringify({
category,
title,
body,
repo_url:repo
})
})

navigate(`/post/${created.id}`)
}

return(

<section>

<h2>Create Thread</h2>

<form onSubmit={handleSubmit}>

<select
value={category || ""}
onChange={e => setCategory(Number(e.target.value))}
required
>

{categories.map(c=>(
<option key={c.id} value={c.id}>
{c.name}
</option>
))}

</select>

<input
placeholder="Title"
value={title}
onChange={e=>setTitle(e.target.value)}
/>

<input
placeholder="Repo URL"
value={repo}
onChange={e=>setRepo(e.target.value)}
/>

<textarea
placeholder="Body"
value={body}
onChange={e=>setBody(e.target.value)}
/>

<button>Post Thread</button>

</form>

</section>

)

}
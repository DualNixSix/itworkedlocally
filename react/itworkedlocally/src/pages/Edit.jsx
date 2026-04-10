import {useEffect,useState} from "react"
import {useParams,useNavigate} from "react-router-dom"
import {apiFetch,BASE} from "../api"

export default function Edit(){

const {id} = useParams()
const navigate = useNavigate()

const [post,setPost] = useState(null)
const [title,setTitle] = useState("")
const [body,setBody] = useState("")
const [repo,setRepo] = useState("")

useEffect(()=>{

const load = async ()=>{

const data = await apiFetch(`${BASE}/api/v1/posts/${id}/`)

setPost(data)
setTitle(data.title)
setBody(data.body)
setRepo(data.repo_url || "")

}

load()

},[id])

const submit = async (e)=>{

e.preventDefault()

await apiFetch(`${BASE}/api/v1/posts/${id}/`,{
method:"PUT",
headers:{ "Content-Type":"application/json"},
body:JSON.stringify({
category:post.category,
title,
body,
repo_url:repo
})
})

navigate(`/post/${id}`)

}

if(!post){
return <section>Loading...</section>
}

return(

<section>

<h2>Edit Thread</h2>

<form onSubmit={submit}>

<input
value={title}
onChange={e=>setTitle(e.target.value)}
required
/>

<input
placeholder="Repo URL"
value={repo}
onChange={e=>setRepo(e.target.value)}
/>

<textarea
value={body}
onChange={e=>setBody(e.target.value)}
required
/>

<button>Save Changes</button>

</form>

</section>

)

}
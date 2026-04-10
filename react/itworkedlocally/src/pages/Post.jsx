import {useEffect,useState} from "react"
import {useParams,useNavigate} from "react-router-dom"
import {apiFetch,BASE} from "../api"

export default function Post(){

const {id} = useParams()
const navigate = useNavigate()

const [post,setPost] = useState(null)
const [comment,setComment] = useState("")

const token = localStorage.getItem("token")
const currentUser = localStorage.getItem("username")

useEffect(()=>{

const load = async ()=>{

const data = await apiFetch(`${BASE}/api/v1/posts/${id}/`)
setPost(data)

}

load()

},[id])

const submitComment = async (e)=>{

e.preventDefault()

await apiFetch(`${BASE}/api/v1/posts/${id}/comments/`,{
method:"POST",
headers:{ "Content-Type":"application/json"},
body:JSON.stringify({body:comment})
})

setComment("")

const data = await apiFetch(`${BASE}/api/v1/posts/${id}/`)
setPost(data)

}

const deletePost = async ()=>{

if(!confirm("Delete this post?")) return

await apiFetch(`${BASE}/api/v1/posts/${id}/`,{
method:"DELETE"
})

navigate("/")

}

if(!post){
return <section>Loading...</section>
}

return(

<section id="post-detail">

<div className="post-header-row">

<h2>{post.title}</h2>

{token && currentUser === post.author_username && (

<div className="post-controls">

<button onClick={()=>navigate(`/edit/${post.id}`)}>
Edit
</button>

<button onClick={deletePost}>
Delete
</button>

</div>

)}

</div>

<p className="post-body">{post.body}</p>

{/* repository metadata */}
{post.repo_metadata && (

<div className="repo-box">

<strong>Repository:</strong> {post.repo_metadata.repo_name}
<br/>

Stars: {post.repo_metadata.stars}
<br/>

Open Issues: {post.repo_metadata.open_issues}
<br/>

Last Updated: {post.repo_metadata.last_updated}

{post.repo_url && (
<a
href={post.repo_url}
target="_blank"
style={{display:"block",marginTop:"6px"}}
>
Open Repository
</a>
)}

</div>

)}

{/* stackoverflow results */}
{post.related_stackoverflow && (

<div className="stack-box">

<strong>Related StackOverflow:</strong>
<br/>

{post.related_stackoverflow.map(item=>(
<div key={item.link}>
<a href={item.link} target="_blank">
{item.title} (Score: {item.score})
</a>
</div>
))}

</div>

)}

{/* comments */}
<div className="comments-box">

<h3>Comments</h3>

{post.comments.length === 0 && <p>No comments yet.</p>}

{post.comments.map(c=>(
<div key={c.id} className="comment-item">

<strong>{c.author_username}</strong>
<p>{c.body}</p>

</div>
))}

</div>

{/* comment form */}
{token && (

<form onSubmit={submitComment}>

<textarea
placeholder="Write a comment..."
required
value={comment}
onChange={e=>setComment(e.target.value)}
/>

<button>Add Comment</button>

</form>

)}

</section>

)

}
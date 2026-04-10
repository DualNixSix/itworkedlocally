import {useEffect,useState} from "react"
import {Link} from "react-router-dom"
import {apiFetch,BASE} from "../api"

export default function Home(){

const [posts,setPosts] = useState([])

useEffect(()=>{

const load = async ()=>{

const data = await apiFetch(`${BASE}/api/v1/posts/`)
setPosts(data)

}

load()

},[])

return(

<section>

<h2>Threads</h2>

<div id="posts-list">

{posts.map(post=>(
<div key={post.id} className="post-card">

<Link to={`/post/${post.id}`}>
[{post.category_name}] {post.title}
</Link>

</div>
))}

</div>

</section>

)

}
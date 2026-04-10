import { useEffect, useState } from "react"

// authors used for random quote API selection
const QUOTE_AUTHORS = [
"Elon Musk",
"Steve Jobs",
"Jeff Bezos",
"Larry Page",
"Thomas Edison",
"Nikola Tesla",
"Henry Ford",
"Warren Buffett",
"Peter Drucker",
"Napoleon Hill",
"Jim Rohn",
"Sun Tzu",
"Marcus Aurelius",
"Seneca the Younger",
"Paul Graham",
"Jason Fried",
"Sheryl Sandberg",
"Jack Welch",
"Thomas J. Watson",
"Stephen Hawking",
"Isaac Asimov",
"Arthur C. Clarke",
"Buckminster Fuller",
"Edward de Bono",
"Clay Shirky",
"Howard H. Aiken",
"Hal Abelson",
"Vernor Vinge",
"Cory Doctorow",
"Robert Kiyosaki",
"Tony Robbins",
"Zig Ziglar"
]

// retrieve random programming joke
const fetchRandomJoke = async () => {

const response = await fetch(
"https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
)

const data = await response.json()

if (data.setup && data.delivery) {
return `${data.setup} ${data.delivery}`
}

return data.joke

}

// retrieve random quote
const fetchRandomQuote = async () => {

const randomAuthor =
QUOTE_AUTHORS[Math.floor(Math.random() * QUOTE_AUTHORS.length)]

const response = await fetch(
`https://quoteslate.vercel.app/api/quotes/random?authors=${encodeURIComponent(randomAuthor)}`
)

const data = await response.json()

if (data.quote && data.author) {
return `${data.quote} — ${data.author}`
}

return "Quote unavailable."

}

// render footer quote or joke content
export default function RandomFooter(){

const [content,setContent] = useState("Loading inspiration...")

// load random content when component renders
useEffect(()=>{

const load = async ()=>{

const roll = Math.random()

try{

let result

if(roll < 0.75){
result = await fetchRandomQuote()
}
else{
result = await fetchRandomJoke()
}

setContent(result)

}catch{
setContent("Unable to load content.")
}

}

load()

},[])

return (
<div id="random-footer" className="post-card random-card">
{content}
</div>
)

}
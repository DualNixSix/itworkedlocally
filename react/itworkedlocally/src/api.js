// base URL derived from current origin
const BASE_URL = window.location.protocol + "//" + window.location.host;

// perform API request with optional token authentication
export const apiFetch = async (url, options = {}) => {

const token = localStorage.getItem("token");

if(token){
options.headers = {
...options.headers,
Authorization:`Token ${token}`
}
}

const response = await fetch(url,options)

const isJson = response.headers
.get("content-type")
?.includes("application/json")

const body = isJson ? await response.json() : null

if(!response.ok){

let msg="Request failed"

if(body){

if(body.detail){
msg = body.detail
}

else if(body.non_field_errors){
msg = body.non_field_errors[0]
}

else{
const firstKey = Object.keys(body)[0]

if(firstKey && Array.isArray(body[firstKey])){
msg = body[firstKey][0]
}

}

}

throw new Error(msg)
}

return body
}

export const BASE = BASE_URL
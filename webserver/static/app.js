// base URL derived from current origin
const BASE_URL = window.location.protocol + "//" + window.location.host;

// perform API request with optional token authentication  
const apiFetch = async (url, options = {}) => {
    const token = localStorage.getItem("token");

    if (token) {
        options.headers = {
            ...options.headers,
            "Authorization": `Token ${token}`
        };
    }

    const response = await fetch(url, options);

    const isJson = response.headers
        .get("content-type")
        ?.includes("application/json");

    const body = isJson ? await response.json() : null;

    if (!response.ok) {
        let msg = "Request failed";

        if (body) {
            if (body.detail) {
                msg = body.detail;
            } 
            else if (body.non_field_errors) {
                msg = body.non_field_errors[0];
            } 
            else {
                // Handle DRF field validation errors
                const firstKey = Object.keys(body)[0];
                if (firstKey && Array.isArray(body[firstKey])) {
                    msg = body[firstKey][0];
                }
            }
        }

        throw new Error(msg);
    }

    return body;
};

// update authentication status display 
const setAuthStatus = (text) => {
    const el = document.getElementById("auth-status");
    if (!el) return;
    el.innerHTML = text;
};

// toggle authentication buttons based on login state 
const updateAuthUI = () => {
    const token = localStorage.getItem("token");

    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password");
    const signupBtn = document.getElementById("signup-btn");
    const loginBtn = document.getElementById("login-btn");
    const logoutBtn = document.getElementById("logout-btn");
    const createLink = document.getElementById("create-link");

    if (!usernameInput || !passwordInput || !signupBtn || !loginBtn || !logoutBtn) return;

    if (token) {
        usernameInput.style.display = "none";
        passwordInput.style.display = "none";
        signupBtn.style.display = "none";
        loginBtn.style.display = "none";
        logoutBtn.style.display = "inline-block";
        if (createLink) createLink.style.display = "inline-block";
    } else {
        usernameInput.style.display = "inline-block";
        passwordInput.style.display = "inline-block";
        signupBtn.style.display = "inline-block";
        loginBtn.style.display = "inline-block";
        logoutBtn.style.display = "none";
        if (createLink) createLink.style.display = "none";
    }

};

// retrieve username and password from input fields 
const getCredentials = () => {
    return {
        username: document.getElementById("username")?.value.trim(),
        password: document.getElementById("password")?.value
    };
};

// register new user and automatically authenticate
const handleSignup = async () => {
    const { username, password } = getCredentials();

    if (!username || !password) {
    setAuthStatus("Username and password required.");
    return;
    }

    try {
        // Create account
        await apiFetch(`${BASE_URL}/api/v1/accounts/signup/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });

        // Auto-login immediately after signup
        const data = await apiFetch(`${BASE_URL}/api/v1/accounts/token/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });

        localStorage.setItem("token", data.token);
        localStorage.setItem("username", username);

        updateAuthUI();
        setAuthStatus("Account created.<br>Logged in.");
    } 
    catch (err) {
        setAuthStatus("Invalid username or password.");
    }
};

// authenticate user and store token 
const handleLogin = async () => {
    const { username, password } = getCredentials();

    if (!username || !password) {
    setAuthStatus("Username and password required.");
    return;
    }

    try {
        const data = await apiFetch(`${BASE_URL}/api/v1/accounts/token/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });

        localStorage.setItem("token", data.token);
        localStorage.setItem("username", username);

        updateAuthUI();
        setAuthStatus("Logged in.");
    } 
    catch (err) {
        setAuthStatus(err.message);
    }
};

// remove authentication token 
const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("username");
    updateAuthUI();
    setAuthStatus("Logged out.");
};

// load all posts and render clickable list 
const loadPosts = async () => {
    const container = document.getElementById("posts-list");
    if (!container) return;

    container.innerHTML = "";

    const posts = await apiFetch(`${BASE_URL}/api/v1/posts/`);

    posts.forEach(post => {
        const div = document.createElement("div");
        div.className = "post-card";
        div.innerText = `[${post.category_name}] ${post.title}`;
        div.addEventListener("click", () => {
            window.location.href = `/post/${post.id}`;
        });
        container.appendChild(div);
    });
};

// load categories into select dropdown 
const loadCategories = async () => {
    const select = document.getElementById("post-category");
    if (!select) return;

    select.innerHTML = "";

    const categories = await apiFetch(`${BASE_URL}/api/v1/categories/`);

    categories.forEach(cat => {
        const option = document.createElement("option");
        option.value = cat.id;
        option.innerText = cat.name;
        select.appendChild(option);
    });
};

// submit new thread and redirect to detail view 
const handleCreatePost = async (e) => {
    e.preventDefault();

    const category = Number(document.getElementById("post-category").value);
    const title = document.getElementById("post-title").value.trim();
    const repo_url = document.getElementById("post-repo").value.trim();
    const body = document.getElementById("post-body").value;

    const created = await apiFetch(`${BASE_URL}/api/v1/posts/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ category, title, body, repo_url })
    });

    window.location.href = `/post/${created.id}`;
};

// render comments under a thread 
const renderComments = (comments, container) => {
    const wrap = document.createElement("div");
    wrap.className = "comments-box";
    const header = document.createElement("h3");
    header.innerText = "Comments";
    wrap.appendChild(header);

    if (!comments || comments.length === 0) {
        const empty = document.createElement("p");
        empty.innerText = "No comments yet.";
        wrap.appendChild(empty);
        container.appendChild(wrap);
        return;
    }

    comments.forEach(c => {
        const item = document.createElement("div");
        item.className = "comment-item";

        const author = document.createElement("strong");
        author.innerText = c.author_username;

        const body = document.createElement("p");
        body.innerText = c.body;

        item.appendChild(author);
        item.appendChild(body);
        wrap.appendChild(item);
    });

    container.appendChild(wrap);
};

// render comment submission form 
const renderCommentForm = (postId, container) => {
    const token = localStorage.getItem("token");
    if (!token) return;

    const form = document.createElement("form");
    const textarea = document.createElement("textarea");
    textarea.placeholder = "Write a comment...";
    textarea.required = true;

    const btn = document.createElement("button");
    btn.type = "submit";
    btn.innerText = "Add Comment";

    form.appendChild(textarea);
    form.appendChild(btn);
    container.appendChild(form);

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        await apiFetch(`${BASE_URL}/api/v1/posts/${postId}/comments/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ body: textarea.value })
        });

        loadPostDetail();
    });
};

// render edit and delete controls for post owner 
const renderPostControls = (post, container) => {
    const currentUser = localStorage.getItem("username");
    const token = localStorage.getItem("token");

    if (!token) return;
    if (currentUser !== post.author_username) return;

    const controls = document.createElement("div");
    controls.className = "post-controls";

    const editBtn = document.createElement("button");
    editBtn.innerText = "Edit";
    editBtn.addEventListener("click", () => {
        window.location.href = `/edit/${post.id}`;
    });

    const deleteBtn = document.createElement("button");
    deleteBtn.innerText = "Delete";
    deleteBtn.addEventListener("click", async () => {
        if (!confirm("Delete this post?")) return;

        await apiFetch(`${BASE_URL}/api/v1/posts/${post.id}/`, {
            method: "DELETE"
        });

        window.location.href = "/";
    });

    controls.appendChild(editBtn);
    controls.appendChild(deleteBtn);
    const headerRow = container.querySelector(".post-header-row");
    if (headerRow) {
        headerRow.appendChild(controls);
    }
};

// load single thread including GitHub and StackOverflow metadata 
const loadPostDetail = async () => {
    const container = document.getElementById("post-detail");
    if (!container) return;

    container.innerHTML = "";

    const parts = window.location.pathname.split("/");
    const id = parts[2];
    if (!id) return;

    const post = await apiFetch(`${BASE_URL}/api/v1/posts/${id}/`);

    const headerRow = document.createElement("div");
    headerRow.className = "post-header-row";

    const title = document.createElement("h2");
    title.innerText = post.title;

    const body = document.createElement("p");
    body.innerText = post.body;

    headerRow.appendChild(title);

    container.appendChild(headerRow);
    container.appendChild(body);

    // render GitHub repository metadata 
    if (post.repo_metadata) {
        const repoBox = document.createElement("div");
        repoBox.className = "repo-box";

        repoBox.innerHTML = `
            <strong>Repository:</strong> ${post.repo_metadata.repo_name}<br>
            Stars: ${post.repo_metadata.stars}<br>
            Open Issues: ${post.repo_metadata.open_issues}<br>
            Last Updated: ${post.repo_metadata.last_updated}
        `;

        if (post.repo_url) {
            const link = document.createElement("a");
            link.href = post.repo_url;
            link.target = "_blank";
            link.innerText = "Open Repository";
            link.style.display = "block";    
            link.style.marginTop = "6px"; 
            repoBox.appendChild(link);
        }

        container.appendChild(repoBox);
    }

    // render related StackOverflow results 
    if (post.related_stackoverflow) {
        const stackBox = document.createElement("div");
        stackBox.className = "stack-box";
        stackBox.innerHTML = "<strong>Related StackOverflow:</strong><br>";

        post.related_stackoverflow.forEach(item => {
            const link = document.createElement("a");
            link.href = item.link;
            link.target = "_blank";
            link.innerText = `${item.title} (Score: ${item.score})`;
            stackBox.appendChild(link);
            stackBox.appendChild(document.createElement("br"));
        });

        container.appendChild(stackBox);
    }

    renderPostControls(post, container);
    renderComments(post.comments, container);
    renderCommentForm(post.id, container);
};

// load edit page data and submit updated thread 
const loadEditPage = async () => {
    const form = document.getElementById("edit-post-form");
    if (!form) return;

    const parts = window.location.pathname.split("/");
    const id = parts[2];
    if (!id) return;

    const post = await apiFetch(`${BASE_URL}/api/v1/posts/${id}/`);

    document.getElementById("edit-title").value = post.title;
    document.getElementById("edit-body").value = post.body;
    document.getElementById("edit-repo").value = post.repo_url || "";

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        await apiFetch(`${BASE_URL}/api/v1/posts/${id}/`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                category: post.category,
                title: document.getElementById("edit-title").value.trim(),
                body: document.getElementById("edit-body").value,
                repo_url: document.getElementById("edit-repo").value.trim()
            })
        });

        window.location.href = `/post/${id}`;
    });
};

// Authors for quotes
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
];

// retrieve random programming joke
const fetchRandomJoke = async () => {
    const response = await fetch(
        "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    );

    const data = await response.json();

    if (data.setup && data.delivery) {
        return `${data.setup} ${data.delivery}`;
    }

    return data.joke;
};

// retrieve random quote
const fetchRandomQuote = async () => {
    const randomAuthor =
        QUOTE_AUTHORS[Math.floor(Math.random() * QUOTE_AUTHORS.length)];

    const response = await fetch(
        `https://quoteslate.vercel.app/api/quotes/random?authors=${encodeURIComponent(randomAuthor)}`
    );

    const data = await response.json();

    if (data.quote && data.author) {
        return `${data.quote} — ${data.author}`;
    }

    return "Quote unavailable.";
};

// render footer content 
const loadRandomFooter = async () => {
    const footer = document.getElementById("random-footer");
    if (!footer) return;

    footer.innerText = "Loading inspiration...";

    const roll = Math.random();

    try {
        let content;

        if (roll < 0.75) {
            content = await fetchRandomQuote();
        } else {
            content = await fetchRandomJoke();
        }

        footer.innerText = content;
    } catch {
        footer.innerText = "Unable to load content.";
    }
};

// initialize page behavior 
window.onload = () => {

    // block create and edit pages if not authenticated
    const path = window.location.pathname;
    const token = localStorage.getItem("token");

    if (
        (path.startsWith("/create") || path.startsWith("/edit/")) &&
        !token
    ) {
        window.location.href = "/";
        return;  // stop execution
    }

    updateAuthUI();

    document.getElementById("signup-btn")?.addEventListener("click", handleSignup);
    document.getElementById("login-btn")?.addEventListener("click", handleLogin);
    document.getElementById("logout-btn")?.addEventListener("click", handleLogout);
    document.getElementById("create-post-form")?.addEventListener("submit", handleCreatePost);

    loadPosts();
    loadCategories();
    loadPostDetail();
    loadEditPage();
    loadRandomFooter();
};
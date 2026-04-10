import os
import requests
from dotenv import load_dotenv

# loads environment variables from .env file
load_dotenv()

STACK_SECRET_KEY = os.getenv("STACK_SECRET_KEY")
GITHUB_SECRET_KEY = os.getenv("GITHUB_SECRET_KEY")


# fetch repository metadata from GitHub API
def fetch_github_repo(repo_url):
    # expects repo_url like https://github.com/user/repo
    try:
        parts = repo_url.rstrip("/").split("/")
        owner = parts[-2]
        repo = parts[-1]

        endpoint = f"https://api.github.com/repos/{owner}/{repo}"

        headers = {
            "Authorization": f"Bearer {GITHUB_SECRET_KEY}"
        }

        response = requests.get(endpoint, headers=headers)
        data = response.json()

        return {
            "stars": data.get("stargazers_count"),
            "last_updated": data.get("updated_at"),
            "open_issues": data.get("open_issues_count"),
            "repo_name": data.get("full_name")
        }

    except Exception:
        return None


# search related Stack Overflow answers using title keywords
def fetch_stackoverflow_related(title):
    endpoint = "https://api.stackexchange.com/2.3/search/advanced"

    params = {
        "order": "desc",
        "sort": "relevance",
        "q": title,
        "site": "stackoverflow",
        "key": STACK_SECRET_KEY
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    results = []

    for item in data.get("items", [])[:5]:
        results.append({
            "title": item.get("title"),
            "link": item.get("link"),
            "score": item.get("score")
        })

    return results

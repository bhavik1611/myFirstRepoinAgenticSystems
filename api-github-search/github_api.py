import requests

def search_github_repos(query, sort, order, per_page):
    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": sort,
        "order": order,
        "per_page": per_page
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Search for repositories related to "python", sort by stars descending, limit to 5 results
    data = search_github_repos(query="python", sort="stars", order="desc", per_page=5)
    items = data.get("items", [])
    for repo in items:
        name = repo.get("full_name")
        stars = repo.get("stargazers_count")
        print(f"Repository: {name}")
        print(f"Stars: {stars}")
        print("-" * 30)

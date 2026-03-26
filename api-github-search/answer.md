# Answers to Conceptual Questions

**Q1: What is the role of query parameters in this request?**

Query parameters are key-value pairs that are appended to the URL to modify the API request and specify what kind of data you want to retrieve. In the case of the GitHub repositories search API (`https://api.github.com/search/repositories`), common query parameters include:

- `q`: The search keywords or criteria.
- `sort`: Field to sort results by (e.g., stars, forks).
- `order`: The order of results (ascending 'asc' or descending 'desc').
- `per_page`: Number of results per page.

These parameters let you filter, search, sort, and control the number of results returned by the API.

**Q2: Why do we use `response.json()` instead of `response.text`?**

- `response.json()` parses the body of the HTTP response as JSON and returns a corresponding Python data structure (usually a dictionary or list).
- `response.text` returns the raw response content as a string.

We use `response.json()` when we expect the API to return data in JSON format, which is typical for modern APIs. This allows for easier access to individual fields and values in the response without needing to manually parse the JSON string.
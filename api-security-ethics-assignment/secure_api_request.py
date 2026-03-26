import os
import requests

def main():
    # Retrieve API key securely from environment variable
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("API_KEY environment variable not set.")
        return

    url = "https://dummyjson.com/products"

    if not api_key:
        print("API_KEY environment variable not set.")
        return

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )
    except Exception as e:
        print(f"An error occurred during the request: {e}")
        return

    if response.status_code == 200:
        try:
            print(response.json())
        except Exception:
            print("Response is not valid JSON.")
    elif response.status_code == 429:
        print("Rate limit reached. Try again later.")
    else:
        print(f"Request failed. Status code: {response.status_code}")

if __name__ == "__main__":
    main()

# To run this script, use the following command in VS Code terminal:
# API_KEY=your_api_key python secure_api_request.py

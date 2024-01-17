import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "my-reddit-script"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            if 'data' in data:
                return data['data']['subscribers']
            else:
                print(f"Error: 'data' key not found in the response JSON.")
                return 0
        except Exception as e:
            print(f"Error parsing JSON: {e}")
            return 0
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
        return 0
    else:
        print(f"Error: {response.status_code}")
        print(f"Response content: {response.text}")
        return 0

import requests

# Configuration
SERVER_URL = "http://127.0.0.1:5000/flag"  # Replace with your server's URL

def fetch_flag():
    """
    Fetch the flag from the server.
    """
    try:
        response = requests.get(SERVER_URL)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        print(f"Error fetching flag: {e}")
        return None

if __name__ == "__main__":
    # Fetch the flag
    flag = fetch_flag()
    if flag:
        print(f"Fetched flag: {flag}")
    else:
        print("Failed to fetch the flag.")

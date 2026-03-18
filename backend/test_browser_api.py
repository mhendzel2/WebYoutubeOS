import requests
import time

BASE_URL = "http://localhost:8001"

def test_browser_api():
    print(f"Testing Custom Browser API at {BASE_URL}...")
    
    # Wait for the API to come online up to 30 seconds
    server_online = False
    for i in range(30):
        try:
            res = requests.get(f"{BASE_URL}/status")
            if res.status_code == 200:
                print("Browser API is online!")
                server_online = True
                break
        except requests.exceptions.ConnectionError:
            print(f"Waiting for server... ({i+1}/30)")
            time.sleep(1)
            
    if not server_online:
        print("Failed to connect to Browser API. Make sure start.bat is running.")
        return
        
    print("\nAttempting to navigate to Google Slides...")
    res = requests.post(f"{BASE_URL}/navigate", json={"url": "https://docs.google.com/presentation/u/0/"})
    print(res.json())
    time.sleep(3)
    
    print("\nAttempting to open NotebookLM in the same page context...")
    res = requests.post(f"{BASE_URL}/navigate", json={"url": "https://notebooklm.google.com/"})
    print(res.json())
    time.sleep(2)
    
    print("\nFetching page status...")
    status_res = requests.get(f"{BASE_URL}/status")
    print("Current Browser Status:", status_res.json())
    
    print("\nCustom API test complete!")

if __name__ == "__main__":
    test_browser_api()

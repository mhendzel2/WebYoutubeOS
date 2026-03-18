import requests
from typing import Optional, Dict, Any

class BrowserToolkit:
    """Helper class for interacting with the local AI Browser API on port 8001."""
    
    def __init__(self, base_url: str = "http://localhost:8001"):
        self.base_url = base_url
        
    def check_status(self) -> Dict[str, Any]:
        """Check if the browser API is online and return the current status/URL."""
        try:
            res = requests.get(f"{self.base_url}/status", timeout=5)
            return res.json()
        except requests.exceptions.RequestException as e:
            return {"status": "offline", "error": str(e)}
            
    def navigate(self, url: str) -> Dict[str, Any]:
        """Navigate the browser to a specific URL."""
        res = requests.post(f"{self.base_url}/navigate", json={"url": url})
        return res.json()
        
    def type_text(self, element_id: int, text: str) -> Dict[str, Any]:
        """Type text into an element identified by its visual tag ID."""
        res = requests.post(f"{self.base_url}/type", json={"element_id": element_id, "text": text})
        return res.json()
        
    def click_element(self, element_id: int) -> Dict[str, Any]:
        """Click an element identified by its visual tag ID."""
        res = requests.post(f"{self.base_url}/click", json={"element_id": element_id})
        return res.json()
        
    def get_markdown(self) -> str:
        """Extract the current page's content as Markdown."""
        res = requests.get(f"{self.base_url}/markdown")
        data = res.json()
        if data.get("status") == "success":
            return data.get("markdown", "")
        return f"Error: {data.get('error', 'Unknown Error')}"
        
    def get_screenshot(self) -> str:
        """Get the current page screenshot as a base64 string."""
        res = requests.get(f"{self.base_url}/screenshot")
        data = res.json()
        if data.get("status") == "success":
            return data.get("image_base64", "")
        return ""

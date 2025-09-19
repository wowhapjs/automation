import httpx
from bs4 import BeautifulSoup

def fetch_title(url: str) -> str:
    with httpx.Client(timeout=15) as c:
        r = c.get(url, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        return (soup.title.string or "").strip()

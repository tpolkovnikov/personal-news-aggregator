from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import feedparser

app = FastAPI()

# Enable CORS for local frontend (http://localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

rss_link = "http://www.ria.ru/export/rss2/index.xml"

@app.get("/rss")
def get_rss(url: Optional[str] = None, limit: int = 10):
    """Parse an RSS/Atom feed and return basic fields.

    Query params:
    - url: optional feed URL (defaults to module-level rss_link)
    - limit: number of items to return
    """
    feed_url = rss_link
    parsed = feedparser.parse(feed_url)

    if getattr(parsed, "bozo", False) and not getattr(parsed, "entries", []):
        raise HTTPException(status_code=400, detail="Invalid or unreadable RSS/Atom feed")

    items = []
    for entry in parsed.entries[: max(limit, 0)]:
        items.append({
            "title": entry.get("title"),
            "link": entry.get("link"),
            "published": entry.get("published") or entry.get("updated"),
            "summary": entry.get("summary"),
        })

    print(items)

    return {
        "items": items,
    }

# Do not execute on import
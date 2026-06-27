from fastapi import FastAPI, HTTPException

from app.services.youtube_scraper import scrape_youtube

app = FastAPI(
    title="YouTube Scraper API",
    description="YouTube Search Scraper using Playwright",
    version="1.0.0"
)

@app.get("/youtube/search", tags=["YouTube Scraper"])
async def youtube_search(keyword: str):

    if not keyword or not keyword.strip():
        raise HTTPException(
            status_code=400,
            detail="Keyword is required"
        )

    try:
        results = await scrape_youtube(keyword)

        return {
            "success": True,
            "count": len(results),
            "data": results
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

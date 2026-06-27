# YouTube Scraper API

A FastAPI-based YouTube scraper that returns YouTube search results using Playwright.

## Features

- Search YouTube by keyword
- Returns up to 20 search results
- Includes:
  -Title
  - Video URL
  - Channel Name
  - View Count
  - Thumbnail URL

## Setup

Create a virtual environment:

bash
python -m venv venv


Activate it:

bash
venv\Scripts\activate


Install dependencies:

bash
pip install -r requirements.txt


Install Playwright Chromium:

bash
playwright install chromium


## Run

bash
python -m uvicorn app.main:app --reload --port 9001


## API Documentation

Swagger UI:

text
http://127.0.0.1:9001/docs


## Endpoint

### Search YouTube

http
GET /youtube/search


Query Parameter:

text
keyword


Example:

http
GET /youtube/search?keyword=python


Example Response:

json
{
  "success": true,
  "count": 20,
  "data": [
    {
      "title": "Python Full Course for Beginners",
      "video_url": "https://youtube.com/watch?v=xxxx",
      "channel_name": "Programming with Mosh",
      "view_count": "6.7M views",
      "thumbnail_url": "https://i.ytimg.com/..."
    }
  ]
}

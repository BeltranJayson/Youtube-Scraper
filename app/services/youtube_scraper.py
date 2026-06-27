from urllib.parse import quote
from playwright.sync_api import sync_playwright
import asyncio


def scrape_youtube_sync(keyword: str):
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(
            f"https://www.youtube.com/results?search_query={quote(keyword)}"
        )

        page.wait_for_timeout(5000)

        videos = page.locator("ytd-video-renderer")

        count = videos.count()

        for i in range(min(count, 20)):
            try:
                video = videos.nth(i)

                title = video.locator("#video-title").text_content()
                title = " ".join(title.split()) if title else ""

                url = video.locator("#video-title").get_attribute("href")

                video_url = (
                    f"https://youtube.com{url}"
                    if url
                    else ""
                )

                channel_name = ""

                channel_locator = video.locator(
                    "ytd-channel-name a"
                )

                if channel_locator.count() > 0:
                    channel_name = channel_locator.first.text_content()
                    channel_name = (
                        " ".join(channel_name.split())
                        if channel_name
                        else ""
                    )

                view_count = ""

                metadata_locator = video.locator(
                    "#metadata-line span"
                )

                if metadata_locator.count() > 0:
                    view_count = (
                        metadata_locator.nth(0).text_content() or ""
                    )

                thumbnail_url = ""

                thumbnail_locator = video.locator("img")

                if thumbnail_locator.count() > 0:
                    thumbnail_url = (
                        thumbnail_locator.first.get_attribute("src")
                        or ""
                    )

                results.append({
                    "title": title,
                    "video_url": video_url,
                    "channel_name": channel_name,
                    "view_count": view_count,
                    "thumbnail_url": thumbnail_url
                })

            except Exception:
                continue

        browser.close()

    return results


async def scrape_youtube(keyword: str):
    return await asyncio.to_thread(
        scrape_youtube_sync,
        keyword
    )
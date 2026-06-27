import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        page = await browser.new_page()

        await page.goto(
            "https://www.youtube.com/results?search_query=python"
        )

        await page.wait_for_timeout(3000)

        videos = page.locator("ytd-video-renderer")

        count = await videos.count()

        print(f"Found {count} videos\n")

        for i in range(min(count, 5)):
            video = videos.nth(i)

            # Title
            title = await video.locator("#video-title").text_content()
            title = " ".join(title.split()) if title else ""

            # URL
            url = await video.locator("#video-title").get_attribute("href")
            video_url = f"https://youtube.com{url}" if url else ""

            # Channel Name
            channel_name = ""

            channel_locator = video.locator("ytd-channel-name a")

            if await channel_locator.count() > 0:
                channel_name = await channel_locator.first.text_content()
                channel_name = " ".join(channel_name.split())

            # View Count
            view_count = ""

            metadata_locator = video.locator("#metadata-line span")

            if await metadata_locator.count() > 0:
                view_count = await metadata_locator.nth(0).text_content()
                view_count = view_count.strip()

            # Thumbnail
            thumbnail_url = ""

            thumbnail_locator = video.locator("img")

            if await thumbnail_locator.count() > 0:
                thumbnail_url = (
                    await thumbnail_locator.first.get_attribute("src")
                or ""
                )

            if await thumbnail_locator.count() > 0:
                thumbnail_url = await thumbnail_locator.first.get_attribute(
                    "src"
                )

            print({
                "title": title,
                "video_url": video_url,
                "channel_name": channel_name,
                "view_count": view_count,
                "thumbnail_url": thumbnail_url
            })

            print("-" * 80)

        await browser.close()


asyncio.run(main())
import time
from typing import Tuple
import asyncio

from playwright.async_api import Playwright, async_playwright


async def run(playwright: Playwright, URL: str) -> Tuple[str | None, str]:
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto(URL)
    await page.get_by_role("button", name="Sort reviews").click()
    await page.get_by_role("menuitemradio", name="Newest").click()
    await page.get_by_role("button", name="Actions").first.click()

    await page.get_by_role("menuitemradio", name="Share review").click()

    link = await page.get_by_role("textbox").get_attribute("value")
    await page.goto(link)  # type: ignore
    page_content: list[str] = (
        await page.get_by_role("main")
        .locator("div")
        .filter(has_text="ago")
        .nth(1)
        .all_text_contents()
    )
    star: str | None = await page.get_by_role("img", name="star").get_attribute(
        "aria-label"
    )

    await context.close()
    await browser.close()

    return (star.strip()[0], page_content[0])  # type: ignore


async def extract_review(URL: str) -> Tuple[str | None, str]:
    async with async_playwright() as playwright:
        output = await run(
            playwright,
            URL=URL,
        )
        return output


def extract(URL: str) -> Tuple[str | None, str]:
    output = asyncio.run(extract_review(URL))
    return output


if __name__ == "__main__":
    URL = input("Enter the URL of the review to extract: ")
    st = time.perf_counter()
    tuki = asyncio.run(extract_review(URL))
    print(time.perf_counter() - st)
    print(tuki)

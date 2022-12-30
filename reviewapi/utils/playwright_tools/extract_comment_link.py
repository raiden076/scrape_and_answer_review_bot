# Not necessary Now, but just in case

import asyncio

from playwright.async_api import Playwright, async_playwright


async def run(playwright: Playwright, URL: str) -> str | None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto(URL)
    await page.get_by_role("button", name="Sort reviews").click()
    await page.get_by_role("menuitemradio", name="Newest").click()
    await page.get_by_role("button", name="Actions").first.click()
    # time.sleep(2)
    await page.get_by_role("menuitemradio", name="Share review").click()
    # time.sleep(2)
    link = await page.get_by_role("textbox").get_attribute("value")
    # time.sleep(2)
    # ---------------------
    await context.close()
    await browser.close()
    # ---------------------
    return link


async def extract_link(URL: str) -> str | None:
    async with async_playwright() as playwright:
        output = await run(
            playwright,
            URL=URL,
        )
        return output


if __name__ == "__main__":
    URL = input("Enter the URL of the shop to extract: ")
    print(asyncio.run(extract_link(URL)))

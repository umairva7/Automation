from time import sleep
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def requestHTML(page, browser, x=1):
    url = "https://priceoye.pk/mobiles"
    page.goto(url)
    sleep(6)

    # Extract page HTML
    html = page.content()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.title.text)

    # Close browser
    browser.close()

with sync_playwright() as p:
    # 1️⃣ Launch Browser
    browser = p.chromium.launch(headless=False)

    # 2️⃣ Create New Page / Tab
    page = browser.new_page()

    # 3️⃣ Call your function (pass page and browser)
    requestHTML(page, browser)

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()

    # Go to target site
    url = "https://priceoye.pk/mobiles"
    page.goto(url)

    # Wait for product list to load
    page.wait_for_selector("//div[@id='product_list_scroll_identifier']")

    # Find all product links
    links = page.locator("//div[@class='productBox b-productBox']/a[@class='ga-dataset']")

    # Loop through them and print href attributes
    count = links.count()
    for i in range(count):
        href = links.nth(i).get_attribute("href")
        print(href)

    browser.close()

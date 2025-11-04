from playwright.sync_api import sync_playwright
import time

pw=sync_playwright().start()

#creating browser
browser=pw.chromium.launch(headless=False,slow_mo=2000)

#creating page/tab
page=browser.new_page()

url = "https://priceoye.pk/mobiles"
page.goto(url)

page=page.locator("xpath=//div[@id='product_list_scroll_identifier']")

links=page.locator("xpath=//a[@class='ga-dataset']").get_attribute("href")

for link in links:
    print(link)








browser.close()
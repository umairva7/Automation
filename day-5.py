from playwright.sync_api import sync_playwright
import time

pw=sync_playwright().start()

#creating browser
browser=pw.chromium.launch(headless=False,slow_mo=2000)

#creating page/tab
page=browser.new_page()

url = "https://priceoye.pk/mobiles"
page.goto(url)


print(page.content())
print(page.title())
page.screenshot(path='screenshot.png')




browser.close()
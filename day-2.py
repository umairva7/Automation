from requests_html import HTMLSession

URL='https://beerwulf.com/collections/blade-kegs?page=2'

print("Day -2 ")


s=HTMLSession()
r=s.get(URL)

r.html.render(sleep=1)

products=r.html.xpath('//*[@id="shopify-section-template--26799930999119__main"]/product-collection/div/product-grid/div',first=True)


#print(products.absolute_links)

for item in products.absolute_links:
    r=s.get(item)
    name=r.html.xpath('//*[@id="shopify-section-template--26799934112079__main"]/variant-details-code/product-form-code/section[1]/div[1]/div/h1',first=True).text
    try:
        price=r.html.xpath('//*[@id="shopify-section-template--26799934112079__main"]/variant-details-code/product-form-code/section[1]/div[1]/div/div[1]/p[2]',first=True).text
    except:
        price=''
    print(f'Name:{name} Price:{price} ')

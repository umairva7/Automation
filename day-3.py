import requests
import json
from bs4 import BeautifulSoup


#Step1 : Requests

url="https://www.accommodationforstudents.com/search-results?location=London&beds=0&occupancy=min&minPrice=0&maxPrice=500&latitude=51.509865&longitude=-0.118092&geo=false&page=1&filterName=location"
r=requests.get(url)

#print(r.status_code)

soup = BeautifulSoup(r.content,'html.parser')
print(soup.title) # to check if we are in the right page

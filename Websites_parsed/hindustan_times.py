##data parsing for Hindustan times
#Centre Headline

from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req = Request('https://www.hindustantimes.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
containers = page_soup.find_all("div", {"class": "big-middlenews"})
for container in containers:
    Product_container = container.find("div",{"class": "bigstory-h2"})
    Product_Name = Product_container.text.strip()
    print(Product_Name)

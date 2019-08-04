from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import itertools
myurl= 'https://timesofindia.indiatimes.com/home/headlines'
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.find("div", {"class": "overlay-content"})

for container in containers:
    Product_container = container.find("div", {"class": "overlay-content"})
    Product_Name = Product_container.get_txt

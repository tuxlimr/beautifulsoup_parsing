from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req4 = Request('https://scroll.in/', headers={'User-Agent': 'Mozilla/5.0'})
webpage4 = urlopen(req4).read()
page_soup4 = soup(webpage4, "html.parser")
containers4 = page_soup4.find("div", {"class": "featured-story column scroll-box scroll-box-3"})
p4 = containers4.find("div",{"class":"row-story"})
print(p4.h1.text)
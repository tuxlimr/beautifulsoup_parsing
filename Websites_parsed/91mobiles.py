from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req1 = Request('https://www.91mobiles.com/hub/category/news-2/', headers={'User-Agent': 'Mozilla/5.0'})
webpage1 = urlopen(req1).read()
page_soup1 = soup(webpage1, "html.parser")
containers1 = page_soup1.find("div", {"class": "td-module-thumb img_height"})
p1 = containers1.find("img",{"class":"entry-thumb lazyload"})
print(p1.get("title"))
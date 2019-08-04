from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req = Request('https://www.techradar.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
containers3 = page_soup.find("div", {"id": "Item1"})
p = containers3.find("figure", {"class": "feature-block-item"})

print(p.find("span", {"class": "article-name"}).text)


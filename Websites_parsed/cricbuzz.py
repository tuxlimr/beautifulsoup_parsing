from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req4 = Request('https://www.cricbuzz.com//', headers={'User-Agent': 'Mozilla/5.0'})
webpage4 = urlopen(req4).read()
page_soup4 = soup(webpage4, "html.parser")
containers41 = page_soup4.find("div", {"class": "big-crd-main cb-bg-white"})
containers42 = containers41.h2.text
print(containers42)
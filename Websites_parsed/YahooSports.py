from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req = Request('https://sports.yahoo.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
containers3 = page_soup.find("div", {"class": "C(#fff) Mb(14px)"})
print(containers3)
# print(containers3.h2.text)
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req3 = Request('https://www.espncricinfo.com/', headers={'User-Agent': 'Mozilla/5.0'})
webpage3= urlopen(req3).read()
page_soup31 = soup(webpage3, "html.parser")
containers32 = page_soup31.find("div", {"class": "contentItem__titleWrapper"})
containers33 = containers32.h1.text
print(containers33)
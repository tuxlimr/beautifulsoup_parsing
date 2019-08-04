from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req5 = Request('https://timesofindia.indiatimes.com/home/headlines', headers={'User-Agent': 'Mozilla/5.0'})
webpage5 = urlopen(req5).read()
page_soup5 = soup(webpage5, "html.parser")
containers5 = page_soup5.find("div", {"class": "top-newslist"})
p5 = containers5.find("span", {"class": "w_tle"})
print(p5.text)
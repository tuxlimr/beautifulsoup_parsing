##Data parsing for India today
#Main Headline

from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
req = Request('https://www.indiatoday.in/news.html', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
containers3 = page_soup.find("div", {"class": "col-md-12 col-sm-12"})
print(containers3.h3.text)



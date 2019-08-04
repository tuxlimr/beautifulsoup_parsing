import requests
from bs4 import BeautifulSoup
# import pandas

r = requests.get("https://www.imdb.com/search/title/?release_date=2017&sort=num_votes,desc&page=2&ref_=adv_nxt")
content = r.content
soup = BeautifulSoup(content, "html.parser")
Class = soup.find_all("div", {"class":"lister-item mode-advanced"})


for i in Class:
    Text = i.find("a")
    print(Text.text)


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
e = pyttsx3.init()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

myurl= 'https://www.flipkart.com/search?q=iphone&otracker=start&as-show=on&as=off'
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "_1UoZlX"})
# print(len(containers))
# print(soup.prettify(containers[0]))
# container = containers[0]

filename="products.csv"
f = open(filename,"w", encoding='utf-8')

headers= "Product_Name, Pricing, Ratings\n"
f.write(headers)

for container in containers:
    Product_container = container.find("div",{"class": "_3wU53n"})
    Product_Name = Product_container.text.strip()

    price_container = container.find("div", {"class": "col col-5-12 _2o7WAb"})
    price = price_container.div.div.div.text

    Ratings_container = container.find("div", {"class": "hGSR34"})
    Ratings = Ratings_container.text

    print("Product_Name:", Product_Name)
    print("price :" + price)
    print("Ratings:" + Ratings)
    f.write(Product_Name + price + Ratings)
f.close()
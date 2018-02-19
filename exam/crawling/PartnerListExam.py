import requests
from bs4 import BeautifulSoup

html = requests.get('http://new.encar.com/fc/fc_carmnfccert.do?mnfccd=012').text
soup = BeautifulSoup(html, 'html.parser')

priceList = soup.findAll("span.prc")
listCar = soup.findAll("div", {"id" : "search"})

# print(soup)
print(priceList)
print(listCar)

import requests
from bs4 import BeautifulSoup

html = requests.get('http://new.encar.com/dc/dc_cardetailview.do?pageid=fc_carsearch&listAdvType=normal&carid=21551285').text
soup = BeautifulSoup(html, 'html.parser')

info = soup.select('#depth_main > div.contents > div.wrp_quick > div > div.aside > div.info_car > div.box_info_top > h3 > span')
print('정보 : ' + info[0].getText())

price = soup.select('#depth_main > div.contents > div.wrp_quick > div > div.aside > div.info_car > div.box_info_top > p')
print('가격 : ' + price[0].getText().replace('가격', ''))


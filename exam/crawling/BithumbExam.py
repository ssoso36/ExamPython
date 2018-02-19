import urllib.request
import json
page = urllib.request.urlopen("https://api.bithumb.com/public/ticker/all")
text = page.read().decode("utf8")

jsonStr = json.loads(text)

arrCoin = ['BTC', 'ETH', 'DASH', 'LTC', 'XRP', 'BCH', 'XMR', 'ZEC', 'QTUM', 'BTG', 'EOS']

for coin in arrCoin:
    print(coin + ' : ' + jsonStr['data'][coin]['closing_price'])
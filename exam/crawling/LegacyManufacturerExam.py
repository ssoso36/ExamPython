import urllib.request
import json

page = urllib.request.urlopen("http://apidev.encar.com/legacy/usedcar/car/manufacturer")
text = page.read().decode("utf8")

for text in json.loads(text):
    print(text['code'], text['name'])

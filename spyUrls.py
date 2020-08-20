#-*- coding = utf-8 -*-
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
num = 1
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")

def askURL(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0"
        }
    res = urllib.request.Request(url=url,headers=headers)
    reponse = urllib.request.urlopen(res)
    html = reponse.read().decode("utf-8")
    return html

def getData(bs, index):
    rule = re.compile(r'<a href="/news(.*?)\" title')
    op = open("data_homepage/listUrls_{}.txt".format(index),"w")
    # for item in bs.find_all('div', class_="articleh normal_post"):
    for item in bs.find_all('span', class_="l3 a3"):
        item = str(item)
        print("item =", item)
        hrefs = rule.findall(item)

        print("hrefs =", hrefs)
        for href in hrefs:
            op.write("https://guba.eastmoney.com/news" + href + '\n') 
    op.close()


url = "https://guba.eastmoney.com/list,601216_{}.html"
pages = 11

for index in range(1, pages+1):
    html = askURL(url.format(index))
    print("===================\n")
    op = open("data_homepage/homepage_{}.txt".format(index), "w")
    op.write(html)            
    op.close()
    bs = BeautifulSoup(html,"html.parser")
    getData(bs, index)
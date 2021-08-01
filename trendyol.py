import requests 
from bs4 import BeautifulSoup
from send_email import sendMail
import time


url1 = "https://www.trendyol.com/pull-bear/erkek-gri-suni-yunlu-kareli-ince-ceket-09470504-p-58847704?boutiqueId=543516&merchantId=112044"

def checkPrice(url,paramPrice):
headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"

}
page = requests.get(url1, headers=headers)

htmlPage = BeautifulSoup(page.content,'html.parser') #HTML sayfsının içeriğini çektik 

productTitle=htmlPage.find("h1", class_="pr-new-br").getText()

price = htmlPage.find("span",class_="prc-slg").getText()

image = htmlPage.find("img", class_="ph-gl-img")

convertedPrice = float(price.replace(",",".").replace("TL",""))

if(convertedPrice <= paramPrice):
        print("Ürün fiyatı düştü")
        htmlEmailContent= """\
            <html>
            <head></head>
            <body>
            <h3>{0}</h3>
            <br/>
            {1}
            <br/>
            <p>Ürün linki: {2}</p>
            </body>
            </html>
            """.format(productTitle, image, url)
        sendMail("KIME_EMAIL","Ürünün fiyatı düştü👍👍", htmlEmailContent)
else:
        print("ürün fiyatı düşmedi")

while(True):
    checkPrice(url1,150)
    time.sleep(3)
import requests 
from bs4 import BeautifulSoup

url1 = "https://www.trendyol.com/pull-bear/erkek-gri-suni-yunlu-kareli-ince-ceket-09470504-p-58847704?boutiqueId=543516&merchantId=112044"

headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"

}
page = requests.get(url1, headers=headers)

htmlPage = BeautifulSoup(page.content,'html.parser') #HTML sayfsının içeriğini çektik 



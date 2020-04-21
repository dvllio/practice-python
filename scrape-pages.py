# Scrape elements across multiple pages

import requests
from bs4 import BeautifulSoup

def getPageNb(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')

  for x in soup.find_all('li','current'):
    x = int(((x.text).split())[-1])
    print ("There are",x,"pages")
    return x

def getTitles(pageNb):
  for page in range(1,pageNb+1):
    url = baseUrl + '/catalogue/page-' + str(page) + '.html'
    print ("---")
    print ("page",page)
    print ("---")
    r2 = requests.get(url)
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    for z in soup2.find_all('article', 'product_pod'):
      print(">>",z.h3.a.get("title"))

baseUrl = "http://books.toscrape.com"
getTitles(getPageNb(baseUrl))
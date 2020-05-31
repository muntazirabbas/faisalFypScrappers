import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pymongo
from selenium import webdriver
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')

def goToSaleDetail(saleUrl):
    #get colors and size of product
    mainUrl = "https:"
    driver.get(saleUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    title = soup.find('h1', attrs={ 'class' : 'page-header'}).text
    # print('title ', title)
    startDate  = soup.find('span', attrs={'class' : 'date-display-single'}).text
    # print('date ', startDate)
    buyLink  = mainUrl +  soup.find('a', attrs={'class' : 'btn btn-xs btn-info m-b'})['href']
    # print('liknk ', buyLink)
    saleData = {
        "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
        "title": title,
        "startDate": startDate,
        "buyLink": buyLink
    }
    print('sale data ', saleData)
    # mydb.whatsonsale.insert_one(saleData)
    print('................................................................................................')

def processSitePageSoup(soup):
        mainUrl = "https://whatsonsale.com.pk"
        print('in soup page ')
        salesLinks = soup.findAll('div', {'class': "offer clearfix"})
        # print("sales link ", salesLinks)
        for link in salesLinks:
            detailLink =  mainUrl + link.find('a')['href']
            print(detailLink)
            goToSaleDetail(detailLink)

#find list to iterate

print('starting scrapping')


def startSalesScrapping(_url):
        print('sitePage ', _url)
        driver.get(_url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup)

try:
    _url = "https://whatsonsale.com.pk/categories/fashion?page=1"
    # startLink = "https://whatsonsale.com.pk/categories/fashion?page="+str(page)
    # print('startlink ', startLink)
    startSalesScrapping(_url)
except Exception as el:
    print("Exception occured ", el)
    driver.close()

# driver.close()

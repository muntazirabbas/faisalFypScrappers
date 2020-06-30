import random
import requests
# import time
from datetime import date, datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
# url = driver.command_executor._url
# session_id = driver.session_id
# driver = webdriver.Remote(command_executor=url, desired_capabilities={})
# driver.close()  # this prevents the dummy browser
# driver.session_id = session_id

from datetime import date

print('starting scrapping')


def goToProductDetail(_detailUrl):
    print('product url ', _detailUrl)
    driver.get(_detailUrl)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # print('detail soup ', soup)
    productTitle = ""
    price = 0
    shipingAndHandling = 0
    totalBeforeTax = 0
    estTax = 0
    importFeeDeposit = 0
    orderTotal = 0
    paymentTotal = 0
    paymentCurrenty = 0
    applicableExcRate = 'N/A'
    productUrl = _detailUrl

    if (soup.find('span', attrs={'id': 'productTitle'})):
        productTitle = soup.find('span', attrs={'id': 'productTitle'}).text.strip().replace('\n', '')
        # print('product titile ', productTitle)
    if (soup.find('div', attrs={'id': 'a-popover-agShipMsgPopover'})):
        priceDiv = soup.find('div', attrs={'id': 'a-popover-agShipMsgPopover'}).find('table').findAll('tr')
        price = priceDiv[0].findAll('span')[1].text.strip()
        shipingAndHandling = priceDiv[1].findAll('span')[1].text.strip()
        importFeeDeposit = priceDiv[2].findAll('span')[1].text.strip()
        orderTotal = priceDiv[-1].findAll('span')[1].text.strip()
        paymentTotal = orderTotal
        paymentCurrenty = "dollar"
        estTax = float(shipingAndHandling.replace('$', '').replace(',', '')) + float(
            importFeeDeposit.replace('$', '').replace(',', ''))

        productDetail = {
            'productTitle': productTitle,
            'price': price,
            'shipingAndHandling': shipingAndHandling,
            'totalBeforeTax': price,
            'estTax': estTax,
            'importFeeDeposit': importFeeDeposit,
            'orderTotal': orderTotal,
            'paymentTotal': paymentTotal,
            'paymentCurrenty': paymentCurrenty,
            'applicableExcRate': applicableExcRate,
            'productUrl': productUrl
        }

        print('product data ', productDetail)
        mydb.amazonEs.insert_one(productDetail)
    print('................................................................................................')
    # driver.close()


jsonData = []


def processSitePageSoup(soup):
    print('processing soup')
    products = soup.findAll('div', attrs={'class': 's-include-content-margin s-border-bottom s-latency-cf-section'})
    print('products count ', len(products))

    productTitle = ""
    price = 0
    shipingAndHandling = 0
    totalBeforeTax = 0
    estTax = 0
    importFeeDeposit = 0
    orderTotal = 0
    paymentTotal = 0
    paymentCurrenty = 0
    applicableExcRate = 'N/A'
    productUrl = ''

    for product in products:
        if (product):

            firstLink = "sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32"
            secondLink = "a-section a-spacing-none a-spacing-top-micro"
            priceClass = "a-price-whole"
            if (product.find('div', attrs={'class', firstLink})) and (
            product.find('div', attrs={'class', secondLink})) and (product.find('span', attrs={'class', priceClass})):
                if (product.find('div', attrs={'class': 'a-row'})):
                    shipingRow = product.find('div', attrs={'class', 'a-row'})
                    if ('de envío' in shipingRow.text.lower().strip()):
                        shipingAndHandling = shipingRow.split('€ de envío')[0].replace(',', '.')
                        price = product.find('span', attrs={'class', priceClass}).text.replace(',', '.')
                        # price = priceDiv[0].findAll('span')[1].text.strip()
                        # shipingAndHandling = priceDiv[1].findAll('span')[1].text.strip()
                        # importFeeDeposit = priceDiv[2].findAll('span')[1].text.strip()
                        # orderTotal = priceDiv[-1].findAll('span')[1].text.strip()
                        # paymentTotal = orderTotal
                        # paymentCurrenty = "dollar"
                        # estTax = float(shipingAndHandling.replace('$', '').replace(',', '')) + float(
                        #     importFeeDeposit.replace('$', '').replace(',', ''))
                        # 
                        # productDetail = {
                        #     'productTitle': productTitle,
                        #     'price': price,
                        #     'shipingAndHandling': shipingAndHandling,
                        #     'totalBeforeTax': price,
                        #     'estTax': estTax,
                        #     'importFeeDeposit': importFeeDeposit,
                        #     'orderTotal': orderTotal,
                        #     'paymentTotal': paymentTotal,
                        #     'paymentCurrenty': paymentCurrenty,
                        #     'applicableExcRate': applicableExcRate,
                        #     'productUrl': productUrl
                        # }

            # goToProductDetail(buyUrl)

            # if(('ships to united kingdom' in productText) or ('shipping' in productText)):
            #     print('contains text__')
            #     goToProductDetail(buyUrl)
            # else:
            #     print('doest not contains text ', buyUrl)


def openSitePage(_pageLink):
    driver.get(_pageLink)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    processSitePageSoup(soup)


try:
    # https://www.amazon.com/s?k=laptops&page=1
    # for pageNo in range(1,200):
    # amazonPageLink = "https://www.amazon.com/b/ref=mh_565108_is_pn_"+str(pageNo)+"?rh=n%3A172282%2Cn%3A%21493964%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108&page="+str(pageNo)+"&ie=UTF8&qid=1592893049&node=565108"
    amazonPageLink = "https://www.amazon.es/"
    print('pagelink _____________', amazonPageLink)
    openSitePage(amazonPageLink)

except Exception as el:
    print("Exception occured ", el)
    driver.close()








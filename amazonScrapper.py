from bs4 import BeautifulSoup
from selenium import webdriver
import pymongo
import time
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')

print('starting scrapping')

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
            priceClass = "a-price-whole"
            if (product.find('div', attrs={'class', firstLink})) and (product.find('span', attrs={'class', priceClass})):
                    appendUrl = "https://www.amazon.es/"
                    shipingRows = product.findAll('span')
                    shipRowData = ''
                    for shipRow in shipingRows:
                        # print('shipRow ', shipRow)
                        if(("de envío" in shipRow.text.lower().strip())):
                            shipRowData = shipRow
                            # print('in de envio check ')
                    # print('shipRowData ', shipRowData)
                    if(shipRowData != ''):
                        shipingAndHandling = shipRowData.text.strip().split('€ de envío')[0].replace(',', '.').replace('\xa0','')
                    else:
                        shipingAndHandling = 0
                        # print('shipping and handling ', shipingAndHandling)
                    price = product.find('span', attrs={'class', priceClass}).text.replace('.', '').replace(',','.')
                    print('price ', price)
                    # if(float(price) < 100):
                    #     print('Price lower than 100')
                    # else:
                    importFeeDeposit = 'N/A'
                    paymentCurrenty = "Euro"
                    estTax = shipingAndHandling
                    orderTotal = float(price) + float(shipingAndHandling)
                    paymentTotal = orderTotal
                    productTitle = product.find('span', attrs = {'class' : 'a-size-medium a-color-base a-text-normal'}).text.strip()
                    productUrl = appendUrl + product.find('a', attrs = {'class' : 'a-link-normal a-text-normal'})['href']
                    print('shipingAndHandling ', shipingAndHandling)
                    if(shipingAndHandling == 0):
                        shipingAndHandling = 'N/A'
                        estTax = 'N/A'
                    else:
                        shipingAndHandling =  shipingAndHandling.strip().replace('\xa0', '')
                        estTax =  estTax.strip().replace('\xa0', '')

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
                    mydb.amazonEsArgMayNotShip.insert_one(productDetail)
                    print('................................................................................................')


def openSitePage(_pageLink):
    driver.get(_pageLink)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    processSitePageSoup(soup)


try:
    # https://www.amazon.com/s?k=laptops&page=1
    signInlink = "https://www.amazon.es/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.es%2Fs%3Fk%3Dlaptops%26i%3Dcomputers%26rh%3Dn%253A667049031%252Cn%253A938008031%26dc%26__mk_es_ES%3D%25C3%2585M%25C3%2585%25C5%25BD%25C3%2595%25C3%2591%26qid%3D1593525161%26rnid%3D1703620031%26ref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=esflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
    driver.get(signInlink)
    email = "mechaniconline1@gmail.com"
    password = "Wh0isthis??"
    print("email  and passowrd ")
    print(email)
    print(password)
    time.sleep(70)
    for pageNo in range(1,100):
        # amazonPageLink = "https://www.amazon.com/b/ref=mh_565108_is_pn_"+str(pageNo)+"?rh=n%3A172282%2Cn%3A%21493964%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108&page="+str(pageNo)+"&ie=UTF8&qid=1592893049&node=565108"
        amazonPageLink= "https://www.amazon.es/s?k=laptops&i=computers&rh=n%3A667049031%2Cn%3A938008031&dc&page="+str(pageNo)+"&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1593525161&rnid=1703620031&ref=sr_pg_"+str(pageNo)
        print('pagelink _____________', amazonPageLink)
        openSitePage(amazonPageLink)

except Exception as el:
    print("Exception occured ", el)
    # driver.close()
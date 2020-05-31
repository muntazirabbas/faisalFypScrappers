import time
from datetime import date,datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from fake_useragent import  UserAgent
import random
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
menBrands = [
    {'url': 'https://furorjeans.com/product-category/top/casual-shirts-for-men/', 'name': 'CASUAL SHIRTS'},
    {'url': 'http://furorjeans.wpengine.com/product-category/top/graphic-art-t-shirts/', 'name': 'GRAPHIC TSHIRTS'},
    {'url': 'http://furorjeans.wpengine.com/product-category/bottom/denim-jeans/', 'name': 'JEANS'},
    {'url': 'http://furorjeans.wpengine.com/product-category/bottom/chinos/', 'name': 'CHINOS'},
    {'url': 'http://furorjeans.wpengine.com/product-category/outer-wear/hoodies/', 'name': 'HOODIES'},
    {'url': 'http://furorjeans.wpengine.com/product-category/outer-wear/jackets/', 'name': 'JACKETS'},
    {'url': 'http://furorjeans.wpengine.com/product-category/outer-wear/sweat-shirts/', 'name': 'SWEAT SHIRTS'},
    {'url': 'http://furorjeans.wpengine.com/product-category/accessories/socks/', 'name': 'SOCKS'},
    {'url': 'http://furorjeans.wpengine.com/product-category/accessories/bags/', 'name': 'BAGS'},
    {'url': 'http://furorjeans.wpengine.com/product-category/accessories/belts/', 'name': 'BELTS'},
    {'url': 'http://furorjeans.wpengine.com/product-category/accessories/bracelets/', 'name': 'BRACELETS'},
    {'url': 'http://furorjeans.wpengine.com/product-category/top/polo-shirts/', 'name': 'POLO SHIRTS'},
]

def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    print('product url ', productUrl)
    driver.get(productUrl)
    # time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    size = []
    sizeDiv = []
    if(soup.find('select', attrs={'id' : 'pa_size'})):
        sizeDiv = soup.find('select', attrs={'id' : 'pa_size'}).findAll('option')[1:]
    for _size in sizeDiv:
        if (_size):
            # print('size => ',_size.text)
            size.append(_size.text.strip().lower())
        # print('sizeDiv ', sizeDiv)
    _productData['size'] = size
    print('product data ', _productData)
    mydb.products.insert_one(_productData)
    # print('................................................................................................')

def processSitePageSoup(soup, brandName,gender):
    colors = []
    for rowdata in soup.select('li[class*="qv-hover product-display-standard"]'):
        if (rowdata != None):
            buy_url = rowdata.findAll('a')[-1]['href']
            title = rowdata.find('div', attrs={'class': 'product-details'}).find('a').text.strip()
            # color = ""
            # if(title.split("–").__len__() > 1):
            #     color = title.split("–")[-1].strip().lower()
            # print('color ', color)
            # compareColors = ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 'lime', 'maroon', 'navy', 'olive', 'orange', 'purple', 'red', 'silver', 'teal', 'white', 'yellow']
            # for _name in compareColors:
            #     if _name in color:
            #         print('_name match', _name)

            # print('color after compare ___________', color)
            imageURL = rowdata.find("img")['src']
            price = rowdata.find('span', {'class': 'woocommerce-Price-amount amount'})
            colorFirst = title.lower().split('-')
            # print('colors ', colorFirst)
            color = colorFirst[-1].split('–')[-1].strip()
            # print('final color ', color)

            if not (color.isdigit()):
               colors = [color]
            else:
                colors = []
            dataObject = {
                "id" : random.choice(list(range(0,100000)))+random.choice(list(range(77,15400)))+random.choice(list(range(55,5000))),
                'name' :  "title",
                'colors': colors,
                'size': [],
                'pictures' : [imageURL],
                'stock' : "N/A",
                'price' : int(price.text.strip()[2:].replace(',','')),
                'discount' : 0,
                'salePrice' : 0,
                'description': '',
                'tags': [gender,brandName],
                'rating': random.choice(list(range(3, 5))),
                'category':gender,
                'buyUrl': buy_url,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'furorjeans'
            }
            # print("data________",dataObject, "/n buyUrl",buy_url)
            goToProductDetail(dataObject,buy_url)

def openSitePage(brandData, gender):
    print("brandData " , brandData)
    for sitePage in brandData:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],gender)


def getAllLinks(scrapeUrl):
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source,'lxml')
    brandSoup = soup.findAll('div', attrs={'class': 'textwidget'})[3].findAll('a')
    print('brand soup ', brandSoup)
    print('soup_____length', brandSoup.__len__())
    for brand in brandSoup:
        # print("brand_", brand)
        if(brand['href']):
            print(brand['href'])
            print(brand.text.strip())
            menBrands.append(
                        {
                            'url': brand['href'],
                            'name': brand.text.strip()
                        })
        print('........................................................................')
    driver.close()
    print('menBrands =', menBrands)



try:
    allBrands = [{'blist':menBrands, 'name': 'men'}]
    for brand in allBrands:
       openSitePage(brand['blist'], brand['name'])
except Exception as el:
    print("Exception occured ", el)
    driver.close()


# try:
#     scrapeUrl = "https://furorjeans.com/product-category/top/casual-shirts-for-men/"
#     getAllLinks(scrapeUrl)
# except Exception as el:
#     print("Error opening site  ", el)
#     driver.close()
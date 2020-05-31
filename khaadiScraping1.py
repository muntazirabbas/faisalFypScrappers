import random
import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
womenBrands = [{'url': 'https://pk.khaadi.com/new-in.html?material=219', 'name': 'cambric'}, {'url': 'https://pk.khaadi.com/new-in.html?material=227', 'name': 'brosha'}, {'url': 'https://pk.khaadi.com/new-in.html?material=229', 'name': 'raw silk'}, {'url': 'https://pk.khaadi.com/new-in.html?material=231', 'name': 'denim'}, {'url': 'https://pk.khaadi.com/new-in.html?material=232', 'name': 'viscose'}, {'url': 'https://pk.khaadi.com/new-in.html?material=233', 'name': 'khaddar'}, {'url': 'https://pk.khaadi.com/new-in.html?material=234', 'name': 'marina'}, {'url': 'https://pk.khaadi.com/new-in.html?material=236', 'name': 'poly viscose'}, {'url': 'https://pk.khaadi.com/new-in.html?material=237', 'name': 'sateen'}, {'url': 'https://pk.khaadi.com/new-in.html?material=238', 'name': 'jacquard'}, {'url': 'https://pk.khaadi.com/new-in.html?material=239', 'name': 'silk'}, {'url': 'https://pk.khaadi.com/new-in.html?material=245', 'name': 'chiffon silk'}, {'url': 'https://pk.khaadi.com/new-in.html?material=246', 'name': 'chiffon'}, {'url': 'https://pk.khaadi.com/new-in.html?material=247', 'name': 'organza'}, {'url': 'https://pk.khaadi.com/new-in.html?material=248', 'name': 'handwoven'}, {'url': 'https://pk.khaadi.com/new-in.html?material=250', 'name': 'default'}, {'url': 'https://pk.khaadi.com/new-in.html?material=251', 'name': 'hand woven'}, {'url': 'https://pk.khaadi.com/new-in.html?material=253', 'name': 'woolen'}, {'url': 'https://pk.khaadi.com/new-in.html?material=254', 'name': 'acrylic'}, {'url': 'https://pk.khaadi.com/new-in.html?material=255', 'name': 'polyester'}, {'url': 'https://pk.khaadi.com/new-in.html?material=256', 'name': 'cotton stretch'}, {'url': 'https://pk.khaadi.com/new-in.html?material=257', 'name': 'schiffli'}, {'url': 'https://pk.khaadi.com/new-in.html?material=258', 'name': 'cross hatch denim'}, {'url': 'https://pk.khaadi.com/new-in.html?material=260', 'name': 'cross hatch'}, {'url': 'https://pk.khaadi.com/new-in.html?material=261', 'name': 'velvet'}, {'url': 'https://pk.khaadi.com/new-in.html?material=264', 'name': 'metallica'}, {'url': 'https://pk.khaadi.com/new-in.html?material=272', 'name': 'indian chiffon'}, {'url': 'https://pk.khaadi.com/new-in.html?material=273', 'name': 'tissue silk'}, {'url': 'https://pk.khaadi.com/new-in.html?material=274', 'name': 'viscose silk'}, {'url': 'https://pk.khaadi.com/new-in.html?material=275', 'name': 'polyester net'}, {'url': 'https://pk.khaadi.com/new-in.html?material=280', 'name': 'light khaddar'}, {'url': 'https://pk.khaadi.com/new-in.html?material=281', 'name': 'duck'}, {'url': 'https://pk.khaadi.com/new-in.html?material=282', 'name': 'dobby'}, {'url': 'https://pk.khaadi.com/new-in.html?material=284', 'name': 'oak silk'}, {'url': 'https://pk.khaadi.com/new-in.html?material=285', 'name': 'zari net'}, {'url': 'https://pk.khaadi.com/new-in.html?material=287', 'name': 'flannel'}, {'url': 'https://pk.khaadi.com/new-in.html?material=289', 'name': 'cotton net'}, {'url': 'https://pk.khaadi.com/new-in.html?material=290', 'name': 'self jacquard'}, {'url': 'https://pk.khaadi.com/new-in.html?material=291', 'name': 'silk viscose'}, {'url': 'https://pk.khaadi.com/new-in.html?material=297', 'name': 'plastic'}]
kidsBrands = [{'url': 'https://pk.khaadi.com/kids.html?material=216', 'name': 'poplin'}, {'url': 'https://pk.khaadi.com/kids.html?material=218', 'name': 'jersey'}, {'url': 'https://pk.khaadi.com/kids.html?material=219', 'name': 'cambric'}, {'url': 'https://pk.khaadi.com/kids.html?material=231', 'name': 'denim'}, {'url': 'https://pk.khaadi.com/kids.html?material=232', 'name': 'viscose'}, {'url': 'https://pk.khaadi.com/kids.html?material=233', 'name': 'khaddar'}, {'url': 'https://pk.khaadi.com/kids.html?material=250', 'name': 'default'}, {'url': 'https://pk.khaadi.com/kids.html?material=251', 'name': 'hand woven'}, {'url': 'https://pk.khaadi.com/kids.html?material=261', 'name': 'velvet'}, {'url': 'https://pk.khaadi.com/kids.html?material=287', 'name': 'flannel'}, {'url': 'https://pk.khaadi.com/kids.html?material=306', 'name': 'corduroy'}, {'url': 'https://pk.khaadi.com/kids.html?material=307', 'name': 'terry'}, {'url': 'https://pk.khaadi.com/kids.html?material=308', 'name': 'twill'}, {'url': 'https://pk.khaadi.com/kids.html?material=313', 'name': 'cotton yd'}, {'url': 'https://pk.khaadi.com/kids.html?material=314', 'name': 'lycra jersey'}]

womenSalesBrands = [
    {'url': 'https://pk.khaadi.com/sale.html?cat=1391', 'name': 'Pret'},
]

kidsSalesBrands = [
    {'url': 'https://pk.khaadi.com/sale.html?cat=1394', 'name': 'Mix'},
]

def goToProductDetail(_productData,productUrl, collectionName):
    #get colors and size of product
    print('product url ', productUrl)
    driver.get(productUrl)
    time.sleep(7)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    colorDiv = []
    sizeDiv = []
    try:
        colorDiv = soup.find('div', attrs={'class': 'swatch-attribute color'}).select('div[class*="swatch-option color"]')
        sizeDiv = soup.select('div[class*="swatch-attribute-options clearfix"]')[1].select('div[class*="swatch-option text"]')
    except Exception as el:
        print("product detail exception  ", el)

    price = int(soup.find('span', attrs={'class': 'price'}).text.strip()[3:].replace(',', ''))
    colors = []
    size = []
    # print('color div _____ ', colorDiv)
    if(sizeDiv):
        for _size in sizeDiv:
            # print('size => ',_size)
            size.append(_size.text.strip())
    if(colorDiv):
        # print('color div _____ 2222 ', colorDiv)
        for _color in colorDiv:
            # print('color => ', _color)
            colors.append(_color['option-label'].strip().lower())
    _productData['colors'] = colors
    _productData['size'] = size
    _productData['price'] = price
    _productData['salePrice'] = price
    print('product data ', _productData)
    # mydb[collectionName].insert_one(_productData)
    print('................................................................................................')


def getBrandData(soup,brandName,gender, collectionName):
    for khad in soup:
        if(khad):
            buy_url = khad.find('a')['href']
            title = khad.find('a', {'class': "product-item-link"}).text.strip()
            imageURL = ""
            for i in khad.findAll('img'):
                imageURL = i['src']

            dataObject = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                'name': title,
                'pictures': [imageURL],
                'stock': "N/A",
                'price': 0,
                'discount': 0,
                'salePrice': 0,
                'description': '',
                'tags': [gender, brandName],
                'rating': random.choice(list(range(0, 5))),
                'category': gender,
                'colors': [],
                'size': [],
                'buyUrl': buy_url,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'khaadi'
            }
            goToProductDetail(dataObject, buy_url, collectionName)

def processBrands(brandArray,type, collectionName):
    for data in brandArray:
        print('site url ', data['url'])
        driver.get(data['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        khaadi = soup.select('li[class*="item product product-item"]')
        getBrandData(khaadi,data['name'],type, collectionName)


def getAllLinks(_url):
    driver.get(_url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    allUrls = soup.findAll('a', attrs={'class': 'mgs-ajax-layer-item'})[8:23]
    myarray = []
    for brand in allUrls:
        if(brand['href']):
            linkUrl = brand['href']
            name = brand.contents[0].strip()
            print('anchor____', linkUrl)
            print('name______', name)
            myarray.append(
                        {
                            'url': linkUrl,
                            'name': name
                        })
        print('........................................................................')
    driver.close()
    print('womenBrands ', myarray)

def ScrapSales(collectionName):
    try:
        salesBrands = [
            {'blist': womenSalesBrands, 'name': 'women'},
            {'blist': kidsSalesBrands, 'name': 'kids'},
        ]
        for brand in salesBrands:
            processBrands(brand['blist'], brand['name'],collectionName)
    except Exception as el:
        print("Exception occured ", el)
        driver.close()

def ScrapProducts(collectionName):
    try:
        allBrands = [
            {'blist': womenBrands, 'name': 'women'},
            {'blist': kidsBrands, 'name': 'kids'},
        ]
        for brand in allBrands:
            processBrands(brand['blist'], brand['name'],collectionName)
    except Exception as el:
        print("Exception occured ", el)
        driver.close()

try:

    ScrapSales('sales')
    # ScrapProducts('products')
    # scrapeUrl = 'https://pk.khaadi.com/kids.html'
    # getAllLinks(scrapeUrl)
except Exception as el:
    print("Exception occured ", el)
    driver.close()

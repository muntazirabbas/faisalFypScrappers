import random
from datetime import datetime
from bs4 import BeautifulSoup
import pymongo
from selenium import webdriver
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome("C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe",chrome_options=chrome_options)
# driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
menBrands =  [
               #  {'url': 'https://monark.com.pk/collections/t-shirts', 'name': 'T-SHIRTS'},
               # {'url': 'https://monark.com.pk/collections/polo-shirts', 'name': 'POLO SHIRTS'},
               # {'url': 'https://monark.com.pk/collections/casual-shirts', 'name': 'Casual Shirts'},
               # {'url': 'https://monark.com.pk/collections/formal-shirts', 'name': 'FORMAL/DRESS SHIRTS'},
               # {'url': 'https://monark.com.pk/collections/formal-pants', 'name': 'FORMAL/DRESS PANTS'},
               # {'url': 'https://monark.com.pk/collections/chinos-5-pockets', 'name': 'CHINO/COTTON PANTS'},
               # {'url': 'https://monark.com.pk/collections/jeans', 'name': 'JEANS/COTTON JEANS'},
               # {'url': 'https://monark.com.pk/collections/joggers', 'name': 'TROUSER/JOG PANTS'},
               # {'url': 'https://monark.com.pk/collections/shorts', 'name': 'Shorts'},
               # {'url': 'https://monark.com.pk/collections/suits', 'name': 'SUITS'},
               {'url': 'https://monark.com.pk/collections/blazers', 'name': 'COATS/BLAZERS'}
            ]

def getColor(color):
    if "black" in color:
        return "black"
    elif "blue" in color:
        return "blue"
    elif "white" in color:
        return "white"
    elif "red" in color:
        return "red"
    elif "green" in color:
        return "green"
    elif "navy" in color:
        return "navy"
    else:
        return "other"


def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    # print('product url ', productUrl)
    driver.get(productUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # print("detail soup ",soup)
    priceSpans = soup.find('span', attrs={'class': 'price price--sale'}).findAll('span')
    size = []
    price = 0
    # print('sizes ', sizeDiv)
    if(soup.find('div', attrs={'class': 'product-options__section d-flex flex-wrap'})):
        for _size in soup.find('div', attrs={'class': 'product-options__section d-flex flex-wrap'}).findAll('div'):
            if(_size) and ('disabled' not in _size.attrs['class']):
                # print('size => ', _size)
                size.append(_size.text)
    if(priceSpans[1]):
        price = priceSpans[1].text.strip()
    else:
        price = priceSpans[0].text.strip()
    _productData['size'] = size
    _productData['price'] =  float(price[3:].replace(',',''))
    mydb.freshProducts.insert_one(_productData)
    print('product data ', _productData)

def openSitePage(brandData, type):
    for sitePage in brandData:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],type)

jsonData = []
def processSitePageSoup(soup, brandName,gender):
    domainName = "https://monark.com.pk"
    products = soup.findAll('div', attrs={'class': 'col-6 col-sm-6 col-md-6 col-lg-6 col-xl-4'})
    # print('products ', products)
    for product in products:
        if(product):
            # print("product======>>>>",product)
            title = product.find('div', attrs={'class':'product-collection__title mb-3'}).text.strip()
            color = getColor(title.lower())
            buyUrl = domainName + product.find('a')['href'].strip()
            _image = 'https:'+ product.find('img')['data-srcset'].strip().split(',')[0]
            pictures = [_image]

            dataObject = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                'name': title,
                'price': 0,
                'pictures': pictures,
                'stock': 'N/A',
                'discount': 0,
                'salePrice': 0,
                'description': '',
                'tags': [gender, brandName],
                'rating': 'N/A',
                'category': gender,
                'colors': [color],
                'size': [],
                'buyUrl': buyUrl,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'monark'
            }
            # print('data_____',dataObject)
            goToProductDetail(dataObject,buyUrl)

print('starting scrapping')

def getAllLinks():
    scrapeUrl = "https://monark.com.pk"
    domainName = "https://monark.com.pk"
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source,'lxml')
    for brand in soup.findAll('div', {'class': 'menu__item'}):
        # print("brand_", brand['class'])
        if(brand.find('a') != -1) and (len(brand.findAll('a')) == 1):
                # print(brand.find('a')['href'])
                # print(brand.find('a').text.strip())
                menBrands.append(
                        {
                            'url': domainName + brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
        print('........................................................................')
    driver.close()
    print('menBrands = ', menBrands)

# #start point for getting all the links for men,women,kids brands urls and brand names
try:
    # getAllLinks()
    openSitePage(menBrands, 'men')
except Exception as el:
    print("Error opening site  ", el)
    driver.close()


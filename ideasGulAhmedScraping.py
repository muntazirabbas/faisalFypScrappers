import random
from datetime import datetime
import time
from bs4 import BeautifulSoup
import pymongo
from selenium import webdriver
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')

womenBrands = [
    {'url': 'https://www.gulahmedshop.com/women/ideas-pret/solids', 'name': 'SOLIDS'},
    {'url': 'https://www.gulahmedshop.com/women/ideas-pret/digitals', 'name': 'DIGITALS'},
    {'url': 'https://www.gulahmedshop.com/women/ideas-pret/stitched-suits', 'name': 'SUITS'},
    {'url': 'https://www.gulahmedshop.com/women/ideas-pret/semi-formals', 'name': 'SEMI-FORMALS'},
    {'url': 'https://www.gulahmedshop.com/women/ideas-pret/formals', 'name': 'FORMALS'},
    {'url': 'https://www.gulahmedshop.com/women/ideas-pret/trousers', 'name': 'TROUSERS'},
    {'url': 'https://www.gulahmedshop.com/women/stitched-kurtis', 'name': 'KURTIS'},
    {'url': 'https://www.gulahmedshop.com/women/western-17/tops', 'name': 'TOPS'},
    {'url': 'https://www.gulahmedshop.com/women/western-17/bottoms', 'name': 'BOTTOMS'},
    {'url': 'https://www.gulahmedshop.com/women/western-17/sweaters', 'name': 'SWEATERS'},
    {'url': 'https://www.gulahmedshop.com/accessories/shawls-stoles', 'name': 'SHAWLS/STOLES'}
]
kidsBrands = [
    {'url': 'https://www.gulahmedshop.com/kids/girls/girls-eastern/kurtis', 'name': 'KURTIS'},
    {'url': 'https://www.gulahmedshop.com/kids/girls/girls-eastern/2pc-suits', 'name': '2PC SUITS'},
    {'url': 'https://www.gulahmedshop.com/kids/girls/girls-eastern/trousers', 'name': 'TROUSERS'},
    {'url': 'https://www.gulahmedshop.com/kids/girls/girls-western/sweaters', 'name': 'SWEATERS'},
    {'url': 'https://www.gulahmedshop.com/kids/girls/girls-western/shirts', 'name': 'TEES'},
    {'url': 'https://www.gulahmedshop.com/kids/girls/girls-western/tops', 'name': 'TOPS'},
    {'url': 'https://www.gulahmedshop.com/kids/boys/sweaters', 'name': 'SWEATERS'},
    {'url': 'https://www.gulahmedshop.com/kids/home/bed-sheet', 'name': 'BED SHEETS'},
    {'url': 'https://www.gulahmedshop.com/kids/home/bath-robes', 'name': 'BATHROBES'},
    {'url': 'https://www.gulahmedshop.com/kids/home/towel', 'name': 'TOWELS'}]
menBrands = [
    {'url': 'https://www.gulahmedshop.com/mens-clothes/western/dress-shirts', 'name': 'DRESS SHIRTS'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/western/casual-shirts', 'name': 'CASUAL SHIRTS'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/western/polos', 'name': 'POLOS'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/western/tees', 'name': 'TEES'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/western/sweaters', 'name': 'SWEATERS'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/western/jackets', 'name': 'JACKETS'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/western/dress-pants', 'name': 'DRESS PANTS'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/western/khaki-s', 'name': "KHAKI'S"},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/western/jeans', 'name': 'JEANS'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/western/trousers', 'name': 'TROUSERS'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/western/shorts', 'name': 'SHORTS'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/western/belts', 'name': 'BELTS'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/eastern/kurta', 'name': 'KURTA'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/eastern/suits', 'name': 'SUITS'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/eastern/president-edition', 'name': 'PRESIDENT EDITION'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/eastern/shalwar', 'name': 'ETHNIC BOTTOMS'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/eastern/stitched-waist-coat', 'name': 'STITCHED WAIST COAT'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/unstitched/men-chairman-latha', 'name': 'CHAIRMAN LATHA'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/unstitched/shawls', 'name': 'SHAWLS'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/unstitched/regular', 'name': 'CLASSIC'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/unstitched/winter', 'name': 'WINTER'},
    {'url': 'https://www.gulahmedshop.com/mens-clothes/unstitched/summer', 'name': 'SUMMER'}
]

def colorAssignment(color):
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

def goToProductDetail(_productData, productUrl, collectionName):
    #get colors and size of product
    print('product url ', productUrl)
    driver.get(productUrl)
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    size = []
    if(soup.find('div', attrs={'class' : 'swatch-attribute-options clearfix'})):
        sizeDiv = soup.find('div', attrs={'class' : 'swatch-attribute-options clearfix'}).findAll('div')
        for _size in sizeDiv:
            if (_size):
                size.append(_size.text.strip().lower())
    price = 0
    if(soup.find('div', attrs={'class': 'product-info-main'}).find('span', attrs={'class': 'price'})):
        price = soup.find('div', attrs={'class': 'product-info-main'}).find('span', attrs={'class': 'price'}).text.strip()[4:]
    price = float(price.replace(',', ''))
    # print('price__',price)

    _productData['size'] = size
    _productData['price'] = price
    _productData['salePrice'] = 0
    _productData['discount'] = 0
    print('product data ', _productData)
    mydb[collectionName].insert_one(_productData)
    print('................................................................................................')


def openSitePage(brandData, type,collectionName):
    for sitePage in brandData:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],type,collectionName)


def processSitePageSoup(soup, brandName,gender,collectionName):
        khaadi = soup.findAll("li", {"class": "item product product-item"})[0:17]
        for khad in khaadi:
            buy_url = khad.find('a')['href']
            title = khad.find('a', {'class': "product-item-link"}).text.strip()
            imageURL = khad.findAll('img')[0]['src']
            color = colorAssignment(title.lower())

            dataObject = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                'name': title,
                'pictures': [imageURL],
                'stock': 'N/A',
                'price': 0,
                'discount': 0,
                'salePrice': 0,
                'description': '',
                'tags': [gender, brandName],
                'rating': random.choice(list(range(3, 5))),
                'category': gender,
                'colors': [color],
                'size': [],
                'buyUrl': buy_url,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'gulahmed'
            }
            # print('data__',dataObject)
            goToProductDetail(dataObject,buy_url,collectionName)

print('starting scrapping')

#find list to iterate
def getAllLinks():
    scrapeUrl = "https://www.gulahmedshop.com/"
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source,'lxml')
    womenSoup1 = soup.findAll('ul', attrs={'class': 'groupdrop-link'})[8].findAll('li')
    womenSoup2 = soup.findAll('ul', attrs={'class': 'groupdrop-link'})[10].findAll('li')
    womenSoup3 = soup.findAll('ul', attrs={'class': 'groupdrop-link'})[11].findAll('li')
    womenSoup = womenSoup1 + womenSoup2 + womenSoup3

    print('womensoup ', womenSoup)
    menSoup1 = soup.findAll('ul', attrs={'class': 'groupdrop-link'})[13].findAll('li')
    menSoup2 = soup.findAll('ul', attrs={'class': 'groupdrop-link'})[14].findAll('li')
    menSoup3 = soup.findAll('ul', attrs={'class': 'groupdrop-link'})[15].findAll('li')
    menSoup = menSoup1 + menSoup2 + menSoup3
    print('menSoup ', menSoup)
    kidsSoup1 = soup.findAll('ul', attrs={'class': 'groupdrop-link'})[16].findAll('li')
    kidsSoup2 = soup.findAll('ul', attrs={'class': 'groupdrop-link'})[17].findAll('li')
    kidsSoup3 = soup.findAll('ul', attrs={'class': 'groupdrop-link'})[18].findAll('li')
    kidsSoup4 = soup.findAll('ul', attrs={'class': 'groupdrop-link'})[19].findAll('li')
    kidsSoup = kidsSoup1 + kidsSoup2 + kidsSoup3 + kidsSoup4
    print('kidsSoup ', kidsSoup)
    for brand in menSoup:
        print('brand ', brand)
        if(brand.find('a') != -1):
            print(brand.find('a')['href'])
            print(brand.find('a').text.strip())
            menBrands.append(
                        {
                            'url':  brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
    for brand in kidsSoup:
            # print('brand ', brand)
            if (brand.find('a') != -1):
                # print(brand.find('a')['href'])
                # print(brand.find('a').text.strip())
                kidsBrands.append(
                    {
                        'url': brand.find('a')['href'],
                        'name': brand.find('a').text.strip()
                    })
    for brand in womenSoup:
        # print('brand ', brand)
        if(brand.find('a') != -1):
            # print(brand.find('a')['href'])
            # print(brand.find('a').text.strip())
            womenBrands.append(
                        {
                            'url':  brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })

    print('kidsBrands = ', kidsBrands)
    print('womenBrands = ', womenBrands)
    print('menBrands = ', menBrands)
    driver.close()


#start point for scrapping all the data

def ScrapProducts(collectionName):
    try:
        allBrands = [
                        # {'blist': womenBrands, 'name': 'women'},
                        # {'blist': kidsBrands, 'name': 'kids'},
                        {'blist': menBrands, 'name': 'men'},
                    ]
        for brand in allBrands:
            openSitePage(brand['blist'], brand['name'],collectionName)
    except Exception as el:
        print("Exception occured ", el)
        driver.close()

try:

    ScrapProducts('freshProducts')
    # getAllLinks()
except Exception as el:
    print("Exception occured ", el)
    driver.close()

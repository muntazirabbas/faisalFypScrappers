import random
import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
# dbProducts = mydb.freshProducts.find({'mainBrand' : 'khaadi'})

driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
kidsBrands =  [{'url': 'https://pk.khaadi.com/kids/girls-eastern/kurta.html', 'name': 'Kurta'}, {'url': 'https://pk.khaadi.com/kids/girls-eastern/pants.html', 'name': 'Pants'}, {'url': 'https://pk.khaadi.com/kids/girls-eastern/formal-suits.html', 'name': 'Formal Suits'}, {'url': 'https://pk.khaadi.com/kids/girls-western/blouses.html', 'name': 'Blouses'}, {'url': 'https://pk.khaadi.com/kids/girls-western/dresses.html', 'name': 'Dresses'}, {'url': 'https://pk.khaadi.com/kids/girls-western/tights.html', 'name': 'Tights'}, {'url': 'https://pk.khaadi.com/kids/girls-western/pants.html', 'name': 'Pants'}, {'url': 'https://pk.khaadi.com/kids/girls-western/denim.html', 'name': 'Denim'}, {'url': 'https://pk.khaadi.com/kids/girls-western/t-shirts.html', 'name': 'T Shirts'}, {'url': 'https://pk.khaadi.com/kids/girls-western/jogger-pants.html', 'name': 'Jogger Pants'}, {'url': 'https://pk.khaadi.com/kids/boys-eastern/kurta.html', 'name': 'Kurta'}, {'url': 'https://pk.khaadi.com/kids/boys-eastern/waistcoat.html', 'name': 'Waistcoat'}, {'url': 'https://pk.khaadi.com/kids/boys-western/t-shirts.html', 'name': 'T Shirts'}, {'url': 'https://pk.khaadi.com/kids/boys-western/shirts.html', 'name': 'Shirts'}, {'url': 'https://pk.khaadi.com/kids/boys-western/jogger-pants.html', 'name': 'Jogger Pants'}, {'url': 'https://pk.khaadi.com/kids/boys-western/polo-shirts.html', 'name': 'Polo Shirts'}, {'url': 'https://pk.khaadi.com/kids/boys-western/briefs.html', 'name': 'briefs'}, {'url': 'https://pk.khaadi.com/kids/boys-western/boys-socks.html', 'name': 'Socks'}, {'url': 'https://pk.khaadi.com/kids/essentials-accessories/socks.html', 'name': 'Socks'}]
womenBrands =  [{'url': 'https://pk.khaadi.com/unstitched/festive-eid-collection.html', 'name': 'Festive Eid Collection'}, {'url': 'https://pk.khaadi.com/unstitched/spring-collection.html', 'name': 'Spring Collection'}, {'url': 'https://pk.khaadi.com/unstitched/summer-collection.html', 'name': 'Summer Collection'}, {'url': 'https://pk.khaadi.com/unstitched/luxury-collection.html', 'name': 'Luxury Collection'}, {'url': 'https://pk.khaadi.com/unstitched.html?material=215', 'name': 'Lawn'}, {'url': 'https://pk.khaadi.com/unstitched.html?material=238', 'name': 'Jacquard'}, {'url': 'https://pk.khaadi.com/unstitched.html?material=257', 'name': 'Schiffli'}, {'url': 'https://pk.khaadi.com/unstitched.html?size=31', 'name': 'Two Piece'}, {'url': 'https://pk.khaadi.com/unstitched.html?size=32', 'name': 'Three Piece'}, {'url': 'https://pk.khaadi.com/ready-to-wear/pret/basic-kurta.html', 'name': 'Basic Kurta'}, {'url': 'https://pk.khaadi.com/ready-to-wear/pret/printed-kurta.html', 'name': 'Printed Kurta'}, {'url': 'https://pk.khaadi.com/ready-to-wear/pret/kurta-with-dupatta.html', 'name': 'Kurta with Dupatta'}, {'url': 'https://pk.khaadi.com/ready-to-wear/pret/kurta-with-pants.html', 'name': 'Kurta With Pants'}, {'url': 'https://pk.khaadi.com/ready-to-wear/pret/full-suit.html', 'name': 'Full Suit'}, {'url': 'https://pk.khaadi.com/ready-to-wear/pret/embroidered-kurta.html', 'name': 'Embroidered Kurta'}, {'url': 'https://pk.khaadi.com/ready-to-wear/khaas/semi-formals.html', 'name': 'Semi Formals'}, {'url': 'https://pk.khaadi.com/ready-to-wear/bottoms/tights.html', 'name': 'Tights'}, {'url': 'https://pk.khaadi.com/ready-to-wear/bottoms/pants.html', 'name': 'Pants'}, {'url': 'https://pk.khaadi.com/ready-to-wear/bottoms/shalwar.html', 'name': 'Shalwar'}, {'url': 'https://pk.khaadi.com/ready-to-wear/western/t-shirts.html', 'name': 'T Shirts'}, {'url': 'https://pk.khaadi.com/ready-to-wear/western/tunics.html', 'name': 'Tunics'}, {'url': 'https://pk.khaadi.com/ready-to-wear/western/pants.html', 'name': 'Pants'}, {'url': 'https://pk.khaadi.com/ready-to-wear/western/stoles.html', 'name': 'Stoles'}, {'url': 'https://pk.khaadi.com/ready-to-wear/western/tops.html', 'name': 'Tops'}, {'url': 'https://pk.khaadi.com/ready-to-wear/western/dresses.html', 'name': 'Dresses'}]


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

    price = float(soup.find('span', attrs={'class': 'price'}).text.strip()[3:].replace(',', ''))
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
    print('product data ', _productData)

    # if(any((_productData['name'] == product['name'] for product in dbProducts))):
    #     print(('existing product !!!!!!!!!!!!!!!!!!!!!!!!!!!!!'))
    # else:
    #     print('new product ================' )
    mydb[collectionName].insert_one(_productData)
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

def getAllLinks():
    scrapeUrl = 'https://pk.khaadi.com/'
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    womenUnstichedSoup = soup.find('ul', attrs={'id': "mobile-menu-54-1"}).findAll('li', attrs={'class' : 'level2'})
    print('womenUns ' , womenUnstichedSoup)
    womenReadydSoup = soup.find('ul', attrs={'id': "mobile-menu-53-1"}).findAll('li', attrs={'class' : 'level2'})
    kidsSoup = soup.find('ul', attrs={'id': "mobile-menu-55-1"}).findAll('li', attrs={'class' : 'level2'})
    womenSoup = womenUnstichedSoup + womenReadydSoup
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
        if (brand.find('a') != -1):
            # print(brand.find('a')['href'])
            # print(brand.find('a').text.strip())
            womenBrands.append(
                {
                    'url': brand.find('a')['href'],
                    'name': brand.find('a').text.strip()
                })

    print('kidsBrands = ', kidsBrands)
    print('womenBrands = ', womenBrands)

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

    ScrapProducts('freshProducts')
    # getAllLinks()
except Exception as el:
    print("Exception occured ", el)
    driver.close()

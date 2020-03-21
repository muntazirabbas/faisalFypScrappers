import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pymongo
from selenium import webdriver
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
menBrands   = [{'url': 'https://www.gulahmedshop.com/mens-clothes/western/dress-shirts', 'name': 'DRESS SHIRTS'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/western/casual-shirts', 'name': 'CASUAL SHIRTS'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/western/polos', 'name': 'POLOS'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/western/tees', 'name': 'TEES'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/western/sweaters', 'name': 'SWEATERS'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/western/jackets', 'name': 'JACKETS'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/western/dress-pants', 'name': 'DRESS PANTS'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/western/khaki-s', 'name': "KHAKI'S"}, {'url': 'https://www.gulahmedshop.com/mens-clothes/western/jeans', 'name': 'JEANS'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/western/trousers', 'name': 'TROUSERS'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/western/shorts', 'name': 'SHORTS'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/western/belts', 'name': 'BELTS'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/eastern/kurta', 'name': 'KURTA'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/eastern/suits', 'name': 'SUITS'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/eastern/stitched-waist-coat', 'name': 'STITCHED WAIST COAT'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/eastern/shalwar', 'name': 'ETHNIC BOTTOMS'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/eastern/president-edition', 'name': 'PRESIDENT EDITION'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/unstitched/men-chairman-latha', 'name': 'CHAIRMAN LATHA'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/unstitched/shawls', 'name': 'SHAWLS'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/unstitched/regular', 'name': 'CLASSIC'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/unstitched/winter', 'name': 'WINTER'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/unstitched/summer', 'name': 'SUMMER'}]
womenBrands = [{'url': 'https://www.gulahmedshop.com/unstitched-fabric/lawn-collection/summer-premium-collection', 'name': 'SUMMER PREMIUM COLLECTION'}, {'url': 'https://www.gulahmedshop.com/unstitched-fabric/lawn-collection/summer-basic-collection', 'name': 'SUMMER BASIC COLLECTION'}, {'url': 'https://www.gulahmedshop.com/unstitched-fabric/lawn-collection/bagh-e-gul', 'name': 'BAGH-E-GUL'}, {'url': 'https://www.gulahmedshop.com/unstitched-fabric/lawn-collection/vintage-garden', 'name': 'VINTAGE GARDEN'}, {'url': 'https://www.gulahmedshop.com/unstitched-fabric/lawn-collection/taani-jacquard-collection', 'name': 'TAANI JACQUARD COLLECTION'}, {'url': 'https://www.gulahmedshop.com/unstitched-fabric/lawn-collection/tribute-mothers-lawn-collection', 'name': 'TRIBUTE COLLECTION'}, {'url': 'https://www.gulahmedshop.com/unstitched-fabric/lawn-collection/uni-trend', 'name': 'UNI TREND'}, {'url': 'https://www.gulahmedshop.com/women/ideas-pret/solids', 'name': 'SOLIDS'}, {'url': 'https://www.gulahmedshop.com/women/ideas-pret/digitals', 'name': 'DIGITALS'}, {'url': 'https://www.gulahmedshop.com/women/ideas-pret/stitched-suits', 'name': 'SUITS'}, {'url': 'https://www.gulahmedshop.com/women/ideas-pret/semi-formals', 'name': 'SEMI-FORMALS'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/eastern', 'name': 'EASTERN'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/western', 'name': 'WESTERN'}, {'url': 'https://www.gulahmedshop.com/mens-clothes/unstitched', 'name': 'UNSTITCHED'}, {'url': 'https://www.gulahmedshop.com/ideas-home/bed-sheets', 'name': 'BED SHEETS'}, {'url': 'https://www.gulahmedshop.com/ideas-home/bed-sheets/throw', 'name': 'THROWS'}, {'url': 'https://www.gulahmedshop.com/ideas-home/bath-linen/towel', 'name': 'TOWELS'}, {'url': 'https://www.gulahmedshop.com/ideas-home/bed-sheets/dyed-sheet-set', 'name': 'DUVET SETS'}, {'url': 'https://www.gulahmedshop.com/ideas-home/home-accessories/cushion', 'name': 'CUSHION COVERS'}, {'url': 'https://www.gulahmedshop.com/ideas-home/home-accessories', 'name': 'ACCESSORIES'}]
kidsBrands  = [{'url': 'https://www.gulahmedshop.com/kids/girls/girls-eastern/kurtis', 'name': 'KURTIS'}, {'url': 'https://www.gulahmedshop.com/kids/girls/girls-eastern/2pc-suits', 'name': '2PC SUITS'}, {'url': 'https://www.gulahmedshop.com/kids/girls/girls-eastern/trousers', 'name': 'TROUSERS'}, {'url': 'https://www.gulahmedshop.com/kids/girls/girls-western/sweaters', 'name': 'SWEATERS'}, {'url': 'https://www.gulahmedshop.com/kids/girls/girls-western/shirts', 'name': 'TEES'}, {'url': 'https://www.gulahmedshop.com/kids/girls/girls-western/tops', 'name': 'TOPS'}, {'url': 'https://www.gulahmedshop.com/kids/boys/sweaters', 'name': 'SWEATERS'}, {'url': 'https://www.gulahmedshop.com/kids/home/bed-sheet', 'name': 'BED SHEETS'}, {'url': 'https://www.gulahmedshop.com/kids/home/bath-robes', 'name': 'BATHROBES'}, {'url': 'https://www.gulahmedshop.com/kids/home/towel', 'name': 'TOWELS'}]


def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    print('product url ', productUrl)
    driver.get(productUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # print("detail soup ",soup)
    sizeDiv =[]
    if(soup.find('select', attrs={'class' : 'swatch-attribute-options clearfix'})):
        sizeDiv = soup.find('select', attrs={'class' : 'swatch-attribute-options clearfix'}).findAll('div')
    price = soup.find('div', attrs={'class': 'product-info-main'}).find('span', attrs={'class': 'price'}).text.strip()[4:]
    print("pice_____", price)
    price = int(price.replace(',', ''))
    print('price__',price)
    colors = []
    size = []

    for _size in sizeDiv:
        if(_size):
            # print('size => ',_size.text)
            size.append(_size.text)

    _productData['colors'] = colors
    _productData['size'] = size
    _productData['price'] = price
    _productData['salePrice'] = price
    _productData['discount'] = price - price
    print('product data ', _productData)
    print('................................................................................................')


def openSitePage(brandData, type):
    for sitePage in brandData:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],type)


def processSitePageSoup(soup, brandName,gender):
        khaadi = soup.findAll("li", {"class": "item product product-item"})
        for khad in khaadi:
            price = khad.find('span', {'class': 'price'}).text.strip()[4:]
            buy_url = khad.find('a')['href']
            title = khad.find('a', {'class': "product-item-link"}).text.strip()
            imageURL = khad.findAll('img')[0]['src']
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
                'colors': [],
                'size': [],
                'buyUrl': buy_url,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'gulahmed'
            }
            # print('data__',dataObject)
            # if(dataObject['pictures'][0] != ""):
            #mydb.products.insert_one(dataObject)
            goToProductDetail(dataObject,buy_url)
            print('...........................................................................................')

print('starting scrapping')
#         url = "https://www.gulahmedshop.com/" + type_array[type_temp] + "?p="+str(pagecount)
#         response = requests.get(url,headers=header)
#         print(url)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         khaadi = soup.findAll("li", {"class": "item product product-item"})
#         for khad in khaadi:
#             price = khad.find('span', {'class': 'price'}).text.strip()[4:]
#             buy_url = khad.find('a')['href']
#             title = khad.find('a', {'class': "product-item-link"}).text.strip()
#             imageURL = khad.findAll('img')[0]['src']
#             dataObject = {
#                 "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
#                 'name': title,
#                 'pictures': [imageURL],
#                 'stock': random.choice(list(range(10, 400))),
#                 # 'price': int(price.strip().replace(',', '')),
#                 'discount': random.choice(list(range(0, 100))),
#                 # 'salePrice': int(price.strip().replace(',', '')) + random.choice([0, 300]),
#                 'description': '',
#                 'tags': [type_array[type_temp]],
#                 'rating': random.choice(list(range(0, 5))),
#                 'category': type_array[type_temp],
#                 'colors': [random.choice(colors), random.choice(colors), random.choice(colors)],
#                 'size': size,
#                 'buyUrl': buy_url,
#                 'gender': type_array[type_temp],
#                 'brand': '',
#                 'date': datetime.today(),
#                 'mainBrand': 'gulahmed'
#             }
#             print('data__',dataObject)
#             mydb.products.insert_one(dataObject)
#
#         pagecount -=1
#
#     type_temp += 1
#



#find list to iterate
def getAllLinks(_url):
    driver.get(_url)
    soup = BeautifulSoup(driver.page_source,'lxml')

    menSoup1 = soup.findAll('ul', attrs={'class': 'groupdrop-link'})[16].findAll('li')
    menSoup2 = soup.findAll('ul', attrs={'class': 'groupdrop-link'})[17].findAll('li')
    menSoup3 = soup.findAll('ul', attrs={'class': 'groupdrop-link'})[18].findAll('li')
    menSoup4 = soup.findAll('ul', attrs={'class': 'groupdrop-link'})[19].findAll('li')

    print("mensoup1",menSoup1)
    # womenSoup = soup.findAll('div', attrs={'class': 'col-1 parent-mega-menu'})[1].find('ul').findAll('li')
    # kidsSoup = soup.findAll('div', attrs={'class': 'col-1 parent-mega-menu'})[2].find('ul').findAll('li')
    for brand in menSoup1:
        print('brand ', brand)
        if(brand.find('a') != -1):
            # print(brand.find('a')['href'])
            # print(brand.find('a').text.strip())
            kidsBrands.append(
                        {
                            'url':  brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
    for brand in menSoup2:
            print('brand ', brand)
            if (brand.find('a') != -1):
                # print(brand.find('a')['href'])
                # print(brand.find('a').text.strip())
                kidsBrands.append(
                    {
                        'url': brand.find('a')['href'],
                        'name': brand.find('a').text.strip()
                    })
    for brand in menSoup3:
        print('brand ', brand)
        if(brand.find('a') != -1):
            # print(brand.find('a')['href'])
            # print(brand.find('a').text.strip())
            kidsBrands.append(
                        {
                            'url':  brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
    for brand in menSoup4:
        print('brand ', brand)
        if (brand.find('a') != -1):
            # print(brand.find('a')['href'])
            # print(brand.find('a').text.strip())
            kidsBrands.append(
                {
                    'url': brand.find('a')['href'],
                    'name': brand.find('a').text.strip()
                })
        print('........................................................................')
    print('kidsBrands__________', kidsBrands)

    driver.close()

##start point for getting all the links for men,women,kids brands urls and brand names

# try:
#     scrapeUrl = "https://www.gulahmedshop.com/women"
#     getAllLinks(scrapeUrl)
# except Exception as el:
#     print("Error opening site  ", el)
#     driver.close()

#start point for scrapping all the data
try:
    allBrands = [{'blist':kidsBrands, 'name': 'kids'},{'blist':menBrands, 'name': 'men'},{'blist':womenBrands, 'name': 'women'}]
    for brand in allBrands:
       openSitePage(brand['blist'], brand['name'])
except Exception as el:
    print("Exception occured ", el)
    driver.close()

driver.close()

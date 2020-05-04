import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pymongo
from selenium import webdriver
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
menBrands = [{'url': 'https://www.leisureclub.pk/men/tops-t-shirts/shirt.html', 'name': 'Shirt'}, {'url': 'https://www.leisureclub.pk/men/tops-t-shirts/t-shirt.html', 'name': 'T-Shirt'}, {'url': 'https://www.leisureclub.pk/men/tops-t-shirts/polo.html', 'name': 'Polo'}, {'url': 'https://www.leisureclub.pk/men/tops-t-shirts/henley.html', 'name': 'Henley'}, {'url': 'https://www.leisureclub.pk/men/tops-t-shirts/vest.html', 'name': 'Vest'}, {'url': 'https://www.leisureclub.pk/men/outerwear/jacket.html', 'name': 'Jacket'}, {'url': 'https://www.leisureclub.pk/men/outerwear/sweater.html', 'name': 'Sweater'}, {'url': 'https://www.leisureclub.pk/men/outerwear/coat.html', 'name': 'Coat'}, {'url': 'https://www.leisureclub.pk/men/outerwear/zipper.html', 'name': 'Zipper'}, {'url': 'https://www.leisureclub.pk/men/nightwear/night-suit.html', 'name': 'Night Suit'}, {'url': 'https://www.leisureclub.pk/men/bottoms/jeans.html', 'name': 'Jeans'}, {'url': 'https://www.leisureclub.pk/men/bottoms/short.html', 'name': 'Short'}, {'url': 'https://www.leisureclub.pk/men/bottoms/trouser.html', 'name': 'Trouser'}, {'url': 'https://www.leisureclub.pk/men/accessories/badge.html', 'name': 'Badge'}, {'url': 'https://www.leisureclub.pk/men/footwear/flip-flop.html', 'name': 'Flip Flop'}]
womenBrands = [{'url': 'https://www.leisureclub.pk/women/tops-t-shirts/top.html', 'name': 'Top'}, {'url': 'https://www.leisureclub.pk/women/tops-t-shirts/t-shirt.html', 'name': 'T-Shirt'}, {'url': 'https://www.leisureclub.pk/women/tops-t-shirts/suit.html', 'name': 'Suit'}, {'url': 'https://www.leisureclub.pk/women/tops-t-shirts/tunic.html', 'name': 'Tunic'}, {'url': 'https://www.leisureclub.pk/women/outerwear/cardigan.html', 'name': 'Cardigan'}, {'url': 'https://www.leisureclub.pk/women/outerwear/pullover.html', 'name': 'Pullover'}, {'url': 'https://www.leisureclub.pk/women/outerwear/blazer.html', 'name': 'Blazer'}, {'url': 'https://www.leisureclub.pk/women/outerwear/jacket.html', 'name': 'Jacket'}, {'url': 'https://www.leisureclub.pk/women/outerwear/reglan.html', 'name': 'Reglan'}, {'url': 'https://www.leisureclub.pk/women/outerwear/hoodie.html', 'name': 'Hoodie'}, {'url': 'https://www.leisureclub.pk/women/outerwear/sweater.html', 'name': 'Sweater'}, {'url': 'https://www.leisureclub.pk/women/outerwear/coat.html', 'name': 'Coat'}, {'url': 'https://www.leisureclub.pk/women/nightwear/night-suit.html', 'name': 'Night Suit'}, {'url': 'https://www.leisureclub.pk/women/bottoms/jean.html', 'name': 'Jean'}, {'url': 'https://www.leisureclub.pk/women/bottoms/trouser.html', 'name': 'Trouser'}, {'url': 'https://www.leisureclub.pk/women/bottoms/tight.html', 'name': 'Tight'}, {'url': 'https://www.leisureclub.pk/women/bottoms/jeggings.html', 'name': 'JEGGINGS'}, {'url': 'https://www.leisureclub.pk/women/accessories/belt.html', 'name': 'Belt'}, {'url': 'https://www.leisureclub.pk/women/footwear/shoe.html', 'name': 'Shoe'}, {'url': 'https://www.leisureclub.pk/women/footwear/flip-flop.html', 'name': 'Flip Flop'}]
kidsBrands = [{'url': 'https://www.leisureclub.pk/kids/boys/t-shirts-tops.html', 'name': 'T-Shirts & Tops'}, {'url': 'https://www.leisureclub.pk/kids/boys/outerwear.html', 'name': 'Outerwear'}, {'url': 'https://www.leisureclub.pk/kids/boys/nightwear.html', 'name': 'Nightwear'}, {'url': 'https://www.leisureclub.pk/kids/boys/bottoms.html', 'name': 'Bottoms'}, {'url': 'https://www.leisureclub.pk/kids/boys/footwear.html', 'name': 'Footwear'}, {'url': 'https://www.leisureclub.pk/kids/girls/t-shirts-tops.html', 'name': 'T-Shirts & Tops'}, {'url': 'https://www.leisureclub.pk/kids/girls/outerwear.html', 'name': 'Outerwear'}, {'url': 'https://www.leisureclub.pk/kids/girls/nightwear.html', 'name': 'NightWear'}, {'url': 'https://www.leisureclub.pk/kids/girls/bottoms.html', 'name': 'Bottoms'}, {'url': 'https://www.leisureclub.pk/kids/girls/footwear.html', 'name': 'Footwear'}, {'url': 'https://www.leisureclub.pk/kids/baby-boy/t-shirts-tops.html', 'name': 'T-Shirts & Tops'}, {'url': 'https://www.leisureclub.pk/kids/baby-boy/outerwear.html', 'name': 'Outerwear'}, {'url': 'https://www.leisureclub.pk/kids/baby-boy/bottoms.html', 'name': 'Bottoms'}, {'url': 'https://www.leisureclub.pk/kids/baby-boy/accessories.html', 'name': 'Accessories'}, {'url': 'https://www.leisureclub.pk/kids/baby-boy/footwear.html', 'name': 'Footwear'}, {'url': 'https://www.leisureclub.pk/kids/baby-girl/t-shirts-tops.html', 'name': 'T-Shirts & Tops'}, {'url': 'https://www.leisureclub.pk/kids/baby-girl/outerwear.html', 'name': 'Outerwear'}, {'url': 'https://www.leisureclub.pk/kids/baby-girl/bottoms.html', 'name': 'Bottoms'}, {'url': 'https://www.leisureclub.pk/kids/baby-girl/accessories.html', 'name': 'Accessories'}, {'url': 'https://www.leisureclub.pk/kids/baby-girl/footwear.html', 'name': 'Footwear'}]

def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    print('product url ', productUrl)
    driver.get(productUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    sizeDiv =[]
    if(soup.find('select', attrs={'class': 'currentSwatch required-entry super-attribute-select no-display swatch-select'})):
        sizeDiv = soup.find('select', attrs={'class': 'currentSwatch required-entry super-attribute-select no-display swatch-select'}).findAll('option')[1:]
    colorRow = soup.find('table', attrs={'class': 'data-table'}).find('tr')
    price = soup.find('span', attrs={'class': 'price'}).text.strip()[4:]
    colors = []
    size = []
    for _size in sizeDiv:
        if(_size):
            # print('size => ',_size.text.strip())
            size.append(_size.text.strip())
    if (colorRow.find('th').text.strip().lower() == 'color'):
            # print('color => ', colorRow.find('td').text.strip().lower())
            colors.append(colorRow.find('td').text.strip().lower())

    _productData['colors'] = colors
    _productData['size'] = size
    _productData['price'] = price
    print('product data ', _productData)
    print('................................................................................................')

def openSitePage(brandData, type):
    for sitePage in brandData:
        print('sitePage ', sitePage['url'])
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],type)

def processSitePageSoup(soup, brandName,gender):
        print('in soup page ')
        products = soup.select('li[class*="item col-lg-3 col-md-3 col-sm-6 col-xs-6"]')
        # print('products ', products)
        for product in products:
            buy_url = product.find('a')['href']
            title = product.find('h2', {'class': "product-name"}).text.strip()
            imageURL = product.find('img')['src']
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
                'mainBrand': 'leisureclub'
            }
            # print('data__',dataObject)
            # if(dataObject['pictures'][0] != ""):
            #mydb.products.insert_one(dataObject)
            goToProductDetail(dataObject,buy_url)
            # print('...........................................................................................')

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
    menLinks = soup.findAll('div', attrs={'class': 'parent level-0'})[1].findAll('li')
    womenLinks = soup.findAll('div', attrs={'class': 'parent level-0'})[2].findAll('li')
    kidsLinks = soup.findAll('div', attrs={'class': 'parent level-0'})[3].findAll('li')

    for brand in menLinks:
        if(brand.find('a') != -1):
            menBrands.append({'url':  brand.find('a')['href'],'name': brand.find('a').text.strip()})
    for brand in womenLinks:
            if (brand.find('a') != -1):
                womenBrands.append({'url': brand.find('a')['href'],'name': brand.find('a').text.strip()})
    for brand in kidsLinks:
        if(brand.find('a') != -1):
            kidsBrands.append({'url':  brand.find('a')['href'],'name': brand.find('a').text.strip()})
    print('menBrands = ', menBrands)
    print('womenBrands = ', womenBrands)
    print('kidsBrands = ', kidsBrands)

    driver.close()

# #start point for getting all the links for men,women,kids brands urls and brand names
# try:
#     scrapeUrl = "https://www.leisureclub.pk"
#     getAllLinks(scrapeUrl)
# except Exception as el:
#     print("Error opening site  ", el)
#     driver.close()

# starting point for scrapping all the data

print('starting scrapping')
try:
    allBrands = [{'blist':womenBrands, 'name': 'women'},{'blist':menBrands, 'name': 'men'},{'blist':kidsBrands, 'name': 'kids'}]
    for brand in allBrands:
       openSitePage(brand['blist'], brand['name'])
except Exception as el:
    print("Exception occured ", el)
    driver.close()
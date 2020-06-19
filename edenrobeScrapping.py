import random
from bs4 import BeautifulSoup
from datetime import datetime
import pymongo
from selenium import webdriver
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
salesUrl = "https://www.bonanzasatrangi.com/pk/sale/"
womenBrands =  [{'url': 'https://edenrobe.com/product-category/summer-collection/', 'name': 'Summer Collection ’20'}, {'url': 'https://edenrobe.com/product-tag/festive-collection-20/', 'name': 'Festive Collection ’20'},{'url': 'https://edenrobe.com/product-category/allure-khaddar-collection/', 'name': 'Allure Khaddar Collection’19'}, {'url': 'https://edenrobe.com/product-tag/monochrome-unstitched/', 'name': 'Monochrome Unstitched'}, {'url': 'https://edenrobe.com/product-tag/mysore-collection/', 'name': 'Mysore Luxury Collection ’19'}, {'url': 'https://edenrobe.com/product-tag/winter-un-stitched-collection-2019/', 'name': 'Winter Unstitched ’19'}, {'url': 'https://edenrobe.com/product-category/woman/cambric-collection-2019/', 'name': 'Cambric Collection'}, {'url': 'https://edenrobe.com/product-tag/festive-unstitched-collection/', 'name': 'Festive Unstitched Collection'}, {'url': 'https://edenrobe.com/product-tag/allure-collection/', 'name': 'Allure Collection'}, {'url': 'https://edenrobe.com/product-tag/sale-unstitched/', 'name': 'Un-stitched Sale'}, {'url': 'https://edenrobe.com/product-tag/pret/', 'name': 'Pret'}, {'url': 'https://edenrobe.com/product-tag/festive-pret/', 'name': 'Festive Pret'}, {'url': 'https://edenrobe.com/product-category/woman/ready-to-wear/western-tops/', 'name': 'Western Tops'}, {'url': 'https://edenrobe.com/product-tag/sale-pret/', 'name': 'Ready To Wear Sale'}, {'url': 'https://edenrobe.com/product-category/woman/trousers/', 'name': 'Tights & Trousers'}, {'url': 'https://edenrobe.com/product-tag/bags-clutches/', 'name': 'Bags & Clutches'}, {'url': 'https://edenrobe.com/product-category/woman/tank-tops/', 'name': 'Tank Tops'}]
menBrands =  [{'url': 'https://edenrobe.com/product-category/man/mens-fashion/mens-shalwar-kameez/', 'name': 'Shalwar Suits'}, {'url': 'https://edenrobe.com/product-category/man/mens-fashion/mens-kurta/', 'name': 'Kurtas'}, {'url': 'https://edenrobe.com/product-category/man/mens-fashion/swish-collection/', 'name': 'Swish Collection'}, {'url': 'https://edenrobe.com/product-category/man/mens-fashion/men-waistcoats/', 'name': 'Waistcoats'}, {'url': 'https://edenrobe.com/product-category/man/mens-fashion/mens-shalwars/', 'name': 'Shalwars'}, {'url': 'https://edenrobe.com/product-category/man/formal-trousers/formal-pants/', 'name': 'Formal Pants'}, {'url': 'https://edenrobe.com/product-tag/denim-pant/', 'name': 'Denim Pants'}, {'url': 'https://edenrobe.com/product-tag/urban-culture/', 'name': 'Urban Culture'}, {'url': 'https://edenrobe.com/product-category/man/men-suiting/formal-suits/', 'name': 'Formal Suits'}, {'url': 'https://edenrobe.com/product-category/man/winter-wear/casual-blazers/', 'name': 'Blazers'}, {'url': 'https://edenrobe.com/product-category/man/ceremonial/sherwanis/', 'name': 'Sherwanis'}, {'url': 'https://edenrobe.com/product-category/man/ceremonial/suiting/', 'name': 'Suits'}, {'url': 'https://edenrobe.com/product-tag/sweat-shirts/', 'name': 'Sweat Shirts'}, {'url': 'https://edenrobe.com/product-category/man/winter-wear/men-jackets/', 'name': 'Jackets'}, {'url': 'https://edenrobe.com/product-category/men-sweater/', 'name': 'Sweaters'}]
kidsBrands =  [{'url': 'https://edenrobe.com/product-category/kids/boys/shirts/', 'name': 'Casual Shirts'}, {'url': 'https://edenrobe.com/product-category/kids/boys/casual-t-shirts/', 'name': 'Casual Tees'}, {'url': 'https://edenrobe.com/product-category/kids/boys/polo-shirts-boys/', 'name': 'Polo Shirts'}, {'url': 'https://edenrobe.com/product-category/kids/boys/shorts/', 'name': 'Shorts'}, {'url': 'https://edenrobe.com/product-category/kids/boys/pant/', 'name': 'Pants'}, {'url': 'https://edenrobe.com/product-category/kids/boys/waistcoat-suit/', 'name': 'Waistcoat Suit'}, {'url': 'https://edenrobe.com/product-category/kids/boys/shalwar-suits/', 'name': 'Shalwar Suits'}, {'url': 'https://edenrobe.com/product-category/kids/boys/kurta/', 'name': 'Kurta'}, {'url': 'https://edenrobe.com/product-tag/hoodies/', 'name': 'Hoodies'}, {'url': 'https://edenrobe.com/product-category/kids/boys/full-sleeve-tees/', 'name': 'Full Sleeve Tees'}, {'url': 'https://edenrobe.com/product-category/kids/boys/sweaters/', 'name': 'Sweaters'}, {'url': 'https://edenrobe.com/product-category/kids/boys/jackets-winter-wear-kids/', 'name': 'Jackets'}, {'url': 'https://edenrobe.com/product-category/kids/boys/sherwani/', 'name': 'Sherwanis'}, {'url': 'https://edenrobe.com/product-category/kids/boys/coat-pant/', 'name': 'Suiting'},{'url': 'https://edenrobe.com/product-category/boys-tank-top/', 'name': 'Tank Top'}, {'url': 'https://edenrobe.com/product-category/kids/boys/casual-wasitcoat/', 'name': 'Casual Waistcoats'}]


def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    print('in detail page  ', productUrl)
    driver.get(productUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    sizeDiv = []
    if(soup.find('select', attrs={'name' : 'attribute_pa_size'})):
        sizeDiv = soup.find('select', attrs={'name' : 'attribute_pa_size'}).findAll('option')[1:]
    size = []
    for _size in sizeDiv:
        if(_size):
            # print('size => ',_size.text)
            size.append(_size.text)

    _productData['size'] = size
    print('product data ', _productData)
    mydb.freshProducts.insert_one(_productData)
    print('................................................................................................')

def openSitePage(brandData, type):
    for sitePage in brandData:
        print('sitePage ', sitePage['url'])
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],type)

def processSitePageSoup(soup, brandName,gender):
    if(soup.find('ul',attrs={'class' : 'products product-grid gutters row clearfix columns-4'})):
        products = soup.find('ul',attrs={'class' : 'products product-grid gutters row clearfix columns-4'}).select('li[class*="product-display-standard"]')
        for product in products:
            buy_url = product.find('a')['href']
            print('buyUrl ', buy_url)
            productDetails = product.find('div', {'class': "product-details"})
            title = productDetails.find('a').text.strip()
            price = 0
            if(productDetails.find('span', attrs={'class' : 'price'})):
                price = productDetails.find('span', attrs={'class' : 'price'}).findAll('span', attrs={'class' : 'woocommerce-Price-amount amount'})[-1].text.strip()[2:]
            imageURL = product.find('img')['src']

            sizes = []
            colorFirst = title.lower().split('-')
            # print('colors ', colorFirst)
            color = colorFirst[-1].split('–')[-1].strip()
            # print('final color ', color)
            colors = []
            if not (color.isdigit()):
                colors = [color]
            else:
                colors = []
            if(product.find('ul', attrs={'class': 'variable-items-wrapper button-variable-wrapper wvs-catalog-variable-wrapper'})):
                # product has sizes
                sizeDiv = product.find('select', attrs={'id': 'pa_size'}).findAll('option')[1:]
                for _size in sizeDiv:
                    if (_size):
                        # print('size => ', _size.text.strip())
                        sizes.append(_size.text.strip())

            dataObject = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                'name': title,
                'pictures': [imageURL],
                'stock': 'N/A',
                'price': price,
                'discount': 0,
                'salePrice': 0,
                'description': '',
                'tags': [gender, brandName],
                'rating': random.choice(list(range(3, 5))),
                'category': gender,
                'colors': colors,
                'size': sizes,
                'buyUrl': buy_url,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'edenrobe'
            }
            if(sizes.__len__() == 0 ):
                goToProductDetail(dataObject,buy_url)
            else:
                print('data__', dataObject)
                mydb.freshProducts.insert_one(dataObject)
            print('...........................................................................................')
    else:
        print('no products on this page')
##get all links

def getAllLinks(_url):
    driver.get(_url)
    soup = BeautifulSoup(driver.page_source,'lxml')
    womenUls = soup.select('ul[class*="ubermenu-submenu ubermenu"]')[0:3]
    menULs = soup.select('ul[class*="ubermenu-submenu ubermenu"]')[3:9]
    kidsULs = soup.select('ul[class*="ubermenu-submenu ubermenu"]')[10:15]

    for menUl in menULs:
        for brand in menUl:
            if(brand.find('a') != -1):
                menBrands.append({'url':  brand.find('a')['href'],'name': brand.find('a').text.strip()})
    for womenUl in womenUls:
        for brand in womenUl:
            if (brand.find('a') != -1):
                womenBrands.append({'url': brand.find('a')['href'],'name': brand.find('a').text.strip()})
    for kidsUL in kidsULs:
        for brand in kidsUL:
            if(brand.find('a') != -1):
                kidsBrands.append({'url':  brand.find('a')['href'],'name': brand.find('a').text.strip()})
    print('womenBrands = ', womenBrands)
    print('menBrands = ', menBrands)
    print('kidsBrands = ', kidsBrands)

    driver.close()

# #start point for getting all the links for men,women,kids brands urls and brand names
# try:
#     scrapeUrl = "https://edenrobe.com"
#     getAllLinks(scrapeUrl)
# except Exception as el:
#     print("Error opening site  ", el)
#     driver.close()


# starting point for scrapping all the data
print('starting scrapping')
try:
    allBrands = [ {'blist':womenBrands, 'name': 'women'},{'blist':menBrands, 'name': 'men'} ,{'blist':kidsBrands, 'name': 'kids'},]
    for brand in allBrands:
       openSitePage(brand['blist'], brand['name'])
except Exception as el:
    print("Exception occured ", el)
    driver.close()

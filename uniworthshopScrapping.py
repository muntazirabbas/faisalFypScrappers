import random
from datetime import date,datetime
from bs4 import BeautifulSoup
import pymongo
from selenium import webdriver
myclient       = pymongo.MongoClient("mongodb://localhost:27017/")
mydb           = myclient["fypDb"]
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
menBrands = [
    {'url': 'https://uniworthshop.com/collections/regular-fit-plain-shirts?limit=48', 'name': 'Regular Fit'},
             {'url': 'https://uniworthshop.com/collections/tuxedo-shirt', 'name': 'Tuxedo Fit'},
             {'url': 'https://uniworthshop.com/collections/check-shirt-regular-fit', 'name': 'Regular Fit'},
             {'url': 'https://uniworthshop.com/collections/check-shirt-smart-fit', 'name': 'Smart Fit'},
             {'url': 'https://uniworthshop.com/collections/smart-fit-stripe-shirts', 'name': 'Smart Fit'},
             {'url': 'https://uniworthshop.com/collections/polo-t-shirts', 'name': 'POLO T-SHIRTS'},
             {'url': 'https://uniworthshop.com/collections/crew-neck-t-shirts', 'name': 'CREW NECK T-SHIRTS'},
             {'url': 'https://uniworthshop.com/collections/full-sleeve', 'name': 'FULL SLEEVES'}, {'url': 'https://uniworthshop.com/collections/half-sleeve', 'name': 'HALF SLEEVES'}, {'url': 'https://uniworthshop.com/collections/full-sleeve-basic-tees', 'name': 'FULL SLEEVE BASIC TEES'}, {'url': 'https://uniworthshop.com/collections/half-sleeve-basic-tees', 'name': 'HALF SLEEVE BASIC TEES'}, {'url': 'https://uniworthshop.com/collections/classic-fit', 'name': 'Classic Fit'}, {'url': 'https://uniworthshop.com/collections/smart-fit', 'name': 'Smart Fit'}, {'url': 'https://uniworthshop.com/collections/regular-ties', 'name': 'REGULAR TIES'}, {'url': 'https://uniworthshop.com/collections/slim-ties', 'name': 'SLIM TIES'}, {'url': 'https://uniworthshop.com/collections/bow-tie', 'name': 'BOW TIE SET'}, {'url': 'https://uniworthshop.com/collections/pin-buckle', 'name': 'PIN BUCKLES'}, {'url': 'https://uniworthshop.com/collections/fancy-buckle', 'name': 'FANCY BUCKLES'}, {'url': 'https://uniworthshop.com/collections/casual-belt', 'name': 'CASUAL BELT'}, ]


#This site has only men's brands products

def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    # print('product url ', productUrl)
    driver.get(productUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # print("detail soup ",soup)
    sizeDiv = soup.findAll('select', attrs={'class' : 'required-entry super-attribute-select'})[0].findAll('option')[1:]
    colorRows = soup.find('div', attrs={'class' : 'ui-tabs-panel ui-widget-content ui-corner-bottom'}).findAll('tr')
    price = soup.find('span', attrs={'class': 'price'}).text.strip()[4:]
    # print('price__',price)
    pictures = []
    colors = []
    size = []


    for colorRow in colorRows:
        # print('colorRow ', colorRow)
        if(colorRow.find('td').text.strip().lower() == 'colour'):
            # print('color => ',colorRow.findAll('td')[1].text.strip().lower())
            colors.append(colorRow.findAll('td')[1].text.strip().lower())
    _productData['colors'] = colors
    _productData['size'] = size
    # _productData['pictures'] = pictures
    _productData['price'] = price
    print('product data ', _productData)

def openSitePage(brandData, type):
    for sitePage in brandData:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],type)

jsonData = []
def processSitePageSoup(soup, brandName,gender):
    webUrl = "https://www.uniworthshop.com"
    products = soup.findAll('div', attrs={'class': 'spf-col-xl-4 spf-col-lg-4 spf-col-md-6 spf-col-sm-6 spf-col-6'})
    # print('products ', products)
    for product in products:
        if(product):
            # print("product======>>>>")
            productInfo = product.find('div', attrs={'class': 'spf-product__info'})
            title = productInfo.find('a').text.strip()
            price = 0
            buyUrl = "https://uniworthshop.com/" + productInfo.find('a')['href'].strip()

            _image = product.find('img', attrs={'class': 'gflazyload spf-product-card__image spf-product-card__image-hidden'})['src']
            if (productInfo.find('div', attrs={'class':'spf-product-card__price-wrapper'})):
                # print('in price div')
                priceCount = len(productInfo.find('div', attrs={'class':'spf-product-card__price-wrapper'}).findAll('span'))
                if(priceCount > 1):
                    price = productInfo.find('div', attrs={'class':'spf-product-card__price-wrapper'}).findAll('span')[1].text.strip()[3:]
                else:
                    price = productInfo.find('div', attrs={'class':'spf-product-card__price-wrapper'}).findAll('span')[0].text.strip()[3:]
            else:
                print('no price detail')
            colors = []
            if(product.find('select', attrs={'class': 'spf-product__variants'})):
                colordDiv = product.find('select', attrs={'class': 'spf-product__variants'}).find('option').text
                color = colordDiv.split('/')[0].lower().strip()
                colors = [color]
            sizes = []
            if(product.find('select', attrs={'class': 'spf-product__variants'})):
                sizeDiv = product.find('select', attrs={'class': 'spf-product__variants'}).findAll('option')
                for _size in sizeDiv:
                    if (_size):
                        # print('size => ',_size.text)
                        sizes.append(_size.text.lower().split('/')[1].strip())

            dataObject = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                'name': title,
                'price': price,
                'pictures': [_image],
                'stock': 'N/A',
                'discount': 0,
                'salePrice': 0,
                'description': '',
                'tags': [gender, brandName],
                'rating': 'N/A',
                'category': gender,
                'colors': colors,
                'size': sizes,
                'buyUrl': buyUrl,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'uniworthshop'
            }
            print('data_____',dataObject)
            mydb.freshProducts.insert_one(dataObject)
            # print('...........................................................................................')

print('starting scrapping')

def getAllLinks(scrapeUrl):
    domainName = "https://www.uniworthshop.com"
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source,'lxml')
    for brand in soup.findAll('a', {'class': 'menu-elemts-hover-ib-2'}):
            print("brand_", brand)
            if(brand != -1):
                print(brand['href'])
                print(brand.text.strip())
                menBrands.append(
                        {
                            'url': brand['href'],
                            'name': brand.text.strip()
                        })
            print('........................................................................')

    driver.close()
    print('menBrands = ', menBrands)

#start point for scrapping all the data
def scrapProducts():
    try:
        openSitePage(menBrands, 'men')
    except Exception as el:
        print("Exception occured ", el)
        driver.close()

try:
    scrapProducts()
    # scrapeUrl = "https://www.uniworthshop.com"
    # getAllLinks(scrapeUrl)
except Exception as el:
    print("Exception occured ", el)
    driver.close()

import random
from datetime import date,datetime
from bs4 import BeautifulSoup
import pymongo
from selenium import webdriver
import time
myclient       = pymongo.MongoClient("mongodb://localhost:27017/")
mydb           = myclient["fypDb"]
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome("C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe",chrome_options=chrome_options)
# driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
menBrands = [
    # {
    #     'url': 'https://uniworthshop.com/collections/plain-shirts',
    #     'name': 'Plain Shirt'
    # },
    # {
    #     'url': 'https://uniworthshop.com/collections/check-shirt',
    #     'name': 'Check Shirt'
    # },
    # {
    #     'url': 'https://uniworthshop.com/collections/stripe-shirt',
    #     'name': 'Stripe Shirt'
    # },
    # {
    #     'url': 'https://uniworthshop.com/collections/button-down',
    #     'name': 'Button Down'
    # },
    # {
    #     'url': 'https://uniworthshop.com/collections/double-cuff',
    #     'name': 'Double Cuff'
    # },
    # {
    #     'url': 'https://uniworthshop.com/collections/designer-shirt',
    #     'name': 'Designer Shirt'
    # },
    # {
    #     'url': 'https://uniworthshop.com/collections/half-sleeve-shirt',
    #     'name': 'Half sleeve Shirt'
    # },
    # {
    #     'url': 'https://uniworthshop.com/collections/printed-shirt',
    #     'name': 'Printed Shirt'
    # },
    # {
    #     'url': 'https://uniworthshop.com/collections/tuxedo-shirt',
    #     'name': 'Tuxedo Shirt'
    # },
    {
        'url': 'https://uniworthshop.com/collections/t-shirt',
        'name': 'T-Shirts'
    },
    {
        'url': 'https://uniworthshop.com/collections/casual-shirt',
        'name': 'Casual Shirts'
    },
    {
        'url': 'https://uniworthshop.com/collections/basic-tees',
        'name': 'Basic Tees'
    },
    {
        'url': 'https://uniworthshop.com/collections/pajamas',
        'name': 'Pajamas'
    },
    {
        'url': 'https://uniworthshop.com/collections/t-shirt-pajama-set',
        'name': 'T-Shirt & Pajama Set'
    },
    {
        'url': 'https://uniworthshop.com/collections/men-shorts',
        'name': 'Mens Shorts'
    },
    {
        'url': 'https://uniworthshop.com/collections/formal-trousers',
        'name': 'Formal Trousers'
    },
    {
        'url': 'https://uniworthshop.com/collections/denim-jeans',
        'name': 'Denim Jeans'
    },
    {
        'url': 'https://uniworthshop.com/collections/mens-chinos',
        'name': 'Mens Chinos'
    },
    {
        'url': 'https://uniworthshop.com/collections/cargo-trousers',
        'name': 'Cargo Trousers'
    },
    {
        'url': 'https://uniworthshop.com/collections/cotton-trousers',
        'name': 'COTTON TROUSERS'
    },
    {
        'url': 'https://uniworthshop.com/collections/shalwar-suit',
        'name': 'Shalwar Suit'
    },
    {
        'url': 'https://uniworthshop.com/collections/kurtas',
        'name': 'Kurtas'
    },
    {
        'url': 'https://uniworthshop.com/collections/shalwar',
        'name': 'Shalwar'
    },
    {
        'url': 'https://uniworthshop.com/collections/men-s-waistcoats',
        'name': 'Waistcoats'
    },
    {
        'url': 'https://uniworthshop.com/collections/peshawari-chappal',
        'name': 'Peshawari Chappal'
    },
    {
        'url': 'https://uniworthshop.com/collections/loose-fabric',
        'name': 'Fabric'
    },
    {
        'url': 'https://uniworthshop.com/collections/suiting',
        'name': 'Suiting'
    },
    {
        'url': 'https://uniworthshop.com/collections/gift-box',
        'name': 'Gift Box'
    },
    {
        'url': 'https://uniworthshop.com/collections/pocket-square',
        'name': 'Pocket Square'
    },
    {
        'url': 'https://uniworthshop.com/collections/tiepin',
        'name': 'Tie Pin'
    },
    {
        'url': 'https://uniworthshop.com/collections/track-suit',
        'name': 'Track Suits'
    },

]

#This site has only men's brands products

def openSitePage(brandData, type):
    for sitePage in brandData:
        sitePageUrl = sitePage['url']+"?limit=24"
        print('sitePage ', sitePageUrl)
        driver.get(sitePageUrl)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],type)

jsonData = []
def processSitePageSoup(soup, brandName,gender):
    webUrl = "https://www.uniworthshop.com"
    products = soup.findAll('div', attrs={'class': 'spf-col-xl-4 spf-col-lg-4 spf-col-md-6 spf-col-sm-6 spf-col-6'})[0:20]
    # print('products ', products)
    for product in products:
        if(product):
            # print("product======>>>>")
            productInfo = product.find('div', attrs={'class': 'spf-product__info'})
            title = productInfo.find('a').text.strip()
            # print('title ', title)
            price = 0
            buyUrl = "https://uniworthshop.com/" + productInfo.find('a')['href'].strip()
            # print('buy url ', buyUrl)
            # _image = product.find('img', attrs={'class': 'gflazyload spf-product-card__image spf-product-card__image-hidden'})['src']
            _image = product.find('img')['src']
            print('img ', _image)
            if (productInfo.find('div', attrs={'class':'spf-product-card__price-wrapper'})):
                print('in price div')
                priceCount = len(productInfo.find('div', attrs={'class':'spf-product-card__price-wrapper'}).findAll('span'))
                if(priceCount > 1):
                    price = productInfo.find('div', attrs={'class':'spf-product-card__price-wrapper'}).findAll('span')[1].text.strip()[3:]
                else:
                    price = productInfo.find('div', attrs={'class':'spf-product-card__price-wrapper'}).findAll('span')[0].text.strip()[3:]
            else:
                price = 0
                print('no price detail')
            print('price ', price)
            colors = []
            sizes = []
            if(product.find('select', attrs={'class': 'spf-product__variants'})):
                colordDiv = product.find('select', attrs={'class': 'spf-product__variants'}).find('option').text
                if('/' in colordDiv):
                    color = colordDiv.split('/')[0].lower().strip()
                    colors = [color]
                    print('colors ', colors)
                    sizeDiv = product.find('select', attrs={'class': 'spf-product__variants'}).findAll('option')
                    for _size in sizeDiv:
                        if (_size):
                            # print('size => ',_size.text)
                            sizes.append(_size.text.lower().split('/')[1].strip())
            print('sizes ', sizes)
            price = float(price.replace(',',''))
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
            # dbProducts = mydb.freshProducts.find({'mainBrand': 'uniworthshop'})
            # if (any((dbProd['pictures'] == dataObject['pictures'] and dbProd['buyUrl'] == dataObject['buyUrl']) for
            #         dbProd in dbProducts)):
            #     print('product exists ')
            # else:
            #     # insert new product
            #     print('inerting new document')

            print('...........................................................................................')

print('starting scrapping')

def getAllLinks():
    scrapeUrl = "https://www.uniworthshop.com"
    domainName = "https://www.uniworthshop.com"
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source,'lxml')
    for brand in soup.findAll('a', {'class': 'menu-elemts-hover-ib'}):
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

try:
    openSitePage(menBrands, 'men')
    # getAllLinks()
except Exception as el:
    print("Exception occured ", el)
    driver.close()

import random
from datetime import datetime
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
menBrands = [
            {'url': 'https://diners.com.pk/collections/shirts', 'name': 'Shirts'},
             {'url': 'https://diners.com.pk/collections/trousers', 'name': 'Trousers'},
             {'url': 'https://diners.com.pk/collections/suiting-blazers', 'name': 'Blazzers'},
             {'url': 'https://diners.com.pk/collections/t-shirts', 'name': 'T-Shirts'},
]

womenBrands = [{'url': 'https://diners.com.pk/collections/ready-to-wear', 'name': 'Ready to Wear'},
               {'url': 'https://diners.com.pk/collections/unstitched', 'name': 'Unstitched'},
               {'url': 'https://diners.com.pk/collections/sohaye-trousers', 'name': 'Bottoms'},
               ]
kidsBrands =[
    {'url': 'https://diners.com.pk/collections/boys', 'name': 'Mix'},
    {'url': 'https://diners.com.pk/collections/girls', 'name': 'Mix'},

]


def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    print('product url ', productUrl)
    driver.get(productUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # print("detail soup ",soup)
    sizeDiv = soup.findAll('select', attrs={'class' : 'single-option-selector single-option-selector-product-template product-form__input'})[0].findAll('option')
    colorDiv = soup.findAll('select', attrs={'class' : 'single-option-selector single-option-selector-product-template product-form__input'})[1].findAll('option')
    price = soup.find('span', attrs={'class': 'product-single__price'}).text.strip()[3:-3]
    print('price__',price)
    pictures = []
    colors = []
    size = []

    for _size in sizeDiv:
        if(_size):
            # print('size => ',_size.text)
            size.append(_size.text)
    for color in colorDiv:
        if(color):
            # print('color => ',color['title'])
            colors.append(color.text.strip().lower())
    if(soup.find('div', attrs={'class': 'photos'}).findAll('img'))[1:]:
        pictureDiv = soup.find('div', attrs={'class': 'photos'}).findAll('img')[1:]
        for pic in pictureDiv:
            if (pic):
                # print('pic____',pic['src'])
                pictures.append("https:"+pic['src'])

    _productData['colors'] = colors
    _productData['size'] = size
    _productData['pictures'] = pictures
    _productData['price'] = price
    print('product data ', _productData)
    print('................................................................................................')


def openSitePage(brandData, type):
    for sitePage in brandData:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],type)

jsonData = []
def processSitePageSoup(soup, brandName,gender):
    webUrl = "https://diners.com.pk/"
    products = soup.findAll('div', attrs={'class': 'grid-item col-6 col-md-4'})
    # print('products ', products)
    for product in products:
        if(product):
            # print("product======>>>>",product)
            title = product.find('a',{'class' : 'product-title'}).text.strip()
            # print('title ', title)
            buyUrl =  webUrl + product.find('a',{'class' : 'product-title'})['href']
            # print('b-url ', buyUrl)

            price = 0
            if(product.findAll('span', attrs={'class' : 'money'})):
                price = product.findAll('span', attrs={'class': 'money'})[-1].text.strip()[3:]
            imageUrl = ''
            if(product.find('img')['data-srcset']):
                imageUrl = 'https:' + product.find('img')['data-srcset']
            # print('image ', imageUrl)
            sizes = []
            if(product.find('ul' , attrs={'class' : 'sizes-list'})):
                for _size in product.find('ul' , attrs={'class' : 'sizes-list'}).findAll('li'):
                    sizes.append(_size.text.strip())
            dataObject = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                'name': title,
                'price': price,
                'pictures': [imageUrl],
                'stock': 'N/A',
                'discount': 0,
                'salePrice': 0,
                'description': '',
                'tags': [gender, brandName],
                'rating': 'N/A',
                'category': gender,
                'colors': [],
                'size': sizes,
                'buyUrl': buyUrl,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'diners'
            }
            # print('data_____',dataObject)
            # mydb.freshProducts.insert_one(dataObject)
print("starting scrapping")

def getAllLinks(scrapeUrl):
    webUrl = "https://diners.com.pk/"
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source,'lxml')
    menSoup = soup.findAll('li', attrs={'class': 'drawer__nav-item'})[2:12]
    womenSoup = soup.findAll('li', attrs={'class': 'drawer__nav-item'})[14:25]
    kidsSoup = soup.findAll('li', attrs={'class': 'drawer__nav-item'})[27:33]

    for brand in menSoup:
        # print("brand_", brand)
        if(brand.find('a') != -1):
            print(brand.find('a')['href'])
            print(brand.find('a').text.strip())
            menBrands.append(
                        {
                            'url': webUrl + brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
        print('........................................................................')
    for brand in womenSoup:
        # print("brand_", brand)
        if(brand.find('a') != -1):
            print(brand.find('a')['href'])
            print(brand.find('a').text.strip())
            womenBrands.append(
                        {
                            'url': webUrl + brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
        print('........................................................................')
    for brand in kidsSoup:
        # print("brand_", brand)
        if(brand.find('a') != -1):
            print(brand.find('a')['href'])
            print(brand.find('a').text.strip())
            kidsBrands.append(
                        {
                            'url': webUrl + brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
        print('........................................................................')
    driver.close()
    print('menBrands ', menBrands)
    print('womenBrands ', womenBrands)
    print('kidsBrands ', kidsBrands)

def startScrapping():
    # start point for scrapping all the data
    try:
        allBrands = [{'blist': kidsBrands, 'name': 'kids'}, {'blist': womenBrands, 'name': 'women'},
                     {'blist': menBrands, 'name': 'men'}]
        for brand in allBrands:
            openSitePage(brand['blist'], brand['name'])
    except Exception as el:
        print("Exception occured ", el)
        driver.close()

##start point for getting all the links for men,women,kids brands urls and brand names

try:
    scrapeUrl = "https://diners.com.pk/collections/girls"
    # getAllLinks(scrapeUrl)
    startScrapping()
    # _products = mydb.get_collection('products').find()
    # for prod in _products:
    #     print('database products ', prod)
except Exception as el:
    print("Error opening site  ", el)
    driver.close()

driver.close()
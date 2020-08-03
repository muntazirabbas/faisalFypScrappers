import random
from datetime import datetime
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
# dbProducts = mydb.testCollection.find()

# for prod in dbProducts:
#     print('prod ', prod)

from selenium import webdriver
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome("C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe",chrome_options=chrome_options)
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
menBrands = [
            {'url': 'https://www.engine.com.pk/collections/men-casual-shirts', 'name': 'Shirts'},
             {'url': 'https://www.engine.com.pk/collections/men-t-shirts', 'name': 'T-Shirts'},
            {'url': 'https://www.engine.com.pk/collections/men-polo-shirts', 'name': 'Polo Shirts'},
             {'url': 'https://www.engine.com.pk/collections/men-jeans', 'name': 'Jeans'},
             {'url': 'https://www.engine.com.pk/collections/men-pants', 'name': 'Pants'},
             {'url': 'https://www.engine.com.pk/collections/men-trousers', 'name': 'Trousers'},
             {'url': 'https://www.engine.com.pk/collections/men-hoodies-sweatshirts', 'name': 'Hoodies & Sweatshirts'}, {'url': 'https://www.engine.com.pk/collections/men-sweaters', 'name': 'Sweaters'}, {'url': 'https://www.engine.com.pk/collections/men-jackets', 'name': 'Jackets'}, {'url': 'https://www.engine.com.pk/collections/men-glasses', 'name': 'Glasses'}, {'url': 'https://www.engine.com.pk/collections/men-footwear', 'name': 'Footwear'}
    ]
womenBrands = [{'url': 'https://www.engine.com.pk/collections/women-shirts-blouses', 'name': 'Knit Tops'}, {'url': 'https://www.engine.com.pk/collections/woven-top', 'name': 'Woven Tops'}, {'url': 'https://www.engine.com.pk/collections/women-bottoms', 'name': 'Jeans'}, {'url': 'https://www.engine.com.pk/collections/women-pants', 'name': 'Pants'}, {'url': 'https://www.engine.com.pk/collections/women-trousers', 'name': 'Trousers'}, {'url': 'https://www.engine.com.pk/collections/women-tights', 'name': 'Tights'}, {'url': 'https://www.engine.com.pk/collections/women-footwear', 'name': 'shoes'}]
kidsBrands = [{'url': 'https://www.engine.com.pk/collections/t-shirt', 'name': 'T-Shirts'}, {'url': 'https://www.engine.com.pk/collections/casual-shirt', 'name': 'Shirts'}, {'url': 'https://www.engine.com.pk/collections/boys-bottom', 'name': 'Jeans'}, {'url': 'https://www.engine.com.pk/collections/boys-pants', 'name': 'Pants'}, {'url': 'https://www.engine.com.pk/collections/boys-trousers', 'name': 'Trousers'}, {'url': 'https://www.engine.com.pk/collections/boys-shorts', 'name': 'Shorts'}, {'url': 'https://www.engine.com.pk/collections/girls-knit-top', 'name': 'Knit Tops'}, {'url': 'https://www.engine.com.pk/collections/woven-top-1', 'name': 'Woven Tops'}, {'url': 'https://www.engine.com.pk/collections/girls-bottom', 'name': 'Jeans'}, {'url': 'https://www.engine.com.pk/collections/girls-pants', 'name': 'Pants'}, {'url': 'https://www.engine.com.pk/collections/girls-trousers', 'name': 'Trousers'}, {'url': 'https://www.engine.com.pk/collections/girls-tights', 'name': 'Tights'}]


def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    print('product url ', productUrl)
    driver.get(productUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # print("detail soup ",soup)

    sizeDiv = []
    selectCount = len(soup.findAll('select', attrs={'class': 'single-option-selector single-option-selector-product-template product-form__input'}))
    if(soup.findAll('select', attrs={'class' : 'single-option-selector single-option-selector-product-template product-form__input'})[0]):
        # print('in size div')
        sizeDiv = soup.findAll('select', attrs={'class' : 'single-option-selector single-option-selector-product-template product-form__input'})[0].findAll('option')
    colorDiv = []
    # print('select count ', selectCount)
    if(selectCount > 1):
        # print('in count > 1')
        if(soup.findAll('select', attrs={'class' : 'single-option-selector single-option-selector-product-template product-form__input'})[1]):
            print('in color div')
            colorDiv = soup.findAll('select', attrs={'class' : 'single-option-selector single-option-selector-product-template product-form__input'})[1].findAll('option')
    price = float(soup.find('span', attrs={'class': 'product-single__price'}).text.strip()[3:].replace(',',''))
    # print('price__',price)
    pictures = []
    colors = []
    size = []

    for _size in sizeDiv:
        if(_size):
            # print('size => ',_size.text)
            size.append(_size.text.lower())
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
    mydb.freshProducts.insert_one(_productData)
    # print(doc._id)
    print('................................................................................................')


def openSitePage(brandData, type):
    for sitePage in brandData:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],type)

jsonData = []
def processSitePageSoup(soup, brandName,gender):
    webUrl = "https://www.engine.com.pk"
    products = soup.findAll('div', attrs={'class': 'grid__item small--one-half medium-up--one-fifth'})
    # print('products ', products)
    for product in products:
        if(product):
            # print("product======>>>>",product)
            title = product.find('div',{'class':'product-card__name'}).text.strip()
            buyUrl = webUrl + product.findAll('a')[0]['href']

            dataObject = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                'name': title,
                'price': 0,
                'pictures': [],
                'stock': 'N/A',
                'discount': 0,
                'salePrice': 0,
                'description': '',
                'tags': [gender, brandName],
                'rating': 'N/A',
                'category': gender,
                'colors': [],
                'size': [],
                'buyUrl': buyUrl,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'engine'
            }
            # print('data_____',dataObject)
            goToProductDetail(dataObject,buyUrl)

print('starting scrapping')

def getAllLinks(scrapeUrl):
    webUrl = "https://www.engine.com.pk"
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source,'lxml')
    # menSoup = soup.findAll('li', attrs={'class': 'drawer__nav-item'})[2:12]
    # womenSoup = soup.findAll('li', attrs={'class': 'drawer__nav-item'})[14:25]
    kidsBoysSoup = soup.findAll('ul', attrs={'class': 'meganav__list meganav__list--gutter'})[2].findAll("li")
    # print('kboys ', kidsBoysSoup)
    kidsGirlsSoup = soup.findAll('ul', attrs={'class': 'meganav__list meganav__list--gutter'})[5].findAll("li")
    # print('kgirls ', kidsGirlsSoup)
    kidsSoup = kidsBoysSoup + kidsGirlsSoup

    # for brand in menSoup:
    #     # print("brand_", brand)
    #     if(brand.find('a') != -1):
    #         print(brand.find('a')['href'])
    #         print(brand.find('a').text.strip())
    #         menBrands.append(
    #                     {
    #                         'url': webUrl + brand.find('a')['href'],
    #                         'name': brand.find('a').text.strip()
    #                     })
    #     print('........................................................................')
    # for brand in womenSoup:
    #     # print("brand_", brand)
    #     if(brand.find('a') != -1):
    #         print(brand.find('a')['href'])
    #         print(brand.find('a').text.strip())
    #         womenBrands.append(
    #                     {
    #                         'url': webUrl + brand.find('a')['href'],
    #                         'name': brand.find('a').text.strip()
    #                     })
    #     print('........................................................................')
    print('kidsSoup ', kidsSoup)
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
    # print('menBrands ', menBrands)
    # print('womenBrands ', womenBrands)
    print('kidsBrands ', kidsBrands)


##start point for getting all the links for men,women,kids brands urls and brand names
#
# try:
#     scrapeUrl = "https://www.engine.com.pk/"
#     getAllLinks(scrapeUrl)
# except Exception as el:
#     print("Error opening site  ", el)
#     driver.close()


#start point for scrapping all the data
try:
    allBrands = [
        {'blist': kidsBrands, 'name': 'kids'},
        # {'blist': womenBrands, 'name': 'women'},
        # {'blist': menBrands, 'name': 'men'}
    ]
    for brand in allBrands:
       openSitePage(brand['blist'], brand['name'])
except Exception as el:
    print("Exception occured ", el)
    driver.close()

driver.close()
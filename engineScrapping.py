import random
from datetime import datetime
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
menBrands = [{'url': 'https://www.engine.com.pk/collections/men-casual-shirts', 'name': 'Shirts'}, {'url': 'https://www.engine.com.pk/collections/men-t-shirts', 'name': 'T-Shirts'}, {'url': 'https://www.engine.com.pk/collections/men-jeans', 'name': 'Jeans'}, {'url': 'https://www.engine.com.pk/collections/men-pants', 'name': 'Pants'}, {'url': 'https://www.engine.com.pk/collections/men-trousers', 'name': 'Trousers'}, {'url': 'https://www.engine.com.pk/collections/men-hoodies-sweatshirts', 'name': 'Hoodies & Sweatshirts'}, {'url': 'https://www.engine.com.pk/collections/men-sweaters', 'name': 'Sweaters'}, {'url': 'https://www.engine.com.pk/collections/men-jackets', 'name': 'Jackets'}, {'url': 'https://www.engine.com.pk/collections/men-glasses', 'name': 'Glasses'}, {'url': 'https://www.engine.com.pk/collections/men-footwear', 'name': 'Footwear'}]
womenBrands = [{'url': 'https://www.engine.com.pk/collections/woven-top', 'name': 'Woven Tops'}, {'url': 'https://www.engine.com.pk/collections/women-kurties', 'name': 'Kurties'}, {'url': 'https://www.engine.com.pk/collections/women-bottoms', 'name': 'Jeans'}, {'url': 'https://www.engine.com.pk/collections/women-pants', 'name': 'Pants'}, {'url': 'https://www.engine.com.pk/collections/women-trousers', 'name': 'Trousers'}, {'url': 'https://www.engine.com.pk/collections/women-tights', 'name': 'Tights'}, {'url': 'https://www.engine.com.pk/collections/women-hoodies-sweatshirts', 'name': 'Hoodies & Sweatshirts'}, {'url': 'https://www.engine.com.pk/collections/women-sweaters', 'name': 'Sweaters'}, {'url': 'https://www.engine.com.pk/collections/ladies-jacket', 'name': 'Jackets'}, {'url': 'https://www.engine.com.pk/collections/women-sleepwear', 'name': 'Sleepwear'}, {'url': 'https://www.engine.com.pk/collections/women-footwear', 'name': 'Footwear'}]
kidsBrands =[{'url': 'https://www.engine.com.pk/collections/t-shirt', 'name': 'T-Shirts'}, {'url': 'https://www.engine.com.pk/collections/boys-bottom', 'name': 'Jeans'}, {'url': 'https://www.engine.com.pk/collections/boys-pants', 'name': 'Pants'}, {'url': 'https://www.engine.com.pk/collections/boys-trousers', 'name': 'Trousers'}, {'url': 'https://www.engine.com.pk/collections/boys-shorts', 'name': 'Shorts'}, {'url': 'https://www.engine.com.pk/collections/boys-hoodies-sweatshirts', 'name': 'Hoodies & Sweatshirts'}]




def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    print('product url ', productUrl)
    driver.get(productUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # print("detail soup ",soup)
    sizeDiv = soup.findAll('select', attrs={'class' : 'single-option-selector single-option-selector-product-template product-form__input'})[0].findAll('option')
    colorDiv = soup.findAll('select', attrs={'class' : 'single-option-selector single-option-selector-product-template product-form__input'})[1].findAll('option')
    priceText = soup.find('span', attrs={'class': 'product-single__price'}).text

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
            colors.append(color.text)
    if(soup.find('div', attrs={'class': 'photos'}).findAll('img'))[1:]:
        pictureDiv = soup.find('div', attrs={'class': 'photos'}).findAll('img')[1:]
        for pic in pictureDiv:
            if (pic):
                # print('pic____',pic['src'])
                pictures.append("https:"+pic['src'])

    _productData['colors'] = colors
    _productData['size'] = size
    _productData['pictures'] = pictures
    print('product data ', _productData)
    # print("sizeDiv ______________", sizeDiv)
    # print("colorDiv______________", colorDiv)
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
                'pictures': [],
                'stock': 'N/A',
                'price': 0,
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
            # if(dataObject['pictures'][0] != ""):
            #     mydb.products.insert_one(dataObject)
            goToProductDetail(dataObject,buyUrl)
            print('...........................................................................................')

print('starting scrapping')

def getAllLinks(scrapeUrl):
    webUrl = "https://www.engine.com.pk"
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


##start point for getting all the links for men,women,kids brands urls and brand names

# try:
#     scrapeUrl = "https://www.engine.com.pk/collections/men"
#     getAllLinks(scrapeUrl)
# except Exception as el:
#     print("Error opening site  ", el)
#     driver.close()


#start point for scrapping all the data
try:
    openSitePage(menBrands, 'kids')
except Exception as el:
    print("Exception occured ", el)
    driver.close()

driver.close()
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
            price = 0
            if (product.find('s',{'class':'product-card__regular-price'})):
                price = product.find('s',{'class':'product-card__regular-price'}).text.strip()[3:].replace(',', '')
            imageUrl = ""
            # print('img-src_____ ',product.find('img'))
            try:
                if(product.find('img')['data-srcset']):
                    imageUrl = "https:" + product.find('img')['data-srcset'].rsplit(',', 1)[1].strip().replace(" ", "")
                elif(product.find('img')['data-src']):
                    imageUrl = "https:" + product.find('img')['data-src'].rsplit(',', 1)[1].strip().replace(" ", "")
                else:
                    imageUrl = ""
            except Exception as el:
                print("")

            print('imageUri ', imageUrl)
            # print("Type = ", gender)
            # print("Brand = ", brandName)
            # print("Title = ", title)
            # print("Buy URL = ", buyUrl)
            print("Price = ", price)
            colors = ["black", "gray", "red", "pink", "white", "green", "blue"]
            size = random.choice(
                [
                    ['100 CM', '90 CM', '95 CM'],
                    ['M', 'L', 'XL'],
                    ['XS', 'S', '2T'],
                    ['3T', '4T', '7'],
                    ['8', '9']
                ])
            mainBrands = ['bonanza', 'outfitters', 'breakout', 'khaadi', 'engine', 'gulahmed']
            dataObject = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(
                    list(range(55, 5000))),
                'name': title,
                'pictures': [imageUrl],
                'stock': random.choice(list(range(10, 400))),
                'price': int(price),
                'discount': random.choice(list(range(0, 100))),
                'salePrice': int(price) + random.choice([0, 300]),
                'description': '',
                'tags': [gender, brandName],
                'rating': random.choice(list(range(0, 5))),
                'category': gender,
                'colors': [random.choice(colors), random.choice(colors), random.choice(colors)],
                'size': size,
                'buyUrl': buyUrl,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'engine'
            }
            print('data_____',dataObject)
            if(dataObject['pictures'][0] != ""):
                mydb.products.insert_one(dataObject)
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
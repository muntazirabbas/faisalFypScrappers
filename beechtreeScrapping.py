from bs4 import BeautifulSoup
import random
from datetime import datetime
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
from fake_useragent import UserAgent
ua = UserAgent()
header = {'user-agent':ua.chrome}
from selenium import  webdriver
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver2 = webdriver.Chrome("C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe",chrome_options=chrome_options)
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
womenBrands = [
    {'url': 'https://www.beechtree.pk/pk/pret/signature-pret.html', 'name': 'Signature Pret'},
    {'url': 'https://www.beechtree.pk/pk/pret/embroidered-shirts.html', 'name': 'Embroidered'},
    {'url': 'https://www.beechtree.pk/pk/pret/printed-shirts.html', 'name': 'Printed'},
    {'url': 'https://www.beechtree.pk/pk/pret/solids.html', 'name': 'Solids'},
    {'url': 'https://www.beechtree.pk/pk/pret/pants.html', 'name': 'Pants'},
    {'url': 'https://www.beechtree.pk/pk/luxpret-festive-edition/silk-tunics-shirt.html', 'name': 'Silk Tunics'},
    {'url': 'https://www.beechtree.pk/pk/luxpret-festive-edition/embroidered-shirt.html', 'name': 'Embroidered'},
    {'url': 'https://www.beechtree.pk/pk/luxpret-festive-edition/pants.html', 'name': 'Pants'},
    {'url': 'https://www.beechtree.pk/pk/unstitched/eid-edition-ii.html', 'name': 'Eid Edition-II'},
    {'url': 'https://www.beechtree.pk/pk/unstitched/eid-collection.html', 'name': "Summer' 20 Vol-3"},
    {'url': 'https://www.beechtree.pk/pk/absolute/tops.html', 'name': ' TOPS'},
]

def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    print('product url ', productUrl)
    driver2.get(productUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    size = []

    if((soup.find('fieldset', attrs={'class' : 'product-options'}))):
        selectCount = len(soup.find('fieldset', attrs={'class': 'product-options'}).findAll('select'))
        # print('select count ', selectCount)
        if (selectCount == 1):
            sizeDiv = (soup.find('fieldset', attrs={'class' : 'product-options'})).find('select').findAll('option')[1:]
            for _size in sizeDiv:
                if (_size):
                    # print('size => ',_size.text)
                    size.append(_size.text)
    imageUrl = ''
    # if(soup.find('div', attrs={'class': 'product-img-box product-img-box-normal'})):
    #     imageUrl =  soup.find('div', attrs={'class': 'product-img-box product-img-box-normal'}).find('img')['src']
    #     print('image url ', imageUrl)
    _productData['size'] = size
    # _productData['pictures'] = [imageUrl]
    print('product data ', _productData)
    mydb.freshProducts.insert_one(_productData)
    print('................................................................................................')

def processBrands(brandArray, gender):
        for data in brandArray:
            print('site url ', data['url'])
            driver.get(data['url'])
            # time.sleep(5)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            for rowdata in soup.findAll("li", {"class": "item"}):
                if (rowdata != None):
                    buy_url = rowdata.find('a')['href']
                    title = rowdata.find('a')['title']
                    price = float(rowdata.find('span', {'class': 'price'}).text.strip()[4:].replace(',','') )
                    imageUrl = rowdata.find('img')['src']
                    brandName = data['name']
                    dataObject = {
                        "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                        'name': title,
                        'pictures': [imageUrl],
                        'stock': 'N/A',
                        'price': price,
                        'discount': 0,
                        'salePrice': 0,
                        'description': '',
                        'tags': [brandName],
                        'rating': random.choice(list(range(3, 5))),
                        'category': gender,
                        'colors': [],
                        'size': [],
                        'buyUrl': buy_url,
                        'gender': gender,
                        'brand': title,
                        'date': datetime.today(),
                        'mainBrand': 'beechtree'
                    }
                    # print(dataObject)
                    goToProductDetail(dataObject,buy_url)

def ScrapProducts():
        try:
            allBrands = [
                {'blist': womenBrands, 'name': 'women'},
            ]
            for brand in allBrands:
                processBrands(brand['blist'], brand['name'])
        except Exception as el:
            print("Exception occured ", el)
            driver.close()

try:
    ScrapProducts()
except Exception as el:
    print("Exception occured ", el)
    driver.close()

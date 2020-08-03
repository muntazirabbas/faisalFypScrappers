import time
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from fake_useragent import  UserAgent
import random
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
ua = UserAgent()
header = {'user-agent':ua.chrome}
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
womenBrands = [
    {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/festive-collection-2020/1-piece/', 'name': 'Unstitched'},
    {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/festive-collection-2020/2-piece/', 'name': 'Unstitched'},
    {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/festive-collection-2020/3-piece/', 'name': 'Unstitched'},
    {'url': 'https://www.bonanzasatrangi.com/pk/pret/kunbi-pret/1-piece/', 'name': 'Kunbi Pret'},
    {'url': 'https://www.bonanzasatrangi.com/pk/pret/kunbi-pret/2-piece/', 'name': 'Kunbi Pret'},
    {'url': 'https://www.bonanzasatrangi.com/pk/pret/kunbi-pret/3-piece/', 'name': 'Kunbi Pret'},
    {'url': 'https://www.bonanzasatrangi.com/pk/pret/pret/1-piece/', 'name': 'Pret Wear'},
    {'url': 'https://www.bonanzasatrangi.com/pk/pret/pret/2-piece/', 'name': 'Pret Wear'},
    {'url': 'https://www.bonanzasatrangi.com/pk/pret/pret/2-piece/', 'name': 'Pret Wear'},
    {'url': 'https://www.bonanzasatrangi.com/pk/pret/outline-collection/1-piece/', 'name': 'Outline Collection'},
    {'url': 'https://www.bonanzasatrangi.com/pk/pret/teens/1-piece/', 'name': 'Alive'},
    {'url': 'https://www.bonanzasatrangi.com/pk/accessories/dupatta/', 'name': 'Dupatta'},
    {'url': 'https://www.bonanzasatrangi.com/pk/accessories/trouser/', 'name': 'Trouser'},
    {'url': 'https://www.bonanzasatrangi.com/pk/accessories/shalwar//', 'name': 'Shalwar'},
]
menBrands = [{'url': 'https://www.bonanzasatrangi.com/pk/men/groom-collection', 'name': 'Groom Collection'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/kurta', 'name': 'Kurta'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/waistcoat', 'name': 'Waistcoat'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/kurta-shalwar', 'name': 'Kurta Shalwar'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/unstitched', 'name': 'Unstitched'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/pajama', 'name': 'Pajama'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/shalwar-suit', 'name': 'Shalwar Suit'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/3in1', 'name': 'Packages'}]
kidsBrands = [{'url':'https://www.bonanzasatrangi.com/pk/kids/kids-alive/1-piece/', 'name': '1 Piece'},{'url':'https://www.bonanzasatrangi.com/pk/kids/kids-alive/2-piece/', 'name': '2 Piece'},{'url':'https://www.bonanzasatrangi.com/pk/kids/kids-alive/3-piece/', 'name': '3 Piece'}]

def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    print('product url ', productUrl)
    driver.get(productUrl)
    time.sleep(12)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    size = []
    colors = []

    if((soup.find('div', attrs={'class' : 'swatch-attribute size'}))):
        sizeDiv = soup.find('div', attrs={'class' : 'swatch-attribute-options clearfix'}).findAll('div')
        for _size in sizeDiv:
            if (_size):
                # print('size => ',_size.text)
                size.append(_size.text)
    if(soup.find('div', attrs={'class' : 'swatch-attribute color'})):
        colorDiv = soup.find('div', attrs={'class' : 'swatch-attribute color'}).find('div', attrs={'class': 'swatch-attribute-options clearfix'}).findAll('div')
        for _color in colorDiv:
            if(_color['option-label']):
                colors.append((_color['option-label']).strip().lower())
    elif(soup.find('div', attrs={'class' : 'color'})):
        # print('has class color')
        colorDiv = soup.find('div', attrs={'class' : 'color'})
        # print('color div ', colorDiv)
        if(colorDiv.find('p').text):
            # print('color ', colorDiv.find('p').text.strip())
            colors.append(colorDiv.find('p').text.strip().lower())

    else:
        colors=[]

    _productData['colors'] = colors
    _productData['size'] = size
    print('product data ', _productData)
    mydb.freshProducts.insert_one(_productData)
    print('................................................................................................')

def processSitePageSoup(soup, brandName,gender):
    if(soup.findAll('div',{'class':'product-item-info product-content'})):
        for rowdata in soup.findAll('div',{'class':'product-item-info product-content'}):
            if (rowdata != None):
                buy_url = rowdata.findAll('a')[-1]['href']
                price = rowdata.find('span', {'class': 'price'}).text.strip()
                title = rowdata.find("img")['alt']
                imageURL = rowdata.find("img")['src']
                dataObject = {
                    "id" : random.choice(list(range(0,100000)))+random.choice(list(range(77,15400)))+random.choice(list(range(55,5000))),
                    'name' : title,
                    'colors': [],
                    'size': [],
                    'pictures' : [imageURL],
                    'stock' : "N/A",
                    'price' : float(price[3:].strip().replace(',', '')),
                    'discount' : 0,
                    'salePrice' : 0,
                    'description': '',
                    'tags': [gender,brandName],
                    'rating': random.choice(list(range(3, 5))),
                    'category':gender,
                    'buyUrl': buy_url,
                    'gender': gender,
                    'brand': brandName,
                    'date': datetime.today(),
                    'mainBrand': 'bonanza'
                }
                # print("data________",dataObject)
                goToProductDetail(dataObject,buy_url)
    else:
        print('no products found')

def openSitePage(brandData, gender):
    # print("brandData " , brandData)
    for sitePage in brandData:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],gender)

def ScrapProducts():
    try:
        allBrands = [
            {'blist': womenBrands, 'name': 'women'},
            # {'blist': menBrands, 'name': 'men'},
            # {'blist': kidsBrands, 'name': 'kids'},
        ]
        for brand in allBrands:
            openSitePage(brand['blist'], brand['name'])
    except Exception as el:
        print("Exception occured ", el)
        driver.close()


def getAllLinks():
    scrapeUrl = "https://www.bonanzasatrangi.com/pk/men/"
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source,'lxml')
    brandSoup = soup.findAll('li', attrs={'class': 'subcategory'})[8:14]
    print('soup_____length', brandSoup.__len__())
    for brand in brandSoup:
        # print("brand_", brand)
        if(brand.find('a') != -1):
            print(brand.find('a')['href'])
            print(brand.find('a').text.strip())
            womenBrands.append(
                        {
                            'url':brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
        print('........................................................................')
    driver.close()
    print('womenBrands ', womenBrands)

try:

    ScrapProducts()
    # getAllLinks()
except Exception as el:
    print("Exception occured ", el)
    driver.close()

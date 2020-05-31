import random
from datetime import date,datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
from datetime import date
menBrands = [{'url': 'https://breakout.com.pk/collections/men-new-in', 'name': 'NEW IN'}, {'url': 'https://breakout.com.pk/collections/men-tees', 'name': 'Tees'}, {'url': 'https://breakout.com.pk/collections/men-polos', 'name': 'Polos'}, {'url': 'https://breakout.com.pk/collections/men-shirts', 'name': 'Shirts'}, {'url': 'https://breakout.com.pk/collections/denim', 'name': 'Denim'}, {'url': 'https://breakout.com.pk/collections/men-trouser-chinos', 'name': 'Trouser / Chinos'}, {'url': 'https://breakout.com.pk/collections/men-shorts', 'name': 'Shorts'}, {'url': 'https://breakout.com.pk/collections/men-joggers', 'name': 'Joggers'}, {'url': 'https://breakout.com.pk/collections/men-bags', 'name': 'Bags'}, {'url': 'https://breakout.com.pk/collections/men-shoes', 'name': 'Shoes'}, {'url': 'https://breakout.com.pk/collections/men-belts', 'name': 'Belts'}, {'url': 'https://breakout.com.pk/collections/men-wallets', 'name': 'Wallets'}, {'url': 'https://breakout.com.pk/collections/men-perfumes', 'name': 'Perfumes'}, {'url': 'https://breakout.com.pk/collections/men_glasses', 'name': 'Glasses'}, {'url': 'https://breakout.com.pk/collections/men_underwears', 'name': 'Underwear'}, {'url': 'https://breakout.com.pk/collections/men_watches', 'name': 'Watches'}, {'url': 'https://breakout.com.pk/collections/men_caps', 'name': 'Caps & Hats'}]
womenBrands = [{'url': 'https://breakout.com.pk/collections/women-new-in', 'name': 'NEW IN'}, {'url': 'https://breakout.com.pk/collections/women-tops', 'name': 'Tops'}, {'url': 'https://breakout.com.pk/collections/women-shirts', 'name': 'Shirts'}, {'url': 'https://breakout.com.pk/collections/women-denim-and-trousers', 'name': 'Denim And Trousers'}, {'url': 'https://breakout.com.pk/collections/women-bags', 'name': 'Bags'}, {'url': 'https://breakout.com.pk/collections/women-shoes', 'name': 'Shoes'}, {'url': 'https://breakout.com.pk/collections/women-scarves', 'name': 'Scarves'}, {'url': 'https://breakout.com.pk/collections/women-perfumes', 'name': 'Perfumes'}, {'url': 'https://breakout.com.pk/collections/women_glasses', 'name': 'Glasses'}, {'url': 'https://breakout.com.pk/collections/women_belts', 'name': 'Belts'}, {'url': 'https://breakout.com.pk/collections/women_caps', 'name': 'Hats'}]
kidsBrands = [{'url': 'https://breakout.com.pk/collections/new-in-3', 'name': 'NEW IN'}, {'url': 'https://breakout.com.pk/collections/tees-3', 'name': 'Tees'}, {'url': 'https://breakout.com.pk/collections/boys_1-5_shirts', 'name': 'Shirts'}, {'url': 'https://breakout.com.pk/collections/bottoms-2', 'name': 'Bottoms'}, {'url': 'https://breakout.com.pk/collections/accessories-shoes-3', 'name': 'Shoes'}, {'url': 'https://breakout.com.pk/collections/boys_acc', 'name': 'Accessories'}, {'url': 'https://breakout.com.pk/collections/new-in-2', 'name': 'NEW IN'}, {'url': 'https://breakout.com.pk/collections/tees-2', 'name': 'Tees'}, {'url': 'https://breakout.com.pk/collections/shirts', 'name': 'Shirts'}, {'url': 'https://breakout.com.pk/collections/bottoms-1', 'name': 'Bottoms'}, {'url': 'https://breakout.com.pk/collections/accessories-shoes-2', 'name': 'Shoes'}, {'url': 'https://breakout.com.pk/collections/boys_acc', 'name': 'Accessories'}]

brand_count = 0
scrapeUrl = ""


def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    print('product url ', productUrl)
    driver.get(productUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # print("detail soup ",soup)
    sizeDiv = soup.findAll('ul', attrs={'class' : 'sbOptions'})[1].findAll('li', attrs={'class' : 'addsize'})[1:]
    colorDiv = soup.find('ul', attrs={'class' : 'option-list color-squares'}).findAll('span', attrs={'class' : 'color-container'})
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
            colors.append(color['title'])
    if(soup.find('div', attrs={'class': 'gallery picture'}).findAll('img')):
        pictureDiv = soup.find('div', attrs={'class': 'gallery picture'}).findAll('img')
        for pic in pictureDiv:
            if (pic):
                # print('pic____',pic['src'])
                pictures.append(pic['src'])

    _productData['colors'] = colors
    _productData['size'] = size
    _productData['pictures'] = pictures
    print('product data ', _productData)
    # mydb.productslist.insert_one(_productData)
    print('................................................................................................')


def openSitePage(menBrands, gender):
    print("menBrands " , menBrands)
    for sitePage in menBrands:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],gender)

jsonData = []
def processSitePageSoup(soup, brandName,gender):
    print('processing soup')
    products = soup.findAll('div',{'class':'product-item'})
    for product in products:
        print('prodcut data ', product)
        if(product.find('div',{'class':'details'})):
            # print("product======>>>>",product.find('div',{'class':'details'}))
            title = product.find('div',{'class':'details'}).findAll('a')[0].text
            buyUrl = 'https://www.breakout.com.pk'+product.find('div',{'class':'details'}).findAll('a')[0]['href']
            priceNew = 0
            priceOld = 0
            if (product.find('div',{'class':'details'}).find('div', {'class': 'prices'}).findAll('span')[1]):
                priceOld = (product.find('div',{'class':'details'}).find('div', {'class': 'prices'}).findAll('span')[0]).text
                priceNew = (product.find('div',{'class':'details'}).find('div', {'class': 'prices'}).findAll('span')[1]).text
            productData = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                'name': title,
                'pictures': [],
                'stock': 0,
                'price': int(priceNew[:-5].strip().replace(',', '')),
                'discount': int(priceOld[:-5].strip().replace(',', '')) - int(priceNew[:-5].strip().replace(',', '')),
                'salePrice': int(priceOld[:-5].strip().replace(',', '')),
                'description': '',
                'tags': [gender, brandName],
                'rating': random.choice(list(range(3, 5))),
                'category': gender,
                'colors': [],
                'size': [],
                'buyUrl': buyUrl,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'breakout'
            }
            goToProductDetail(productData,buyUrl)

print('starting scrapping')

def getAllLinks(_url):
    _mainUrl = "https://breakout.com.pk"
    driver.get(_url)
    soup = BeautifulSoup(driver.page_source,'lxml')
    print('get links')
    menLinks = soup.findAll('li', attrs={'class': 'dropdown megamenu pt-submenu'})[0].findAll('ul', attrs={'class': 'pt-megamenu-submenu'})
    womenLinks = soup.findAll('li', attrs={'class': 'dropdown megamenu pt-submenu'})[1].findAll('ul', attrs={'class': 'pt-megamenu-submenu'})
    kidsLinks = soup.findAll('li', attrs={'class': 'dropdown megamenu pt-submenu'})[2].findAll('ul', attrs={'class': 'pt-megamenu-submenu'})

    for ul in menLinks:
        for brand in ul.findAll('li'):
            if(brand.find('a') != -1):
                menBrands.append({'url': _mainUrl + brand.find('a')['href'],'name': brand.find('a').text.strip()})
    for ul in womenLinks:
        for brand in ul.findAll('li'):
            if (brand.find('a') != -1):
                womenBrands.append({'url': _mainUrl +  brand.find('a')['href'],'name': brand.find('a').text.strip()})
    for ul in kidsLinks:
        for brand in ul.findAll('li'):
            if(brand.find('a') != -1):
                kidsBrands.append({'url': _mainUrl + brand.find('a')['href'],'name': brand.find('a').text.strip()})
    print('menBrands = ', menBrands)
    print('womenBrands = ', womenBrands)
    print('kidsBrands = ', kidsBrands)

    driver.close()

##get all links
# try:
#     getAllLinks('https://breakout.com.pk/')
# except Exception as el:
#     print("Exception occured ", el)
#     driver.close()

try:
    allBrands = [{'blist':menBrands, 'name': 'men'},{'blist':womenBrands, 'name': 'women'},{'blist':kidsBrands, 'name': 'kids'}]
    for brand in allBrands:
       openSitePage(brand['blist'], brand['name'])

except Exception as el:
    print("Exception occured ", el)
    driver.close()
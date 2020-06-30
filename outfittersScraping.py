import time
import random
from datetime import date,datetime
from bs4 import BeautifulSoup
import pymongo
from selenium import webdriver
myclient       = pymongo.MongoClient("mongodb://localhost:27017/")
mydb           = myclient["fypDb"]
driver         = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
allColorsMix   = ['BLU CMO', 'OFT', 'CMO', 'NVY YEL', 'NVY', 'LT. PNK', 'NVY WHT', 'NVY', 'CHM BLU', 'RED NVY', 'PNK', 'BLK', 'WHT', 'OFT', 'YEL WHT', 'BLU WHT', 'BLK', 'PNK WHT', 'MST WHT', 'MGT WHT', 'BLU WHT', 'RED BLK', 'BLK', 'BBY PNK', 'OFT', 'BEG', 'MST NVY', 'BUR', 'PNK MST', 'BLU BUR', 'BUR OLV', 'N:G:B', 'OLV PCH', 'WHT', 'ECR', 'NVY', 'NVY', 'BUR', 'HGR', 'MST BLK', 'LT. PNK', 'WHT', 'BLS PNK', 'WHT', 'BLK', 'MST', 'LT. PNK', 'CHM BLU', 'BLK', 'BLU', 'NEO MNT', 'WHT', 'NVY', 'LIM GRN', 'OLV', 'NVY', 'WHT', 'RED', 'WHT', 'YEL', 'WHT', 'BLU', 'LT. BLU', 'BLK', 'BLU RIN', 'OLV', 'BLK', 'PNK', 'BLK', 'OLV', 'WHT', 'SND', 'LT. BLU', 'BLU DRK', 'LT. BLU', 'BLU DRK', 'BLU DRK', 'BLK', 'LT. BLU', 'DST PNK', 'PNK', 'GRY', 'BLK', 'GRN', 'GRY', 'BLK', 'BLK', 'BRN', 'BLK YEL', 'NVY', 'BLK', 'BLK RED', 'BLK', 'RED', 'BLK', 'GRY', 'ORG', 'BLK', 'BLK', 'OLV', 'BLS PNK', 'NEO MNT', 'MRN', 'BLK', 'MRN', 'BLK', 'MRN', 'WHT', 'BLK', 'WHT', 'GRN', 'HGR BLU', 'WHT BLK', 'HGR YEL', 'BLK', 'N:B:W', 'HGR', 'ASH BLU', 'BLK', 'MST', 'HGR MST', 'HGR WHT', 'BLU', 'OLV', 'HGR', 'NVY WHT', 'BLK', 'HTR GRY', 'HGR BLK', 'MST NVY', 'HGR', 'RED NVY', 'HGR BLK', 'HGR', 'DRK GRN', 'NVY', 'BLK', 'NVY', 'WHT NVY', 'BLU', 'WHT', 'WHT', 'BLK RED', 'PTR', 'RED', 'NVY', 'OLV', 'YEL', 'HGR BLU', 'HGR', 'BLK', 'WHT', 'BLU', 'HGR BLU', 'OLV NVY', 'WHT', 'WHT RED', 'OLV', 'MRN', 'WHT', 'NVY', 'HTR GRY', 'RED', 'BLK', 'MST BLU', 'BLU WHT', 'WHT YEL', 'BLK', 'NVY WHT', 'MID BLU', 'GRN BLU', 'BLU GRN', 'BEG', 'WHT', 'BLK WHT', 'OLV NVY', 'OFT NVY', 'NVY', 'HGR', 'BLK', 'PNK WHT', 'TEL', 'CMO', 'DRK BLU', 'STN', 'WHT', 'NVY', 'BLK', 'WHT', 'WHT', 'NVY RED', 'NVY MST', 'RED BLU', 'BLU MGT', 'NVY GRY', 'LT. BLU', 'BLK', 'LT. BLU', 'MID BLU', 'DRK BLU', 'LT. BLU', 'BLK', 'MID BLU', 'MID BLU', 'MID BLU', 'DRK BLU', 'DRK BLU', 'LT. GRY', 'GRY', 'DRK BLU', 'RNS', 'RNS', 'RNS', 'OLV', 'MRN', 'BEG', 'WHT BLU', 'BLK', 'DRK OLV', 'STN', 'LT. GRN', 'NVY', 'OLV', 'BLK', 'STN', 'BLU', 'BUR', 'STN', 'OLV', 'NVY', 'KHK', 'BLK', 'RED', 'MRN CMO', 'BLU', 'BRN', 'NVY', 'BLK', 'LT. GRY', 'BLK', 'H:N:W', 'RED', 'BRN WHT', 'LT. GRY', 'GRN CMO', 'GRN', 'NVY', 'NVY', 'NVY RED', 'NVY', 'BLU', 'BEG', 'OLV GRN', 'NVY', 'NVY', 'LT. YEL', 'BLU', 'LT. GRY', 'BLK HTG', 'RED', 'ORG', 'MST BLK', 'DRK GRY', 'HTG BLK', 'O:O:N']
colorsWithName = [{'color': 'DST PNK', 'name': 'PINK'}, {'color': 'WHT BLU', 'name': 'WHITE BLUE'}, {'color': 'BEG', 'name': 'BEG'}, {'color': 'BLU CMO', 'name': 'BLU CMO'}, {'color': 'OFT', 'name': 'OFT'}, {'color': 'PNK', 'name': 'PNK'}, {'color': 'RED BLK', 'name': 'RED BLK'}, {'color': 'GRN', 'name': 'GRN'}, {'color': 'NEO MNT', 'name': 'NEO MNT'}, {'color': 'OLV', 'name': 'OLV'}, {'color': 'WHT', 'name': 'WHT'}, {'color': 'BLU BUR', 'name': 'BLU BUR'}, {'color': 'HTR GRY', 'name': 'HTR GRY'}, {'color': 'NVY YEL', 'name': 'NVY YEL'}, {'color': 'KHK', 'name': 'KHK'}, {'color': 'OLV GRN', 'name': 'OLV GRN'}, {'color': 'NVY', 'name': 'NVY'}, {'color': 'OFT NVY', 'name': 'OFT NVY'}, {'color': 'RED BLU', 'name': 'RED BLU'}, {'color': 'WHT YEL', 'name': 'WHT YEL'}, {'color': 'BLU MGT', 'name': 'BLU MGT'}, {'color': 'NVY MST', 'name': 'NVY MST'}, {'color': 'BUR', 'name': 'BUR'}, {'color': 'LT. YEL', 'name': 'LT. YEL'}, {'color': 'MRN', 'name': 'MRN'}, {'color': 'STN', 'name': 'STN'}, {'color': 'H:N:W', 'name': 'H:N:W'}, {'color': 'BLK', 'name': 'BLK'}, {'color': 'HGR BLU', 'name': 'HGR BLU'}, {'color': 'LT. GRY', 'name': 'LT. GRY'}, {'color': 'N:B:W', 'name': 'N:B:W'}, {'color': 'LT. GRN', 'name': 'LT. GRN'}, {'color': 'GRN CMO', 'name': 'GRN CMO'}, {'color': 'GRN BLU', 'name': 'GRN BLU'}, {'color': 'PNK WHT', 'name': 'PNK WHT'}, {'color': 'LIM GRN', 'name': 'LIM GRN'}, {'color': 'OLV NVY', 'name': 'OLV NVY'}, {'color': 'HGR WHT', 'name': 'HGR WHT'}, {'color': 'TEL', 'name': 'TEL'}, {'color': 'BLK HTG', 'name': 'BLK HTG'}, {'color': 'WHT RED', 'name': 'WHT RED'}, {'color': 'ASH BLU', 'name': 'ASH BLU'}, {'color': 'LT. BLU', 'name': 'LT. BLU'}, {'color': 'MST WHT', 'name': 'MST WHT'}, {'color': 'DRK OLV', 'name': 'DRK OLV'}, {'color': 'OLV PCH', 'name': 'OLV PCH'}, {'color': 'BLK WHT', 'name': 'BLK WHT'}, {'color': 'RED NVY', 'name': 'RED NVY'}, {'color': 'BRN', 'name': 'BRN'}, {'color': 'BRN WHT', 'name': 'BRN WHT'}, {'color': 'BLS PNK', 'name': 'BLS PNK'}, {'color': 'BLU RIN', 'name': 'BLU RIN'}, {'color': 'N:G:B', 'name': 'N:G:B'}, {'color': 'BLU', 'name': 'BLU'}, {'color': 'NVY WHT', 'name': 'NVY WHT'}, {'color': 'MGT WHT', 'name': 'MGT WHT'}, {'color': 'O:O:N', 'name': 'O:O:N'}, {'color': 'WHT NVY', 'name': 'WHT NVY'}, {'color': 'RNS', 'name': 'RNS'}, {'color': 'MST NVY', 'name': 'MST NVY'}, {'color': 'BUR OLV', 'name': 'BUR OLV'}, {'color': 'GRY', 'name': 'GRY'}, {'color': 'RED', 'name': 'RED'}, {'color': 'PTR', 'name': 'PTR'}, {'color': 'BLK RED', 'name': 'BLK RED'}, {'color': 'LT. PNK', 'name': 'LT. PNK'}, {'color': 'HGR', 'name': 'HGR'}, {'color': 'CMO', 'name': 'CMO'}, {'color': 'HTG BLK', 'name': 'HTG BLK'}, {'color': 'CHM BLU', 'name': 'CHM BLU'}, {'color': 'BLU DRK', 'name': 'BLU DRK'}, {'color': 'DRK BLU', 'name': 'DRK BLU'}, {'color': 'MST BLK', 'name': 'MST BLK'}, {'color': 'BLU WHT', 'name': 'BLU WHT'}, {'color': 'BBY PNK', 'name': 'BBY PNK'}, {'color': 'HGR BLK', 'name': 'HGR BLK'}, {'color': 'DRK GRN', 'name': 'DRK GRN'}, {'color': 'NVY RED', 'name': 'NVY RED'}, {'color': 'WHT BLK', 'name': 'WHT BLK'}, {'color': 'ECR', 'name': 'ECR'}, {'color': 'SND', 'name': 'SND'}, {'color': 'HGR YEL', 'name': 'HGR YEL'}, {'color': 'MID BLU', 'name': 'MID BLU'}, {'color': 'DRK GRY', 'name': 'DRK GRY'}, {'color': 'YEL WHT', 'name': 'YEL WHT'}, {'color': 'YEL', 'name': 'YEL'}, {'color': 'MST BLU', 'name': 'MST BLU'}, {'color': 'BLK YEL', 'name': 'BLK YEL'}, {'color': 'PNK MST', 'name': 'PNK MST'}, {'color': 'ORG', 'name': 'ORG'}, {'color': 'HGR MST', 'name': 'HGR MST'}, {'color': 'NVY GRY', 'name': 'NVY GRY'}, {'color': 'MST', 'name': 'MST'}, {'color': 'MRN CMO', 'name': 'MRN CMO'}, {'color': 'BLU GRN', 'name': 'BLU GRN'}]
menBrands      = [{'url': 'https://outfitters.com.pk/collections/men-shirts', 'name': 'Shirts'}, {'url': 'https://outfitters.com.pk/collections/men-denim', 'name': 'Denim'}, {'url': 'https://outfitters.com.pk/collections/men-trousers', 'name': 'Trousers'}, {'url': 'https://outfitters.com.pk/collections/men-chinos', 'name': 'Chinos'}, {'url': 'https://outfitters.com.pk/collections/men-sweater-1', 'name': 'Sweater'}, {'url': 'https://outfitters.com.pk/collections/men-jacket-1', 'name': 'Jacket'}, {'url': 'https://outfitters.com.pk/collections/men-cardigan', 'name': 'Cardigan'}, {'url': 'https://outfitters.com.pk/collections/men-hoodie-1', 'name': 'Hoodie'}, {'url': 'https://outfitters.com.pk/collections/men-shorts', 'name': 'Shorts'}, {'url': 'https://outfitters.com.pk/collections/men-t-shirts', 'name': 'T-Shirt'}, {'url': 'https://outfitters.com.pk/collections/men-shirts', 'name': 'Shirts'}, {'url': 'https://outfitters.com.pk/collections/men-denim', 'name': 'Denim'}, {'url': 'https://outfitters.com.pk/collections/men-trousers', 'name': 'Trousers'}, {'url': 'https://outfitters.com.pk/collections/men-chinos', 'name': 'Chinos'}, {'url': 'https://outfitters.com.pk/collections/men-sweater-1', 'name': 'Sweater'}, {'url': 'https://outfitters.com.pk/collections/men-jacket-1', 'name': 'Jacket'}, {'url': 'https://outfitters.com.pk/collections/men-cardigan', 'name': 'Cardigan'}, {'url': 'https://outfitters.com.pk/collections/men-hoodie-1', 'name': 'Hoodie'}, {'url': 'https://outfitters.com.pk/collections/men-shorts', 'name': 'Shorts'},{'url': 'https://outfitters.com.pk/collections/men-t-shirts', 'name': 'T-Shirt'}, ]
womenBrands    = [ {'url': 'https://outfitters.com.pk/collections/women-t-shirts', 'name': 'T-Shirts'}, {'url': 'https://outfitters.com.pk/collections/women-denim', 'name': 'Denim'}, {'url': 'https://outfitters.com.pk/collections/women-trouser', 'name': 'Trousers'}, {'url': 'https://outfitters.com.pk/collections/skirts', 'name': 'Skirt'}, {'url': 'https://outfitters.com.pk/collections/women-sweater-1', 'name': 'Sweater'}, {'url': 'https://outfitters.com.pk/collections/women-jacket-1', 'name': 'Jacket'}, {'url': 'https://outfitters.com.pk/collections/cap-shawal', 'name': 'Cape Shawl'}, {'url': 'https://outfitters.com.pk/collections/women-shrug', 'name': 'Shrug'},{'url': 'https://outfitters.com.pk/collections/women-shirts', 'name': 'Shirts'},]
kidsBrands     = [{'url': 'https://outfitters.com.pk/collections/girls-shirts', 'name': 'Shirts'}, {'url': 'https://outfitters.com.pk/collections/girls-t-shirts', 'name': 'T-Shirts'}, {'url': 'https://outfitters.com.pk/collections/girls-sweat-shirt', 'name': 'Hoodies & Sweatshirt'}, {'url': 'https://outfitters.com.pk/collections/girls-frocks', 'name': 'Frocks'}, {'url': 'https://outfitters.com.pk/collections/girls-jeans', 'name': 'Jeans'}, {'url': 'https://outfitters.com.pk/collections/non-denim-girls', 'name': 'Non Denim'}, {'url': 'https://outfitters.com.pk/collections/girls-sweater-1', 'name': 'Sweater'}, {'url': 'https://outfitters.com.pk/collections/girls-jacket-1', 'name': 'Jacket'}, {'url': 'https://outfitters.com.pk/collections/girl-jump-suit', 'name': 'Jumpsuit'}]


# myset = set(allColorsMix)
# print("unique items ",myset)

colorsArray = []


def colorAssignment(color):
    if "black" in color:
        return "black"
    elif "blue" in color:
        return "blue"
    elif "white" in color:
        return "white"
    elif "red" in color:
        return "red"
    elif "green" in color:
        return "green"
    elif "navy" in color:
        return "navy"
    elif "mint" in color:
        return "mint"
    elif "navy" in color:
        return "navy"
    elif "cream" in color:
        return "cream"
    elif "mehroon" in color:
        return "mehroon"
    else:
        return "other"

def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    print('product url ', productUrl)
    driver.get(productUrl)
    time.sleep(7)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    sizeDiv = []
    if(soup.find('div', attrs={'class' : 'swatch size'})):
        sizeDiv = soup.find('div', attrs={'class' : 'swatch size'}).findAll('label')
    color=''
    if(soup.find('p', attrs={'class': 'Rcolor-label'})):
       color = soup.find('p', attrs={'class': 'Rcolor-label'}).find('span').text.lower().strip()
    size = []
    for _size in sizeDiv:
        if(_size):
            # print('size => ',_size.text.strip())
            size.append(_size.text.strip().lower())
    _productData['colors'] = [color]
    _productData['size'] = size
    mydb.freshProducts.insert_one(_productData)
    print('product data ', _productData)
    print('................................................................................................')


def openSitePage(brandData, type):
    for sitePage in brandData:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],type)

def processSitePageSoup(soup, brandName,gender):
    _mainUrl = "https://www.engine.com.pk"
    for outFitters in soup.select('div[class*="grid-item"]'):
           buyUrl = "https://outfitters.com.pk"+outFitters.find('a')['href'].strip()
           title = outFitters.find('img')['alt'].strip()
           images=[]
           # print('image tag  ', outFitters.find('img'))
           if(outFitters.find('img')['data-src']):
                imageUrl = "https:" + outFitters.find('img')['data-src']
                images = [imageUrl]
           # print('title ', title)
           price = outFitters.find('span', {'class': 'money'}).text.strip()
           dataObject = {
               "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
               'name': title,
               'pictures': images,
               'stock': 'N/A',
               'price': int(price[3:].strip().replace(',', '')),
               'discount': 0,
               'salePrice': 0,
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
               'mainBrand': 'outfitters'
               }
           # print('product ', dataObject)
           goToProductDetail(dataObject,buyUrl)


#find list to iterate
def getAllLinks(_url):
    driver.get(_url)
    soup = BeautifulSoup(driver.page_source,'lxml')
    menSoup = soup.findAll('div', attrs={'class': 'col-1 parent-mega-menu'})[0].find('ul').findAll('li')
    womenSoup = soup.findAll('div', attrs={'class': 'col-1 parent-mega-menu'})[1].find('ul').findAll('li')
    kidsSoup = soup.findAll('div', attrs={'class': 'col-1 parent-mega-menu'})[2].find('ul').findAll('li')

    _mainUrl = "https://outfitters.com.pk"
    for brand in menSoup:
        print('brand ', brand)
        if(brand.find('a') != -1):
            print(brand.find('a')['href'])
            print(brand.find('a').text.strip())
            menBrands.append(
                        {
                            'url': _mainUrl + brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
        print('........................................................................')
    print('menBrands__________', menBrands)

    for brand in womenSoup:
        print('brand ', brand)
        if(brand.find('a') != -1):
            print(brand.find('a')['href'])
            print(brand.find('a').text.strip())
            womenBrands.append(
                        {
                            'url': _mainUrl + brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
        print('........................................................................')
    print('womenBrands__________', womenBrands)

    for brand in kidsSoup:
        print('brand ', brand)
        if(brand.find('a') != -1):
            print(brand.find('a')['href'])
            print(brand.find('a').text.strip())
            kidsBrands.append(
                        {
                            'url': _mainUrl + brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
        print('........................................................................')
    print('kidsBrands__________', kidsBrands)

    print('menBrands = ', menBrands)
    print('womenBrands = ', womenBrands)
    print('kidsBrands = ', kidsBrands)

    driver.close()


try:
    allBrands = [
        {'blist': menBrands, 'name': 'men'},
        {'blist': kidsBrands, 'name': 'kids'},
        {'blist': womenBrands, 'name': 'women'},
    ]

    for brand in allBrands:
       openSitePage(brand['blist'], brand['name'])
except Exception as el:
    print("Exception occured ", el)
    driver.close()

driver.close()

##start point for getting all the links for men,women,kids brands urls and brand names

# try:
#     scrapeUrl = "https://outfitters.com.pk/collections/men"
#     getAllLinks(scrapeUrl)
# except Exception as el:
#     print("Error opening site  ", el)
#     driver.close()

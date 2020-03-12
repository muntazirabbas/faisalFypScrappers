import random
from datetime import date,datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
from datetime import date
menBrands =  [{'url': 'https://www.breakout.com.pk//stranger-things-collection', 'name': 'STRANGER THINGS COLLECTION'}, {'url': 'https://www.breakout.com.pk//new-in', 'name': 'NEW IN'}, {'url': 'https://www.breakout.com.pk//tees', 'name': 'TEES'}, {'url': 'https://www.breakout.com.pk//polos', 'name': 'POLOS'}, {'url': 'https://www.breakout.com.pk//shirts-2', 'name': 'Shirts'}, {'url': 'https://www.breakout.com.pk//denim', 'name': 'Denim'}, {'url': 'https://www.breakout.com.pk//non-denim', 'name': 'TROUSERS / CHINOS'}, {'url': 'https://www.breakout.com.pk//joggers', 'name': 'JOGGERS'}, {'url': 'https://www.breakout.com.pk//sweater-3', 'name': 'Sweaters'}, {'url': 'https://www.breakout.com.pk//coat-4', 'name': 'Coats/Blazers'}, {'url': 'https://www.breakout.com.pk//upper-3', 'name': 'Sweatshirts / hoodies'}, {'url': 'https://www.breakout.com.pk//jacket-3', 'name': 'Jackets'}, {'url': 'https://www.breakout.com.pk//shoes-2', 'name': 'Shoes'}, {'url': 'https://www.breakout.com.pk//bags-3', 'name': 'BAGS'}, {'url': 'https://www.breakout.com.pk//belts', 'name': 'BELTS'}, {'url': 'https://www.breakout.com.pk//wallets', 'name': 'WALLETS'}, {'url': 'https://www.breakout.com.pk//perfumes', 'name': 'PERFUMES'}]
womenBrands = [{'url': 'https://www.breakout.com.pk//stranger-things-collection-2', 'name': 'STRANGER THINGS COLLECTION'}, {'url': 'https://www.breakout.com.pk//new-in-2', 'name': 'NEW IN'}, {'url': 'https://www.breakout.com.pk//tops-3', 'name': 'Tops'}, {'url': 'https://www.breakout.com.pk//shirts-7', 'name': 'Shirts'}, {'url': 'https://www.breakout.com.pk//bottom', 'name': 'Denim and trousers'}, {'url': 'https://www.breakout.com.pk//shawls-2', 'name': 'Shawls/Capes'}, {'url': 'https://www.breakout.com.pk//sweater-4', 'name': 'Sweaters'}, {'url': 'https://www.breakout.com.pk//upper-4', 'name': 'Uppers / Sweatshirts'}, {'url': 'https://www.breakout.com.pk//jacket-4', 'name': 'Jackets'}, {'url': 'https://www.breakout.com.pk//shoes', 'name': 'Shoes'}, {'url': 'https://www.breakout.com.pk//bags-4', 'name': 'BAGS'}, {'url': 'https://www.breakout.com.pk//scarves', 'name': 'SCARVES'}, {'url': 'https://www.breakout.com.pk//perfumes-2', 'name': 'PERFUMES'}]
kidsBrands = [{'url': 'https://www.breakout.com.pk//new-in-5', 'name': 'NEW IN'}, {'url': 'https://www.breakout.com.pk//tees-5', 'name': 'Tees'}, {'url': 'https://www.breakout.com.pk//tops-4', 'name': 'Tops'}, {'url': 'https://www.breakout.com.pk//sweaters-3', 'name': 'Sweaters'}, {'url': 'https://www.breakout.com.pk//jackets-3', 'name': 'Jackets'}, {'url': 'https://www.breakout.com.pk//uppers-3', 'name': 'Uppers'}, {'url': 'https://www.breakout.com.pk//bottoms-5', 'name': 'Bottoms'}, {'url': 'https://www.breakout.com.pk//accessories-shoes-3', 'name': 'Accessories & Shoes'},{'url': 'https://www.breakout.com.pk//new-in-6', 'name': 'NEW IN'}, {'url': 'https://www.breakout.com.pk//tees-6', 'name': 'Tees'}, {'url': 'https://www.breakout.com.pk//tops-5', 'name': 'Tops'}, {'url': 'https://www.breakout.com.pk//sweaters-4', 'name': 'Sweaters'}, {'url': 'https://www.breakout.com.pk//jackets-4', 'name': 'Jackets'}, {'url': 'https://www.breakout.com.pk//uppers-4', 'name': 'Uppers'}, {'url': 'https://www.breakout.com.pk//bottoms-6', 'name': 'Bottoms'}, {'url': 'https://www.breakout.com.pk//accessories-shoes-4', 'name': 'Accessories & Shoes'}]
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
    # print("sizeDiv ______________", sizeDiv)
    # print("colorDiv______________", colorDiv)
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
    products = soup.findAll('div',{'class':'product-item'})
    for product in products:
        if(product.find('div',{'class':'details'})):
            # print("product======>>>>",product.find('div',{'class':'details'}))
            title = product.find('div',{'class':'details'}).findAll('a')[0].text
            buyUrl = 'https://www.breakout.com.pk'+product.find('div',{'class':'details'}).findAll('a')[0]['href']
            priceNew = 0
            priceOld = 0
            if (product.find('div',{'class':'details'}).find('div', {'class': 'prices'}).findAll('span')[1]):
                priceOld = (product.find('div',{'class':'details'}).find('div', {'class': 'prices'}).findAll('span')[0]).text
                priceNew = (product.find('div',{'class':'details'}).find('div', {'class': 'prices'}).findAll('span')[1]).text
            # imageURL = product.find('div',{'class':'picture'}).findAll('img')['src']
            # print("Type = ", gender)
            # print("Brand = ", brandName)
            # print("Title = ", title)
            # print("Buy URL = ",  buyUrl)
            # print("Price = ", price[:-5])
            # print("Date = ", date.today())
            # print('img = ', imageURL)
            #Required attributes#
            # Gender
            # Category
            # Price
            # Color
            # Size
            # Review
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
            # print("data________", productData)
            #openProductDetail => get colors and sizes
            goToProductDetail(productData,buyUrl)
            # mydb.productslist.insert_one(productData)
            print('...........................................................................................')

print('starting scrapping')

try:
    allBrands = [{'blist':menBrands, 'name': 'men'},{'blist':womenBrands, 'name': 'women'},{'blist':kidsBrands, 'name': 'kids'}]
    for brand in allBrands:
       openSitePage(brand['blist'], brand['name'])
except Exception as el:
    print("Exception occured ", el)
    driver.close()

driver.close()
# brandSoup = soup1.findAll('ul', attrs={'class':'sublist '})[7]
# # print('soup_____', brandSoup)
# breakCounter = 0
# for brand in brandSoup:
#     breakCounter += 1
#     for li in brand:
#         # print('', li)
#         if(li.find('a') != -1):
#             print(li['href'])
#             print(li.text)
#             menBrandNames.append(
#                 {
#                    'url': 'https://www.breakout.com.pk/'+li['href'],
#                     'name': li.text.strip()
#                  })
#         # femaleBrandNames =  a
#     print('........................................................................')
#     # break
#     # print('--counter ', breakCounter)
#     # if(breakCounter == 1):
#     #     menBrandNames = []
#     # if(breakCounter == 2):
#
#     # print('link a', brand.find('a').text.strip())
#
# print('menBrandNames________ ', menBrandNames)

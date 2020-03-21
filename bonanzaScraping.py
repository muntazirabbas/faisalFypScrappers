import time
from datetime import date,datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from fake_useragent import  UserAgent
import random
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
# mydb.uni_collection.update_many({}, {'$unset': {'about_uni': 1}})  ##for removing field

ua = UserAgent()
header = {'user-agent':ua.chrome}
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')

menBrands = [{'url': 'https://www.bonanzasatrangi.com/pk/men/groom-collection', 'name': 'Groom Collection'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/kurta', 'name': 'Kurta'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/waistcoat', 'name': 'Waistcoat'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/kurta-shalwar', 'name': 'Kurta Shalwar'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/unstitched', 'name': 'Unstitched'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/pajama', 'name': 'Pajama'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/shalwar-suit', 'name': 'Shalwar Suit'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/3in1', 'name': 'Packages'}]
womenBrands = [{'url': 'https://www.bonanzasatrangi.com/pk/unstitched/dastaan-premium-collection', 'name': 'Dastaan Premium Collection'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/winter-collection-2019-vol-1', 'name': 'Winter Collection 2019'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/festive-collection-2019', 'name': 'Satrangi Collection 2019'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/unstitched-trousers', 'name': 'Unstitched Trousers'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/unstitched', 'name': 'Satrangi Simple'},{'url': 'https://www.bonanzasatrangi.com/pk/unstitched/dastaan-premium-collection', 'name': 'Dastaan Premium Collection'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/winter-collection-2019-vol-1', 'name': 'Winter Collection 2019'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/festive-collection-2019', 'name': 'Satrangi Collection 2019'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/unstitched-trousers', 'name': 'Unstitched Trousers'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/unstitched', 'name': 'Satrangi Simple'}, {'url': 'https://www.bonanzasatrangi.com/pk/pret/kunbi-pret', 'name': 'Kunbi Pret'}, {'url': 'https://www.bonanzasatrangi.com/pk/pret/pret', 'name': 'Summer Pret'}, {'url': 'https://www.bonanzasatrangi.com/pk/pret/outline-collection', 'name': 'Outline Collection'}, {'url': 'https://www.bonanzasatrangi.com/pk/accessories/dupatta', 'name': 'Dupatta'}, {'url': 'https://www.bonanzasatrangi.com/pk/accessories/shalwar', 'name': 'Shalwar'}, {'url': 'https://www.bonanzasatrangi.com/pk/accessories/trouser', 'name': 'Trouser'}]
kidsBrands = [{'url':'https://www.bonanzasatrangi.com/pk/kids/teen-pret', 'name': 'Pop Teen Pret'}]


def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    print('product url ', productUrl)
    driver.get(productUrl)
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    element = ""
    # try:
    #     element = WebDriverWait(driver2, 15).until(
    #         EC.presence_of_element_located((By.XPATH, "//*[@id='product-options-wrapper']/div/div/div/div[2]"))
    #     )
    # except Exception as e:
    #     print("driver except  ", e)

    # print('element ________', element)
    size = []
    sizeDiv = soup.find('div', attrs={'class' : 'swatch-attribute-options clearfix'}).findAll('div')
    for _size in sizeDiv:
        if (_size):
            # print('size => ',_size.text)
            size.append(_size.text)
        # print('sizeDiv ', sizeDiv)
    colorDiv = soup.find('div', attrs={'class' : 'color'})
    # print('color div ', colorDiv)
    colors = []
    if(colorDiv.find('p').text):
        # print('color ', colorDiv.find('p').text.strip())
        colors.append(colorDiv.find('p').text.strip().lower())

    _productData['colors'] = colors
    _productData['size'] = size
    print('product data ', _productData)
    print('................................................................................................')

def processSitePageSoup(soup, brandName,gender):
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
                'price' : int(price[3:].strip().replace(',', '')),
                'discount' : int(price[3:].strip().replace(',', '')) - int(price[3:].strip().replace(',', '')),
                'salePrice' : int(price[3:].strip().replace(',', '')),
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
            # mydb.productslist.insert_one(dataObject)
        # print('jsonData /n', jsonData)
        print('...........................................................................................')

def openSitePage(brandData, gender):
    print("brandData " , brandData)
    for sitePage in brandData:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],gender)

try:
    allBrands = [{'blist':menBrands, 'name': 'men'},{'blist':womenBrands, 'name': 'women'},{'blist':kidsBrands, 'name': 'kids'}]
    for brand in allBrands:
       openSitePage(brand['blist'], brand['name'])
except Exception as el:
    print("Exception occured ", el)
    driver.close()


def getAllLinks(scrapeUrl):
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

# try:
#     scrapeUrl = "https://www.bonanzasatrangi.com/pk/men/"
#     getAllLinks(scrapeUrl)
# except Exception as el:
#     print("Error opening site  ", el)
#     driver.close()
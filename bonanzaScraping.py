from datetime import date,datetime
import requests
from bs4 import BeautifulSoup
from fake_useragent import  UserAgent
from selenium import webdriver
import random
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
# mydb.uni_collection.update_many({}, {'$unset': {'about_uni': 1}})  ##for removing field

ua = UserAgent()
header = {'user-agent':ua.chrome}
# brand_array = ['pret','unstitched','satrangi-simple','tailor-made',"men/kurta","men/kurta-shalwar","men/shalwar-suit", "men/pajama","kids/pret",'beauty']
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
menBrands = [{'url': 'https://www.bonanzasatrangi.com/pk/men/groom-collection', 'name': 'Groom Collection'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/kurta', 'name': 'Kurta'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/waistcoat', 'name': 'Waistcoat'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/kurta-shalwar', 'name': 'Kurta Shalwar'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/unstitched', 'name': 'Unstitched'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/pajama', 'name': 'Pajama'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/shalwar-suit', 'name': 'Shalwar Suit'}, {'url': 'https://www.bonanzasatrangi.com/pk/men/3in1', 'name': 'Packages'}]
womenBrands = [{'url': 'https://www.bonanzasatrangi.com/pk/unstitched/dastaan-premium-collection', 'name': 'Dastaan Premium Collection'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/winter-collection-2019-vol-1', 'name': 'Winter Collection 2019'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/festive-collection-2019', 'name': 'Satrangi Collection 2019'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/unstitched-trousers', 'name': 'Unstitched Trousers'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/unstitched', 'name': 'Satrangi Simple'},{'url': 'https://www.bonanzasatrangi.com/pk/unstitched/dastaan-premium-collection', 'name': 'Dastaan Premium Collection'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/winter-collection-2019-vol-1', 'name': 'Winter Collection 2019'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/festive-collection-2019', 'name': 'Satrangi Collection 2019'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/unstitched-trousers', 'name': 'Unstitched Trousers'}, {'url': 'https://www.bonanzasatrangi.com/pk/unstitched/unstitched', 'name': 'Satrangi Simple'}, {'url': 'https://www.bonanzasatrangi.com/pk/pret/kunbi-pret', 'name': 'Kunbi Pret'}, {'url': 'https://www.bonanzasatrangi.com/pk/pret/pret', 'name': 'Summer Pret'}, {'url': 'https://www.bonanzasatrangi.com/pk/pret/outline-collection', 'name': 'Outline Collection'}, {'url': 'https://www.bonanzasatrangi.com/pk/accessories/dupatta', 'name': 'Dupatta'}, {'url': 'https://www.bonanzasatrangi.com/pk/accessories/shalwar', 'name': 'Shalwar'}, {'url': 'https://www.bonanzasatrangi.com/pk/accessories/trouser', 'name': 'Trouser'}]
kidsBrands = [{'url':'https://www.bonanzasatrangi.com/pk/kids/teen-pret', 'name': 'Pop Teen Pret'}]

jsonData = []
def processSitePageSoup(soup, brandName,gender):
    count = 0
    for rowdata in soup.findAll('div',{'class':'product-item-info product-content'}):
        # print('rowData:==> ', rowdata)
        if (rowdata != None):
            buy_url = rowdata.findAll('a')[-1]['href']
            # print('buyurl ', buy_url)
            price = rowdata.find('span', {'class': 'price'}).text.strip()
            title = rowdata.find("img")['alt']
            imageURL = rowdata.find("img")['src']
            # print("Type      = ", gender)
            # print("Brand     = ",brandName)
            # print("Title     = ", title)
            # print("price     = ", price[:3])
            # print("Buy URL   = ", buy_url)
            # print("Image URL = ", imageURL)
            # print("date      = ", datetime.today())
            colors = ["black","gray","red", "pink","white","green","blue"]
            size = random.choice(
                [
                    ['100 CM', '90 CM', '95 CM'],
                    ['M', 'L', 'XL'],
                    ['XS', 'S', '2T'],
                    ['3T', '4T', '7'],
                    ['8', '9']
                ])
            mainBrands = ['bonanza','outfitters','breakout','khaadi','engine','gulahmed','junaidjamshed','levi']
            dataObject = {
                "id" : random.choice(list(range(0,100000)))+random.choice(list(range(77,15400)))+random.choice(list(range(55,5000))),
                'name' : title,
                'pictures' : [imageURL],
                'stock' : random.choice(list(range(10, 400))),
                'price' : int(price[3:].strip().replace(',', '')),
                'discount' : random.choice(list(range(0,100))),
                'salePrice' : int(price[3:].strip().replace(',', ''))+random.choice([0,300]),
                'description': '',
                'tags': [gender,brandName],
                'rating': random.choice(list(range(0, 5))),
                'category':gender,
                'colors': [random.choice(colors),random.choice(colors),random.choice(colors)],
                'size': size,
                'buyUrl': buy_url,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'bonanza'
                # 'mainBrand': random.choice(mainBrands)
            }
            # jsonData.append(dataObject)
            print("data________",dataObject)
            #databaseRefrence.collectionName.insertdata
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
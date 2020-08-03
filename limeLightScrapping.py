import time
import requests
from bs4 import BeautifulSoup
import requests
import random
from datetime import datetime
import requests
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
from fake_useragent import  UserAgent
ua          = UserAgent()
header      = {'user-agent':ua.chrome}
from selenium import  webdriver
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome("C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe",chrome_options=chrome_options)
# driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
womenBrands =  [{'url': 'https://www.limelight.pk//collections/shirt', 'name': 'Shirts'}, {'url': 'https://www.limelight.pk//collections/suits', 'name': 'Suits'}, {'url': 'https://www.limelight.pk//collections/short-kurti', 'name': 'Short Kurti'}, {'url': 'https://www.limelight.pk//collections/trousers-1', 'name': 'Trousers'}, {'url': 'https://www.limelight.pk//collections/eid-unstitched-volume20', 'name': "Eid Unstitched Vol'20"}, {'url': 'https://www.limelight.pk//collections/unstitched-embroidered-gold', 'name': 'Unstitched Embroidered & Gold'}, {'url': 'https://www.limelight.pk//collections/unstitched-summer-collection', 'name': "Summer Unstitched  Vol-1 '20"}, {'url': 'https://www.limelight.pk//collections/unstitched-cambric-trouser', 'name': 'Unstitched Cambric Trousers'}, {'url': 'https://www.limelight.pk//collections/summer-lawn-2019', 'name': 'Summer Unstitched 2019'}, {'url': 'https://www.limelight.pk//collections/winter-unstitched-1', 'name': 'Winter Unstitched 2019'}, {'url': 'https://www.limelight.pk//collections/unstitched-winter-trousers', 'name': 'Winter Unstitched  Trousers'}, {'url': 'https://www.limelight.pk//collections/tops', 'name': 'Tops'}, {'url': 'https://www.limelight.pk//collections/western-jumpsuits', 'name': 'Jumpsuits'}, {'url': 'https://www.limelight.pk//collections/camisoles', 'name': 'Camisoles'}, {'url': 'https://www.limelight.pk//collections/bottoms-pants', 'name': 'Pants'}, {'url': 'https://www.limelight.pk//collections/bottoms-jeggings', 'name': 'Jeggings'}, {'url': 'https://www.limelight.pk//collections/tights', 'name': 'Tights'}, {'url': 'https://www.limelight.pk//collections/dyed-tights', 'name': 'Dyed Tights'}, {'url': 'https://www.limelight.pk//collections/striped-tights', 'name': 'Striped Tights'}, {'url': 'https://www.limelight.pk//collections/skirts', 'name': 'Skirts'}, {'url': 'https://www.limelight.pk//collections/dresses', 'name': 'Dress'}, {'url': 'https://www.limelight.pk//collections/trousers2', 'name': 'Trousers'}, {'url': 'https://www.limelight.pk//collections/basic-winter-trousers', 'name': 'Basic Winter Trousers'}, {'url': 'https://www.limelight.pk//collections/embroidered-formal', 'name': 'Embroidered & Formal Trousers'}, {'url': 'https://www.limelight.pk//collections/basic-cambric', 'name': 'Basic Cambric Trousers'}, {'url': 'https://www.limelight.pk//collections/printed-jacquard', 'name': 'Printed & Jacquard Trousers'}, {'url': 'https://www.limelight.pk//collections/silk-grip', 'name': 'Silk & Grip Trousers'}, {'url': 'https://www.limelight.pk//collections/velvet-trouser', 'name': 'Velvet Trousers'}, {'url': 'https://www.limelight.pk//collections/tights', 'name': 'Tights'}, {'url': 'https://www.limelight.pk//collections/dyed-tights', 'name': 'Dyed Tights'}, {'url': 'https://www.limelight.pk//collections/striped-tights', 'name': 'Striped Tights'}, {'url': 'https://www.limelight.pk//collections/bottoms-pants', 'name': 'Pants'}, {'url': 'https://www.limelight.pk//collections/bottoms-jeggings', 'name': 'Jeggings'}, {'url': 'https://www.limelight.pk//collections/shalwars1', 'name': 'Shalwars'}]
menBrands =  [{'url': 'https://www.limelight.pk//collections/men-kurta', 'name': 'Men Kurta'}, {'url': 'https://www.limelight.pk//collections/men-shirts', 'name': 'Men Shirts'}, {'url': 'https://www.limelight.pk//collections/men-kurta-shalwar', 'name': 'Men Suits'}, {'url': 'https://www.limelight.pk//collections/men-trousers', 'name': 'MEN Trousers'}]
kidsBrands =  [{'url': 'https://www.limelight.pk//collections/pret-girls', 'name': 'Pret - Girls'}, {'url': 'https://www.limelight.pk//collections/trouser-girls', 'name': 'Trouser - Girls'}, {'url': 'https://www.limelight.pk//collections/tights-girls', 'name': 'Tights - Girls'}, {'url': 'https://www.limelight.pk//collections/kids-bag', 'name': 'Bags - Girls'}, {'url': 'https://www.limelight.pk//collections/skirts-girls', 'name': 'Skirts'}]


def processBrands(brandArray,gender):
    for data in brandArray:
        print('site url ', data['url'])
        driver.get(data['url'])
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        for limeLight in soup.select('div[class*="product desktop-3"]'):
                   buy_url = "https://www.limelight.pk"+limeLight.find('a')['href']
                   title = limeLight.find('a')['title'].strip()
                   price = float( limeLight.find('span', {'class': 'money'}).text.strip()[3:].replace(',',''))
                   imageUrl = "https:"+limeLight.find('img')['data-src']
                   brandName = data['name']
                   # print("Image URL", imageUrl)
                   # print("Type = ",Type)
                   # print("Title = ",title)
                   # print("Buy URL = ", buy_url)
                   # print("Price = ",price)
                   dataObject = {
                       "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                       'name': title,
                       'pictures': [imageUrl],
                       'stock': 'N/A',
                       'price': price,
                       'discount': 0,
                       'salePrice': 0,
                       'description': '',
                       'tags': [gender, title],
                       'rating': random.choice(list(range(3, 5))),
                       'category': gender,
                       'colors': [],
                       'size': [],
                       'buyUrl': buy_url,
                       'gender': gender,
                       'brand': brandName,
                       'date': datetime.today(),
                       'mainBrand': 'limelight'
                   }
                   print(dataObject)
                   # mydb.freshProducts.insert_one(dataObject)
                   print('................................................................................................')

def ScrapProducts():
    try:
        allBrands = [
            {'blist': menBrands, 'name': 'men'},
            {'blist': kidsBrands, 'name': 'kids'},
            {'blist': womenBrands, 'name': 'women'},
        ]
        for brand in allBrands:
            processBrands(brand['blist'], brand['name'])
    except Exception as el:
        print("Exception occured ", el)
        driver.close()


def getAllLinks():
    scrapeUrl = "https://www.limelight.pk/"
    mainUrl = "https://www.limelight.pk/"
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    womenSoup1 = soup.findAll('li', attrs={'class': "dropdown"})[0].findAll("li")
    womenSoup2 = soup.findAll('li', attrs={'class': "dropdown"})[1].findAll("li")
    womenSoup3 = soup.findAll('li', attrs={'class': "dropdown"})[2].findAll("li")
    womenSoup4 = soup.findAll('li', attrs={'class': "dropdown"})[3].findAll("li")
    kidsSoup = soup.findAll('li', attrs={'class': "dropdown"})[8].findAll("li")
    menSoup = soup.findAll('li', attrs={'class': "dropdown"})[9].findAll("li")
    womenSoup = womenSoup1 + womenSoup2 + womenSoup3 + womenSoup4
    # print('kidsSoup ', kidsSoup)
    for brand in womenSoup:
        # print('brand ', brand)
        if (brand.find('a') != -1):
            # print(brand.find('a')['href'])
            # print(brand.find('a').text.strip())
            womenBrands.append(
                {
                    'url':  mainUrl + brand.find('a')['href'],
                    'name': brand.find('a').text.strip()
                })
    for brand in kidsSoup:
        # print('brand ', brand)
        if (brand.find('a') != -1):
            # print(brand.find('a')['href'])
            # print(brand.find('a').text.strip())
            kidsBrands.append(
                {
                    'url':  mainUrl + brand.find('a')['href'],
                    'name': brand.find('a').text.strip()
                })
    for brand in menSoup:
        # print('brand ', brand)
        if (brand.find('a') != -1):
            # print(brand.find('a')['href'])
            # print(brand.find('a').text.strip())
            menBrands.append(
                {
                    'url':  mainUrl + brand.find('a')['href'],
                    'name': brand.find('a').text.strip()
                })

    print('womenBrands = ', womenBrands)
    print('menBrands = ', menBrands)
    print('kidsBrands = ', kidsBrands)

    driver.close()
try:
    ScrapProducts()
    # getAllLinks()
except Exception as el:
    print("Exception occured ", el)
    driver.close()

# while(type_temp < len(type_array)):
#     url = "https://www.limelight.pk/collections/" + type_array[type_temp]
#     response = requests.get(url,headers=header)
#     print(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     for limeLight in soup.select('div[class*="product desktop-3"]'):
#        Type = type_array[type_temp]
#        buy_url = "https://www.limelight.pk"+limeLight.find('a')['href']
#        title = limeLight.find('a')['title'].strip()
#        price = limeLight.find('span', {'class': 'money'}).text.strip()[3:]
#        imageUrl = "https:"+limeLight.find('img')['data-src']
#        # print("Image URL", imageUrl)
#        # print("Type = ",Type)
#        # print("Title = ",title)
#        # print("Buy URL = ", buy_url)
#        # print("Price = ",price)
#        dataObject = {
#            "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
#            'name': title,
#            'pictures': [imageUrl],
#            'stock': 'N/A',
#            'price': price,
#            'discount': 0,
#            'salePrice': 0,
#            'description': '',
#            'tags': [type_array[type_temp], title],
#            'rating': random.choice(list(range(3, 5))),
#            'category': type_array[type_temp],
#            'colors': [],
#            'size': [],
#            'buyUrl': buy_url,
#            'gender': type_array[type_temp],
#            'brand': title,
#            'date': datetime.today(),
#            'mainBrand': 'limelight'
#        }
#        print(dataObject)
#        mydb.freshProducts.insert_one(dataObject)
#        counter +=1
#        print('...........................................\n')
#
#     type_temp += 1

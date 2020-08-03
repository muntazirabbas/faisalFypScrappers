from bs4 import BeautifulSoup
from datetime import datetime
import requests
import  time
import random
from selenium import webdriver
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome("C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe",chrome_options=chrome_options)
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')

kidsBrands = [
              {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Boys/Tops/Kurtas-%26-Waistcoats/c/BOYS_TOPS_KURTAS_AND_WAISTCOATS', 'name': 'Kurtas & Waistcoats'},
              {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Boys/Tops/Shirts/c/BOYS_TOPS_SHIRTS', 'name': 'Shirts'},
              {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Boys/Tops/T-Shirts-%26-Polos/c/BOYS_TOPS_TSHIRTS_AND_POLOS', 'name': 'T-Shirts & Polos'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Boys/Bottoms/Trousers-%26-Shorts/c/BOYS_BOTTOMS_TROUSERS_AND_PYJAMAS', 'name': 'Trousers & Pyjamas'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Boys/Sets/T-Shirt%2C-Shirts-%26-Shorts/c/BOYS_BOTTOMS_SHORTS', 'name': 'Shorts'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Boys/Formals/Eastern-Wear/c/BOYS_FORMALS_EASTERN_WEAR', 'name': 'Eastern Wear'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Boys/Sets/Night-Suits/c/BOYS_SETS_SLEEPWEAR', 'name': 'Sleepwear'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Girls/Tops/Frocks-%26-Jumpsuits/c/GIRLS_TOPS_FROCKS_AND_JUMPSUITS', 'name': 'Frocks & Jumpsuits'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Girls/Tops/Kutris/c/GIRLS_TOPS_KURTIS', 'name': 'Kurtis'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Girls/Tops/T-Shirts-%26-Polos/c/GIRLS_TOPS_TSHIRTS_AND_POLOS', 'name': 'T-Shirts & Polos'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Girls/Tops/Tunic-%26-Blouses/c/GIRLS_TOPS_TUNICS_AND_BLOUSES', 'name': 'Tunics & Blouses'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Girls/Bottoms/Jeans-%26-Pants/c/GIRLS_BOTTOMS_PANTS_AND_JEANS', 'name': 'Pants & Jeans'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Girls/Bottoms/Shalwars%2C-Capris-%26-Tights/c/GIRLS_BOTTOMS_SHALWARS_AND_TIGHTS', 'name': 'Shalwars & Tights'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Girls/Bottoms/Shorts-%26-Skirts/c/GIRLS_BOTTOMS_SHORTS_AND_SKIRTS', 'name': 'Shorts & Skirts'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Girls/Bottoms/Trousers-%26-Pyjamas/c/GIRLS_BOTTOMS_TROUSERS_AND_PYJAMAS', 'name': 'Trousers & Pyjamas'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Girls/Formals/Eastern-Wear/c/GIRLS_FORMALS_EASTERN_WEAR', 'name': 'Eastern Wear'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Girls/Formals/Western-Wear/c/GIRLS_FORMALS_WESTERN_WEAR', 'name': 'Western Wear'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Girls/Sets/Kameez/c/GIRLS_SETS_SHALWAR_KAMEEZ', 'name': 'Shalwar Kameez'}, {'url': 'https://www.minnieminors.com//minnieminors-pk/en/Categories/Girls/Sets/Night-Suits/c/GIRLS_SETS_SLEEPWEAR', 'name': 'Sleepwear'}
]

print('start scrapping')

def getAllLinks():
    scrapeUrl = "https://www.minnieminors.com/minnieminors-pk/en/"
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    kidsSoup = soup.findAll('li', attrs={'class': "yCmsComponent nav__link--secondary"})
    # print('kidsSoup ', kidsSoup)
    for brand in kidsSoup:
        # print('brand ', brand)
        if (brand.find('a') != -1):
            # print(brand.find('a')['href'])
            # print(brand.find('a').text.strip())
            kidsBrands.append(
                {
                    'url': "https://www.minnieminors.com/" + brand.find('a')['href'],
                    'name': brand.find('a').text.strip()
                })
    print('kidsBrands = ', kidsBrands)
    driver.close()

def processBrands(brandArray,type, collectionName):
    mainUrl = "https://www.minnieminors.com"
    for data in brandArray:
        print('site url ', data['url'])
        driver.get(data['url'])
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'lxml')

        for nestedMini in soup.findAll('div', {'class': 'product-item'}):
            price = 0
            if(nestedMini.find('p', {'class': 'price'})):
                price = nestedMini.find('p', {'class': 'price'}).text.strip()[3:].strip().replace(",", "")
            else:
                price = nestedMini.find('div', {'class': 'price'}).text.strip()[3:].strip().replace(",", "")

            title = nestedMini.find('a', {'class': 'thumb'})['title'].lower()
            buy_url = mainUrl + nestedMini.find('a', {'class': 'thumb'})['href']
            imageUrl = mainUrl + nestedMini.find('a', {'class': 'thumb'}).find('img')['src']
            brandName = data['name']
            dataObject = {
                 "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                 'name': title,
                 'pictures': [imageUrl],
                 'stock': 0,
                 'price': price,
                 'discount': 0,
                 'salePrice': 0,
                 'description': '',
                 'tags': [brandName],
                 'rating': random.choice(list(range(3, 5))),
                 'category': type,
                 'colors': [],
                 'size': [],
                 'buyUrl': buy_url,
                 'gender': type,
                 'brand': brandName,
                 'date': datetime.today(),
                 'mainBrand': 'minnieminors'
            }
            print('product ... ', dataObject)
            mydb.freshProducts.insert_one(dataObject)
            print('................................................................................................')

def ScrapProducts(collectionName):
    try:
        allBrands = [
            {'blist': kidsBrands, 'name': 'kids'},
        ]
        for brand in allBrands:
            processBrands(brand['blist'], brand['name'], collectionName)
    except Exception as el:
        print("Exception occured ", el)
        driver.close()

try:
    ScrapProducts('freshProducts')
    # getAllLinks()
except Exception as el:
    print("Exception occured ", el)
    driver.close()

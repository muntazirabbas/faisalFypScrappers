import time
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
driver = webdriver.Chrome("C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe",chrome_options=chrome_options)
# driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
womenBrands =  [{'url': 'https://pk.sapphireonline.pk//collections/pop-vol-4-2020', 'name': 'Pop'}, {'url': 'https://pk.sapphireonline.pk//collections/daily-vol-4-2020', 'name': 'Daily'}, {'url': 'https://pk.sapphireonline.pk//collections/classic-vol-4-2020', 'name': 'Classic'}, {'url': 'https://pk.sapphireonline.pk//collections/serene-vol-4-2020', 'name': 'Serene'}, {'url': 'https://pk.sapphireonline.pk//collections/signature-vol-4-2020', 'name': 'Signature'}, {'url': 'https://pk.sapphireonline.pk//collections/luxe-vol-4-2020', 'name': 'Luxe'}, {'url': 'https://pk.sapphireonline.pk//collections/lawn-daily-vol-3-2020', 'name': 'Daily'}, {'url': 'https://pk.sapphireonline.pk//collections/lawn-pop-vol-3-2020', 'name': 'Pop'}, {'url': 'https://pk.sapphireonline.pk//collections/classic-vol-2-2020', 'name': 'Classic'}, {'url': 'https://pk.sapphireonline.pk//collections/lawn-signature-vol-3-2020', 'name': 'Signature'}, {'url': 'https://pk.sapphireonline.pk//collections/lawn-serene-vol-3-2020', 'name': 'Serene'}, {'url': 'https://pk.sapphireonline.pk//pages/eid-edition', 'name': 'Eid Edition'}, {'url': 'https://pk.sapphireonline.pk//collections/eid-edition-ready-to-wear', 'name': 'Eid Edition'}, {'url': 'https://pk.sapphireonline.pk//collections/printed', 'name': 'Printed'}, {'url': 'https://pk.sapphireonline.pk//collections/solid-colored', 'name': 'Solid Colored'}, {'url': 'https://pk.sapphireonline.pk//collections/ready-to-wear-outfits', 'name': 'Ready To Wear Outfits'}, {'url': 'https://pk.sapphireonline.pk//collections/scarves-dupattas', 'name': 'Scarves / Dupattas'}, {'url': 'https://pk.sapphireonline.pk//collections/embroidered', 'name': 'Embroidered'}, {'url': 'https://pk.sapphireonline.pk//collections/silk-tunics', 'name': 'Silk Tunics'}, {'url': 'https://pk.sapphireonline.pk//collections/printed-trousers', 'name': 'Printed Trousers'}, {'url': 'https://pk.sapphireonline.pk//collections/embroidered-trousers', 'name': 'Embroidered Trousers'}, {'url': 'https://pk.sapphireonline.pk//collections/cotton-trousers', 'name': 'Cotton Trousers'}, {'url': 'https://pk.sapphireonline.pk//collections/silk-pants', 'name': 'Silk Pants'}, {'url': 'https://pk.sapphireonline.pk//collections/shalwars', 'name': 'Shalwars'}, {'url': 'https://pk.sapphireonline.pk//collections/jumpsuits', 'name': 'Jumpsuits'}, {'url': 'https://pk.sapphireonline.pk//collections/dresses', 'name': 'Dresses'}, {'url': 'https://pk.sapphireonline.pk//collections/jeans', 'name': 'Jeans'}, {'url': 'https://pk.sapphireonline.pk//collections/shirts-blouses', 'name': 'Shirts & Blouses'}, {'url': 'https://pk.sapphireonline.pk//collections/women-t-shirts', 'name': 'T-Shirts'}, {'url': 'https://pk.sapphireonline.pk//collections/women-blazers', 'name': 'Blazers'}, {'url': 'https://pk.sapphireonline.pk//collections/western-pants', 'name': 'Pants'}, {'url': 'https://pk.sapphireonline.pk//collections/women-skirts', 'name': 'Skirts'}, {'url': 'https://pk.sapphireonline.pk//collections/western-scarves', 'name': 'Scarves'}, {'url': 'https://pk.sapphireonline.pk//collections/western-tights', 'name': 'Tights'}, {'url': 'https://pk.sapphireonline.pk//collections/active-tops', 'name': 'Tops'}, {'url': 'https://pk.sapphireonline.pk//collections/bottoms-1', 'name': 'Bottoms'},]
menBrands = [{'url': 'https://pk.sapphireonline.pk//collections/kurtas', 'name': 'Kurtas'}, {'url': 'https://pk.sapphireonline.pk//collections/kurta-shalwar', 'name': 'Kurta Shalwar'}, {'url': 'https://pk.sapphireonline.pk//collections/waistcoats', 'name': 'Waistcoats'}, {'url': 'https://pk.sapphireonline.pk//collections/men-s-bottoms', 'name': 'Bottoms'}, {'url': 'https://pk.sapphireonline.pk//collections/menswear-unstitched', 'name': 'Unstitched'}, {'url': 'https://pk.sapphireonline.pk//collections/mens-chinos', 'name': 'Chinos'}, {'url': 'https://pk.sapphireonline.pk//collections/mens-shirts', 'name': 'Shirts'}, {'url': 'https://pk.sapphireonline.pk//collections/mens-denim', 'name': 'Denim'}, {'url': 'https://pk.sapphireonline.pk//pages/unstitched-catalogue', 'name': 'Unstitched Catalogue'},]
kidsBrands =  [{'url': 'https://pk.sapphireonline.pk//collections/boys-shirts', 'name': 'Shirts'}, {'url': 'https://pk.sapphireonline.pk//collections/boys-t-shirts', 'name': 'T-Shirts'}, {'url': 'https://pk.sapphireonline.pk//collections/boys-polos', 'name': 'Polos'}, {'url': 'https://pk.sapphireonline.pk//collections/boys-denims', 'name': 'Denim'}, {'url': 'https://pk.sapphireonline.pk//collections/boys-pants', 'name': 'Pants'}, {'url': 'https://pk.sapphireonline.pk//collections/boys-shorts', 'name': 'Shorts'}, {'url': 'https://pk.sapphireonline.pk//collections/boys-combos', 'name': 'Combos'}, {'url': 'https://pk.sapphireonline.pk//collections/girls-t-shirts', 'name': 'T-Shirts'}, {'url': 'https://pk.sapphireonline.pk//collections/blouses', 'name': 'Blouses'}, {'url': 'https://pk.sapphireonline.pk//collections/girls-dresses', 'name': 'Dresses'}, {'url': 'https://pk.sapphireonline.pk//collections/girls-jumpsuits', 'name': 'Jumpsuits'}, {'url': 'https://pk.sapphireonline.pk//collections/girls-skirts', 'name': 'Skirts'}, {'url': 'https://pk.sapphireonline.pk//collections/girls-shorts', 'name': 'Shorts'}, {'url': 'https://pk.sapphireonline.pk//collections/girls-denim', 'name': 'Denim'}, {'url': 'https://pk.sapphireonline.pk//collections/girls-pants', 'name': 'Pants'}, {'url': 'https://pk.sapphireonline.pk//collections/tights-1', 'name': 'Tights'}, {'url': 'https://pk.sapphireonline.pk//collections/boys-kurtas', 'name': 'Kurtas'}, {'url': 'https://pk.sapphireonline.pk//collections/boys-kurta-shalwar', 'name': 'Kurta Shalwar'}, {'url': 'https://pk.sapphireonline.pk//collections/boys-waistcoats', 'name': 'Waistcoats'}, {'url': 'https://pk.sapphireonline.pk//collections/boys-trousers', 'name': 'Trousers'}, {'url': 'https://pk.sapphireonline.pk//collections/girls-kurtas', 'name': 'Kurtas'}, {'url': 'https://pk.sapphireonline.pk//collections/girls-outfits', 'name': 'Outfits'}, {'url': 'https://pk.sapphireonline.pk//collections/girls-trousers', 'name': 'Trousers'}, {'url': 'https://pk.sapphireonline.pk//collections/boys-bedding', 'name': 'Boys'}, {'url': 'https://pk.sapphireonline.pk//collections/girls-bedding', 'name': 'Girls'}, {'url': 'https://pk.sapphireonline.pk//collections/baby-cot', 'name': 'Baby Cots'}]


def processBrands(brandArray,gender):
    for data in brandArray:
        print('site url ', data['url'])
        driver.get(data['url'])
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        for sapphire in soup.select('div[class*="grid-item col-6 col-md-4 col-xl-3 four-columns"]'):
               buy_url = "https://pk.sapphireonline.pk"+sapphire.find('a')['href']
               title = sapphire.find('img')['alt'].strip()
               price = float(sapphire.find('span', {'class': 'money'}).text.strip()[3:-3].replace(',',''))
               imageUrl = sapphire.find('div', attrs={'class' : 'product-top'}).find('img')['data-src']
               brandName = data['name']
               sizes = []
               if(sapphire.find('ul', attrs={'class': 'product-grid-options-size'})):
                   sizeDiv = sapphire.find('ul', attrs={'class': 'product-grid-options-size'}).findAll('li')
                   for _size in sizeDiv:
                       if (_size):
                           # print('size => ',_size.text)
                           sizes.append(_size.text.strip().lower())
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
                   'size': sizes,
                   'buyUrl': buy_url,
                   'gender': gender,
                   'brand': brandName,
                   'date': datetime.today(),
                   'mainBrand': 'sapphire'
               }
               print(dataObject)
               mydb.freshProducts.insert_one(dataObject)
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
    scrapeUrl = "https://pk.sapphireonline.pk/"
    mainUrl = "https://pk.sapphireonline.pk/"
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    womenSoup1 = soup.findAll('a', attrs={'class': "third-menu "})
    print("womensoup ", womenSoup1)
    for brand in womenSoup1:
        if (brand != -1):
            womenBrands.append(
                {
                    'url':  mainUrl + brand['href'],
                    'name': brand.text.strip()
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
import random
from datetime import date,datetime
import requests
from bs4 import BeautifulSoup
from fake_useragent import  UserAgent
from selenium import webdriver
from datetime import date
ua          = UserAgent()
header      = {'user-agent':ua.chrome}
# brand_array = []
# type_temp =0
# driver = webdriver.chrome('E:/others Efolder/scraping/zia_fyp_scraping/chromedriver_win32')
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
# type_array = ["kids",'woman','accessories',"men"]

womenBrands = [{'url': 'https://pk.khaadi.com/new-in.html?material=219', 'name': 'cambric'}, {'url': 'https://pk.khaadi.com/new-in.html?material=227', 'name': 'brosha'}, {'url': 'https://pk.khaadi.com/new-in.html?material=229', 'name': 'raw silk'}, {'url': 'https://pk.khaadi.com/new-in.html?material=231', 'name': 'denim'}, {'url': 'https://pk.khaadi.com/new-in.html?material=232', 'name': 'viscose'}, {'url': 'https://pk.khaadi.com/new-in.html?material=233', 'name': 'khaddar'}, {'url': 'https://pk.khaadi.com/new-in.html?material=234', 'name': 'marina'}, {'url': 'https://pk.khaadi.com/new-in.html?material=236', 'name': 'poly viscose'}, {'url': 'https://pk.khaadi.com/new-in.html?material=237', 'name': 'sateen'}, {'url': 'https://pk.khaadi.com/new-in.html?material=238', 'name': 'jacquard'}, {'url': 'https://pk.khaadi.com/new-in.html?material=239', 'name': 'silk'}, {'url': 'https://pk.khaadi.com/new-in.html?material=245', 'name': 'chiffon silk'}, {'url': 'https://pk.khaadi.com/new-in.html?material=246', 'name': 'chiffon'}, {'url': 'https://pk.khaadi.com/new-in.html?material=247', 'name': 'organza'}, {'url': 'https://pk.khaadi.com/new-in.html?material=248', 'name': 'handwoven'}, {'url': 'https://pk.khaadi.com/new-in.html?material=250', 'name': 'default'}, {'url': 'https://pk.khaadi.com/new-in.html?material=251', 'name': 'hand woven'}, {'url': 'https://pk.khaadi.com/new-in.html?material=253', 'name': 'woolen'}, {'url': 'https://pk.khaadi.com/new-in.html?material=254', 'name': 'acrylic'}, {'url': 'https://pk.khaadi.com/new-in.html?material=255', 'name': 'polyester'}, {'url': 'https://pk.khaadi.com/new-in.html?material=256', 'name': 'cotton stretch'}, {'url': 'https://pk.khaadi.com/new-in.html?material=257', 'name': 'schiffli'}, {'url': 'https://pk.khaadi.com/new-in.html?material=258', 'name': 'cross hatch denim'}, {'url': 'https://pk.khaadi.com/new-in.html?material=260', 'name': 'cross hatch'}, {'url': 'https://pk.khaadi.com/new-in.html?material=261', 'name': 'velvet'}, {'url': 'https://pk.khaadi.com/new-in.html?material=264', 'name': 'metallica'}, {'url': 'https://pk.khaadi.com/new-in.html?material=272', 'name': 'indian chiffon'}, {'url': 'https://pk.khaadi.com/new-in.html?material=273', 'name': 'tissue silk'}, {'url': 'https://pk.khaadi.com/new-in.html?material=274', 'name': 'viscose silk'}, {'url': 'https://pk.khaadi.com/new-in.html?material=275', 'name': 'polyester net'}, {'url': 'https://pk.khaadi.com/new-in.html?material=280', 'name': 'light khaddar'}, {'url': 'https://pk.khaadi.com/new-in.html?material=281', 'name': 'duck'}, {'url': 'https://pk.khaadi.com/new-in.html?material=282', 'name': 'dobby'}, {'url': 'https://pk.khaadi.com/new-in.html?material=284', 'name': 'oak silk'}, {'url': 'https://pk.khaadi.com/new-in.html?material=285', 'name': 'zari net'}, {'url': 'https://pk.khaadi.com/new-in.html?material=287', 'name': 'flannel'}, {'url': 'https://pk.khaadi.com/new-in.html?material=289', 'name': 'cotton net'}, {'url': 'https://pk.khaadi.com/new-in.html?material=290', 'name': 'self jacquard'}, {'url': 'https://pk.khaadi.com/new-in.html?material=291', 'name': 'silk viscose'}, {'url': 'https://pk.khaadi.com/new-in.html?material=297', 'name': 'plastic'}]
kidsBrands = [{'url': 'https://pk.khaadi.com/kids.html?material=216', 'name': 'poplin'}, {'url': 'https://pk.khaadi.com/kids.html?material=218', 'name': 'jersey'}, {'url': 'https://pk.khaadi.com/kids.html?material=219', 'name': 'cambric'}, {'url': 'https://pk.khaadi.com/kids.html?material=231', 'name': 'denim'}, {'url': 'https://pk.khaadi.com/kids.html?material=232', 'name': 'viscose'}, {'url': 'https://pk.khaadi.com/kids.html?material=233', 'name': 'khaddar'}, {'url': 'https://pk.khaadi.com/kids.html?material=250', 'name': 'default'}, {'url': 'https://pk.khaadi.com/kids.html?material=251', 'name': 'hand woven'}, {'url': 'https://pk.khaadi.com/kids.html?material=261', 'name': 'velvet'}, {'url': 'https://pk.khaadi.com/kids.html?material=287', 'name': 'flannel'}, {'url': 'https://pk.khaadi.com/kids.html?material=306', 'name': 'corduroy'}, {'url': 'https://pk.khaadi.com/kids.html?material=307', 'name': 'terry'}, {'url': 'https://pk.khaadi.com/kids.html?material=308', 'name': 'twill'}, {'url': 'https://pk.khaadi.com/kids.html?material=313', 'name': 'cotton yd'}, {'url': 'https://pk.khaadi.com/kids.html?material=314', 'name': 'lycra jersey'}]

# scrapeUrl = "https://www.khaadi.com/pk/kids/girls-western-1032.html"
# mainSiteUrl = "https://www.khaadi.com/pk"


jsonData= []
def getBrandData(soup,brandName,gender):
    print('in brand data ', brandName)
    print("soup ____",soup)
    for khad in soup:
        if(khad):
            print('in final loop')
            price = khad.find('span', {'class': 'price'}).text.strip()[3:]
            buy_url = khad.find('a')['href']
            title = khad.find('a', {'class': "product-item-link"}).text.strip()
            imageURL = ""
            for i in khad.findAll('img'):
                imageURL = i['src']

            print("Type = ", gender)
            print("Brand = ", brandName)
            print("Title = ", title)
            print("Buy URL = ", buy_url)
            print("Price = ", price)
            print("Date = ", date.today())
            print('img = ', imageURL)
            print('............................................................')
            colors = ["black", "gray", "red", "pink", "white", "green", "blue"]
            size = random.choice(
                [
                    ['100 CM', '90 CM', '95 CM'],
                    ['M', 'L', 'XL'],
                    ['XS', 'S', '2T'],
                    ['3T', '4T', '7'],
                    ['8', '9']
                ])
            mainBrands = ['bonanza', 'outfitters', 'breakout', 'khaadi', 'engine', 'gulahmed', 'junaidjamshed', 'levi']
            dataObject = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(
                    list(range(55, 5000))),
                'name': title,
                'pictures': [imageURL],
                'stock': random.choice(list(range(10, 400))),
                'price': int(price.strip().replace(',', '')),
                'discount': random.choice(list(range(0, 100))),
                'salePrice': int(price.strip().replace(',', '')) + random.choice([0, 300]),
                'description': '',
                'tags': [gender, brandName],
                'rating': random.choice(list(range(0, 5))),
                'category': gender,
                'colors': [random.choice(colors), random.choice(colors), random.choice(colors)],
                'size': size,
                'buyUrl': buy_url,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'khaadi'
            }
            # jsonData.append(dataObject)
            print("data________", dataObject)
def processBrands(brandArray,type):
    for data in brandArray:
        print('site url ', data['url'])
        driver.get(data['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        # khaadi = soup.findAll("li", {"class": "item product product-item"})
        khaadi = soup.select('li[class*="item product product-item"]')
        getBrandData(khaadi,data['name'],type)


# def startScraping(brandArray,type):
#     print('start scrapping ', brandArray)
#     processBrands(brandArray,type)


def getAllLinks(soup):
    allUrls = soup.findAll('a', attrs={'class': 'mgs-ajax-layer-item'})[8:23]
    # print('soup_____', allUrls)
    myarray = []
    for brand in allUrls:
        # print("brand_____",brand)
        if(brand['href']):
            linkUrl = brand['href']
            name = brand.contents[0].strip()
            print('anchor____', linkUrl)
            print('name______', name)
            myarray.append(
                        {
                            'url': linkUrl,
                            'name': name
                        })
        print('........................................................................')
    driver.close()
    print('womenBrands ', myarray)

try:
    allBrands = [ {'blist': womenBrands, 'name': 'women'},{'blist': kidsBrands, 'name': 'kids'}]
    for brand in allBrands:
        processBrands(kidsBrands,'women')
except Exception as el:
    print("Error opening site  ", el)
    driver.close()

# try:
#     scrapeUrl = 'https://pk.khaadi.com/kids.html'
#     driver.get(scrapeUrl)
#     soup = BeautifulSoup(driver.page_source, 'lxml')
#     getAllLinks(soup)
# except Exception as el:
#     print("Error opening site  ", el)
#     driver.close()

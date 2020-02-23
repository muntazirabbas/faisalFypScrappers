import requests
from bs4 import BeautifulSoup
from fake_useragent import  UserAgent
from selenium import webdriver
from datetime import date
ua          = UserAgent()
header      = {'user-agent':ua.chrome}
# brand_array = []
# type_temp =0

driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
type_array = ["kids",'woman','accessories',"men"]

womenBrands =  [{'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/lawn.html', 'name': 'Lawn'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/cambric.html', 'name': 'Cambric'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/chiffon.html', 'name': 'Chiffon'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/khaddar.html', 'name': 'Khaddar'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/jacquard.html', 'name': 'Jacquard'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/marina.html', 'name': 'Marina'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/velvet.html', 'name': 'Velvet'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/brosha.html', 'name': 'Brosha'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/schiffli.html', 'name': 'Schiffli'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/light-khaddar.html', 'name': 'Light Khaddar'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/medium-silk.html', 'name': 'Medium Silk'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/cross-hatch.html', 'name': 'Cross Hatch'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/poly-viscose.html', 'name': 'Poly Viscose'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/yarn-dyed.html', 'name': 'Yarn Dyed'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/karandi.html', 'name': 'Karandi'}, {'url': 'https://www.khaadi.com/pk/unstitched11/by-fabric/oak-silk.html', 'name': 'Oak Silk'}]
menBrands = []
kidsBrands =  [{'url': 'https://www.khaadi.com/pk/kids/girls-western/blouses.html', 'name': 'Blouses'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/t-shirts.html', 'name': 'T-Shirts'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/dresses.html', 'name': 'Dresses'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/tights-girls.html', 'name': 'Tights'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/pants.html', 'name': 'Pants'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/de-nim.html', 'name': 'Denim'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/culottes.html', 'name': 'Culottes'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/lounge-wear.html', 'name': 'Lounge-wear'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/outerwear.html', 'name': 'Outerwear'},{'url': 'https://www.khaadi.com/pk/kids/girls-western/blouses.html', 'name': 'Blouses'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/t-shirts.html', 'name': 'T-Shirts'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/dresses.html', 'name': 'Dresses'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/tights-girls.html', 'name': 'Tights'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/pants.html', 'name': 'Pants'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/de-nim.html', 'name': 'Denim'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/culottes.html', 'name': 'Culottes'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/lounge-wear.html', 'name': 'Lounge-wear'}, {'url': 'https://www.khaadi.com/pk/kids/girls-western/outerwear.html', 'name': 'Outerwear'}, {'url': 'https://www.khaadi.com/pk/kids/boys-western/denim.html', 'name': 'Denim'}, {'url': 'https://www.khaadi.com/pk/kids/boys-western/t-shirts.html', 'name': 'T-Shirts'}, {'url': 'https://www.khaadi.com/pk/kids/boys-western/shirts.html', 'name': 'Shirts'}, {'url': 'https://www.khaadi.com/pk/kids/boys-western/lounge-wear.html', 'name': 'Lounge-wear'}, {'url': 'https://www.khaadi.com/pk/kids/boys-western/shorts.html', 'name': 'Shorts'}, {'url': 'https://www.khaadi.com/pk/kids/boys-western/trousers.html', 'name': 'Trousers'}, {'url': 'https://www.khaadi.com/pk/kids/boys-western/outerwear.html', 'name': 'Outerwear'}]

# scrapeUrl = "https://www.khaadi.com/pk/kids/girls-western-1032.html"
# mainSiteUrl = "https://www.khaadi.com/pk"


jsonData= []
def getBrandData(soup,brandName,type):
    for khad in soup:
        price = khad.find('span', {'class': 'price'}).text.strip()
        buy_url = khad.find('a')['href']
        title = khad.find('a', {'class': "product-item-link"}).text.strip()
        imageUrl = ""
        for i in khad.findAll('img'):
            imageUrl = i['src']

        print("Type = ", type)
        print("Brand = ", brandName)
        print("Title = ", title)
        print("Buy URL = ", buy_url)
        print("Price = ", price)
        print("Date = ", date.today())
        print('img = ', imageUrl)
        jsonData.append({
            'name': title,
            'buyUrl': buy_url,
            'price': price,
            'Type': type,
            'subType': brandName,
            'date': date.today(),
            'image': imageUrl
        })
        print('............................................................')

def processBrands(brandArray,type):
    for data in brandArray:
        driver.get(data['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        khaadi = soup.findAll("li", {"class": "item product product-item"})
        getBrandData(khaadi,data['name'],type)


def startScraping(brandArray,type):
    processBrands(brandArray,type)


def getAllLinks(scrapeUrl):
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    brandSoup = soup.findAll('ul', attrs={'class': 'list-category'})[0]
    print('soup_____', brandSoup)
    for brand in brandSoup:
        # print("brand_",brand)
        if(brand.find('a') != -1):
            print(brand.find('a')['href'])
            print(brand.find('a').text.strip())
            kidsBrands.append(
                        {
                            'url':brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
        print('........................................................................')
    driver.close()
    print('kidsBrands ', kidsBrands)

# try:
#     startScraping(kidsBrands,'kids')
# except Exception as el:
#     print("Error opening site  ", el)
#     driver.close()

try:
    scrapeUrl = "https://www.khaadi.com/pk/kids/boys-western-1036.html"
    getAllLinks(scrapeUrl)
except Exception as el:
    print("Error opening site  ", el)
    driver.close()

from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
from datetime import date
menBrands =  [{'url': 'https://www.breakout.com.pk//stranger-things-collection', 'name': 'STRANGER THINGS COLLECTION'}, {'url': 'https://www.breakout.com.pk//new-in', 'name': 'NEW IN'}, {'url': 'https://www.breakout.com.pk//tees', 'name': 'TEES'}, {'url': 'https://www.breakout.com.pk//polos', 'name': 'POLOS'}, {'url': 'https://www.breakout.com.pk//shirts-2', 'name': 'Shirts'}, {'url': 'https://www.breakout.com.pk//denim', 'name': 'Denim'}, {'url': 'https://www.breakout.com.pk//non-denim', 'name': 'TROUSERS / CHINOS'}, {'url': 'https://www.breakout.com.pk//joggers', 'name': 'JOGGERS'}, {'url': 'https://www.breakout.com.pk//sweater-3', 'name': 'Sweaters'}, {'url': 'https://www.breakout.com.pk//coat-4', 'name': 'Coats/Blazers'}, {'url': 'https://www.breakout.com.pk//upper-3', 'name': 'Sweatshirts / hoodies'}, {'url': 'https://www.breakout.com.pk//jacket-3', 'name': 'Jackets'}, {'url': 'https://www.breakout.com.pk//shoes-2', 'name': 'Shoes'}, {'url': 'https://www.breakout.com.pk//bags-3', 'name': 'BAGS'}, {'url': 'https://www.breakout.com.pk//belts', 'name': 'BELTS'}, {'url': 'https://www.breakout.com.pk//wallets', 'name': 'WALLETS'}, {'url': 'https://www.breakout.com.pk//perfumes', 'name': 'PERFUMES'}]
femaleBrands = [{'url': 'https://www.breakout.com.pk//stranger-things-collection-2', 'name': 'STRANGER THINGS COLLECTION'}, {'url': 'https://www.breakout.com.pk//new-in-2', 'name': 'NEW IN'}, {'url': 'https://www.breakout.com.pk//tops-3', 'name': 'Tops'}, {'url': 'https://www.breakout.com.pk//shirts-7', 'name': 'Shirts'}, {'url': 'https://www.breakout.com.pk//bottom', 'name': 'Denim and trousers'}, {'url': 'https://www.breakout.com.pk//shawls-2', 'name': 'Shawls/Capes'}, {'url': 'https://www.breakout.com.pk//sweater-4', 'name': 'Sweaters'}, {'url': 'https://www.breakout.com.pk//upper-4', 'name': 'Uppers / Sweatshirts'}, {'url': 'https://www.breakout.com.pk//jacket-4', 'name': 'Jackets'}, {'url': 'https://www.breakout.com.pk//shoes', 'name': 'Shoes'}, {'url': 'https://www.breakout.com.pk//bags-4', 'name': 'BAGS'}, {'url': 'https://www.breakout.com.pk//scarves', 'name': 'SCARVES'}, {'url': 'https://www.breakout.com.pk//perfumes-2', 'name': 'PERFUMES'}]
kidsBrands = [{'url': 'https://www.breakout.com.pk//new-in-5', 'name': 'NEW IN'}, {'url': 'https://www.breakout.com.pk//tees-5', 'name': 'Tees'}, {'url': 'https://www.breakout.com.pk//tops-4', 'name': 'Tops'}, {'url': 'https://www.breakout.com.pk//sweaters-3', 'name': 'Sweaters'}, {'url': 'https://www.breakout.com.pk//jackets-3', 'name': 'Jackets'}, {'url': 'https://www.breakout.com.pk//uppers-3', 'name': 'Uppers'}, {'url': 'https://www.breakout.com.pk//bottoms-5', 'name': 'Bottoms'}, {'url': 'https://www.breakout.com.pk//accessories-shoes-3', 'name': 'Accessories & Shoes'},{'url': 'https://www.breakout.com.pk//new-in-6', 'name': 'NEW IN'}, {'url': 'https://www.breakout.com.pk//tees-6', 'name': 'Tees'}, {'url': 'https://www.breakout.com.pk//tops-5', 'name': 'Tops'}, {'url': 'https://www.breakout.com.pk//sweaters-4', 'name': 'Sweaters'}, {'url': 'https://www.breakout.com.pk//jackets-4', 'name': 'Jackets'}, {'url': 'https://www.breakout.com.pk//uppers-4', 'name': 'Uppers'}, {'url': 'https://www.breakout.com.pk//bottoms-6', 'name': 'Bottoms'}, {'url': 'https://www.breakout.com.pk//accessories-shoes-4', 'name': 'Accessories & Shoes'}]
brand_count = 0
scrapeUrl = ""

def openSitePage(menBrands, type):
    print("menBrands " , menBrands)
    for sitePage in menBrands:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],type)

jsonData = []
def processSitePageSoup(soup, brandName,type):
    products = soup.findAll('div',{'class':'product-item'})
    for product in products:
        if(product.find('div',{'class':'details'})):
            # print("product======>>>>",product.find('div',{'class':'details'}))
            title = product.find('div',{'class':'details'}).findAll('a')[0].text
            buyUrl = product.find('div',{'class':'details'}).findAll('a')[0]['href']
            price = 0
            if (product.find('div',{'class':'details'}).find('div', {'class': 'prices'}).findAll('span')[1]):
                price = (product.find('div',{'class':'details'}).find('div', {'class': 'prices'}).findAll('span')[1]).text
            image = product.find('div',{'class':'picture'}).find('img')['src']
            print("Type = ", type)
            print("Brand = ", brandName)
            print("Title = ", title)
            print("Buy URL = ",  'https://www.breakout.com.pk' +buyUrl)
            print("Price = ", price)
            print("Date = ", date.today())
            print('img = ', image)
            jsonData.append({
                'name': title,
                'buyUrl': 'https://www.breakout.com.pk' +buyUrl,
                'price': price,
                'Type': type,
                'subType': brandName,
                'date': date.today(),
                'image': image
            })
            print('jsonData ', jsonData)
            print('...........................................................................................')

print('starting scrapping')

try:
    openSitePage(kidsBrands, 'kids')
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

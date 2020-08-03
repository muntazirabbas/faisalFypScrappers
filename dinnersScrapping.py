import random
from datetime import datetime
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
menBrands = [
            {'url': 'https://diners.com.pk/collections/jeans', 'name': 'Jeans'},
            {'url': 'https://diners.com.pk/collections/shirts', 'name': 'Shirts'},
            {'url': 'https://diners.com.pk/collections/trousers', 'name': 'Trousers'},
            {'url': 'https://diners.com.pk/collections/suiting-blazers', 'name': 'Blazzers'},
            {'url': 'https://diners.com.pk/collections/t-shirts', 'name': 'T-Shirts'},
    {'url': 'https://diners.com.pk/collections/shorts', 'name': 'Shorts'},
    {'url': 'https://diners.com.pk/collections/ethnic-wear', 'name': 'Ethnic'},
]

kidsBrands = [{'url': 'https://diners.com.pk//collections/boys-t-shirts', 'name': 'T-Shirts'}, {'url': 'https://diners.com.pk/https://diners.com.pk/collections/boy-shirts', 'name': 'Shirts'}, {'url': 'https://diners.com.pk//collections/kurta-boy', 'name': 'Kurta Shalwar'}, {'url': 'https://diners.com.pk//collections/polo', 'name': 'Polo'}, {'url': 'https://diners.com.pk//collections/jeans-1', 'name': 'Jeans'}, {'url': 'https://diners.com.pk//collections/chinos-boys', 'name': 'Chinos'}, {'url': 'https://diners.com.pk//collections/shalwar-boy', 'name': 'Shalwar'}, {'url': 'https://diners.com.pk//collections/suit', 'name': 'Suit'}, {'url': 'https://diners.com.pk//collections/shirts-girls', 'name': 'Shirts'}, {'url': 'https://diners.com.pk//collections/t-shirts-girl', 'name': 'T-shirt'}, {'url': 'https://diners.com.pk//collections/girls-kurti', 'name': 'Kurti'}, {'url': 'https://diners.com.pk//collections/frocks', 'name': 'Frocks'}, {'url': 'https://diners.com.pk//collections/jeans-girl', 'name': 'Jeans'}, {'url': 'https://diners.com.pk//collections/tights-girl', 'name': 'Tights'}, {'url': 'https://diners.com.pk//collections/girls-trouser', 'name': 'Trousers'}, {'url': 'https://diners.com.pk//collections/kurti-teen-girl', 'name': 'Kurti'}, {'url': 'https://diners.com.pk//collections/shirts-teen-girls', 'name': 'Shirts'}, {'url': 'https://diners.com.pk//collections/t-shirts-teen-girl', 'name': 'T-shirts'}, {'url': 'https://diners.com.pk//collections/frocks-teen-girl', 'name': 'Frocks'}]
womenBrands = [{'url': 'https://diners.com.pk/collections/ready-to-wear', 'name': 'Ready to Wear'},{'url': 'https://diners.com.pk/collections/unstitched', 'name': 'Unstitched'},{'url': 'https://diners.com.pk/collections/sohaye-trousers', 'name': 'Bottoms'},]

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
    elif "cream" in color:
        return "cream"
    elif "mehroon" in color:
        return "mehroon"
    elif "pink" in color:
        return "pink"
    elif "grey" in color:
        return "grey"
    else:
        return "other"

def openSitePage(brandData, type):
    for sitePage in brandData:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],type)

jsonData = []
def processSitePageSoup(soup, brandName,gender):
    webUrl = "https://diners.com.pk/"
    products = soup.findAll('div', attrs={'class': 'grid-item col-6 col-md-4'})
    # print('products ', products)
    for product in products:
        if(product):
            # print("product======>>>>",product)
            title = product.find('a',{'class' : 'product-title'}).text.strip()
            # print('title ', title)
            buyUrl =  webUrl + product.find('a',{'class' : 'product-title'})['href']
            # print('b-url ', buyUrl)

            price = 0
            if(product.findAll('span', attrs={'class' : 'money'})):
                price = product.findAll('span', attrs={'class': 'money'})[-1].text.strip()[3:]
            imageUrl = ''
            if(product.find('img')['data-srcset']):
                imageUrl = 'https:' + product.find('img')['data-srcset']
            # print('image ', imageUrl)
            sizes = []
            if(product.find('ul' , attrs={'class' : 'sizes-list'})):
                for _size in product.find('ul' , attrs={'class' : 'sizes-list'}).findAll('li'):
                    sizes.append(_size.text.strip())
            color = colorAssignment(title.lower())
            price = float(price.replace(',',''))
            dataObject = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                'name': title,
                'price': price,
                'pictures': [imageUrl],
                'stock': 'N/A',
                'discount': 0,
                'salePrice': 0,
                'description': '',
                'tags': [gender, brandName],
                'rating': 'N/A',
                'category': gender,
                'colors': [color],
                'size': sizes,
                'buyUrl': buyUrl,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'diners'
            }
            print('data_____',dataObject)
            mydb.freshProducts.insert_one(dataObject)
print("starting scrapping")

def getAllLinks():
    scrapeUrl = "https://diners.com.pk/"
    webUrl = "https://diners.com.pk/"
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source,'lxml')
    # menSoup = soup.findAll('li', attrs={'class': 'drawer__nav-item'})[2:12]
    # womenSoup = soup.findAll('li', attrs={'class': 'drawer__nav-item'})[14:25]
    kidsSoupCount = soup.findAll('ul', attrs={'class': 'site-nav-dropdown'})
    print('kids soup count ', kidsSoupCount)
    kidsSoup1 = soup.findAll('ul', attrs={'class': 'site-nav-dropdown'})[13].findAll('li')
    kidsSoup2 = soup.findAll('ul', attrs={'class': 'site-nav-dropdown'})[14].findAll('li')
    kidsSoup3 = soup.findAll('ul', attrs={'class': 'site-nav-dropdown'})[15].findAll('li')
    kidsSoup = kidsSoup1 + kidsSoup2 + kidsSoup3
    # for brand in menSoup:
    #     # print("brand_", brand)
    #     if(brand.find('a') != -1):
    #         print(brand.find('a')['href'])
    #         print(brand.find('a').text.strip())
    #         menBrands.append(
    #                     {
    #                         'url': webUrl + brand.find('a')['href'],
    #                         'name': brand.find('a').text.strip()
    #                     })
    #     print('........................................................................')
    # for brand in womenSoup:
    #     # print("brand_", brand)
    #     if(brand.find('a') != -1):
    #         print(brand.find('a')['href'])
    #         print(brand.find('a').text.strip())
    #         womenBrands.append(
    #                     {
    #                         'url': webUrl + brand.find('a')['href'],
    #                         'name': brand.find('a').text.strip()
    #                     })
    #     print('........................................................................')
    print('kids soup ', kidsSoup)
    for brand in kidsSoup:
        # print("brand_", brand)
        if(brand.find('a') != -1):
            # print(brand.find('a')['href'])
            # print(brand.find('a').text.strip())
            kidsBrands.append(
                        {
                            'url': webUrl + brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
        print('........................................................................')
    driver.close()
    # print('menBrands ', menBrands)
    # print('womenBrands ', womenBrands)
    print('kidsBrands ', kidsBrands)

def startScrapping():
    # start point for scrapping all the data
    try:
        allBrands = [
                     {'blist': kidsBrands, 'name': 'kids'},
                     {'blist': womenBrands, 'name': 'women'},
                     {'blist': menBrands, 'name': 'men'}
        ]
        for brand in allBrands:
            openSitePage(brand['blist'], brand['name'])
    except Exception as el:
        print("Exception occured ", el)
        driver.close()

##start point for getting all the links for men,women,kids brands urls and brand names

try:

    # getAllLinks()
    startScrapping()
except Exception as el:
    print("Error opening site  ", el)
    driver.close()

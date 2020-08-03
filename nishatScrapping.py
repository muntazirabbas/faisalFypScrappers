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

womenBrands = [
    {'url': 'https://nishatlinen.com/pk/women/new-in.html', 'name': 'New In'},
    {'url': 'https://nishatlinen.com/pk/women/unstitched.html', 'name': 'Unstitched'} ,
    {'url': 'https://nishatlinen.com/pk/women/ftb.html', 'name': 'Freedom To Buy'},
    {'url': 'https://nishatlinen.com/pk/women/ready-to-wear.html', 'name': 'Ready To Wear'},
    {'url': 'https://nishatlinen.com/pk/women/fusion-tops.html', 'name': 'Fusion Tops'},
    {'url': 'https://nishatlinen.com/pk/women/lowers.html', 'name': 'Lowers'},
    {'url': 'https://nishatlinen.com/pk/women/lowers/trousers.html', 'name': 'Trousers'},
    {'url': 'https://nishatlinen.com/pk/women/lowers/shalwars.html', 'name': 'Shalwars'},
    {'url': 'https://nishatlinen.com/pk/women/lowers/pants.html', 'name': 'Pants'},
    {'url': 'https://nishatlinen.com/pk/luxury-pret/from-the-closet.html', 'name': 'From The Closet'},
    {'url': 'https://nishatlinen.com/pk/luxury-pret/fit-to-wear.html', 'name': 'Fit To Wear'},
    {'url': 'https://nishatlinen.com/pk/luxury-pret/ready-to-stitch.html', 'name': 'Ready To Stitch'},
    {'url': 'https://nishatlinen.com/pk/luxury-pret/pair-of-pants.html', 'name': 'Pair of Pants'},
    {'url': 'https://nishatlinen.com/pk/luxury-pret/to-wrap-up.html', 'name': 'To Wrap UP'}
]
menBrands =  [{'url': 'https://nishatlinen.com/pk/men/naqsh.html', 'name': 'Naqsh'}]
kidsBrands =  [{'url': 'https://nishatlinen.com/pk/kids/accessories.html', 'name': 'Accessories'},
               {'url': 'https://nishatlinen.com/pk/kids/bags.html', 'name': 'Bags'},
               {'url': 'https://nishatlinen.com/pk/kids/sunglasses.html', 'name': 'Sunglasses'},
               {'url': 'https://nishatlinen.com/pk/kids/footwear.html', 'name': 'Footwear'},
               {'url': 'https://nishatlinen.com/pk/kids/wraps.html', 'name': 'Wraps'},
               {'url': 'https://nishatlinen.com/pk/kids/kids-masks.html', 'name': 'Kids Masks'}]

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

def goToProductDetail(_productData,productUrl):
    print('product url ', productUrl)
    driver.get(productUrl)
    # time.sleep(7)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    descriptionDiv = soup.find("div", attrs={'class': 'product attribute overview'})
    color=''
    if (descriptionDiv):
        if(descriptionDiv.find('p')):
            colorP = descriptionDiv.findAll('p')
            for _para in colorP:
                # print('para ', _para)
                if('color:' in _para.text.strip().lower()):
                    color = _para.text.strip().lower().split('color:')[1].strip()
                    if("&\xa0") in color:
                        color = color.split("&\xa0")[0]
        if(descriptionDiv.find('span')):
            colorP = descriptionDiv.findAll('span')
            for _para in colorP:
                # print('span ', _para)
                if('color:' in _para.text.strip().lower()):
                    color = _para.text.strip().lower().split('color:')[1].strip()

    sizes = []
    if(soup.find('div', attrs={'class' : "swatch-attribute-options clearfix"})):
        sizeDiv = soup.find('div', attrs={'class': "swatch-attribute-options clearfix"})
        for size in sizeDiv:
            sizes.append(size.text.strip())
    _productData['size'] = sizes
    _productData['colors'] = [color]
    mydb.freshProducts.insert_one(_productData)
    print('product data ', _productData)
    print('................................................................................................')


def processBrands(brandArray,gender):
    for data in brandArray:
        print('site url ', data['url'])
        driver.get(data['url'])
        # time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        nishat = soup.findAll("li", {"class": "item product product-item"})
        for nish in nishat:
            if(len(nish.findAll('span', {'class': 'price'})) > 1):
                price = float(nish.findAll('span', {'class': 'price'})[1].text[4:].replace(',',''))
            else:
                price = float(nish.findAll('span', {'class': 'price'})[0].text[4:].replace(',',''))
            buy_url = nish.find('a')['href']
            title = nish.find('a', {'class': "product-item-link"}).text.strip()
            color = ''
            if (gender == 'kids'):
                color = colorAssignment(title.lower())
            imageUrl = nish.find('img')['src']
            brandName = data['name']
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
                'colors': [color],
                'size': [],
                'buyUrl': buy_url,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'nishat'
            }
            if (gender == 'kids'):
                mydb.freshProducts.insert_one(dataObject)
                print(dataObject)
            else:
                goToProductDetail(dataObject, buy_url)

def ScrapProducts():
    try:
        allBrands = [
            {'blist': womenBrands, 'name': 'women'},
            {'blist': menBrands, 'name': 'men'},
            {'blist': kidsBrands, 'name': 'kids'},
        ]
        for brand in allBrands:
            processBrands(brand['blist'], brand['name'])
    except Exception as el:
        print("Exception occured ", el)
        driver.close()

def getAllLinks():
    scrapeUrl = "https://nishatlinen.com/"
    mainUrl = "https://nishatlinen.com/"
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    womenSoup1 = soup.findAll('ul', attrs={'class': "level0 submenu"})[0].findAll('li')
    womenSoup2 = soup.findAll('ul', attrs={'class': "level0 submenu"})[1].findAll('li')
    womenSoup3 = soup.findAll('ul', attrs={'class': "level0 submenu"})[2].findAll('li')
    menSoup = soup.findAll('ul', attrs={'class': "level0 submenu"})[3].findAll('li')
    kidsSoup = soup.findAll('ul', attrs={'class': "level0 submenu"})[4].findAll('li')
    womenSoup = womenSoup1 + womenSoup2 + womenSoup3
    # print("womensoup ", womenSoup)
    # for brand in womenSoup:
    #     if (brand.find('a') != -1):
    #         # print(brand.find('a')['href'])
    #         # print(brand.find('a').text.strip())
    #         kidsBrands.append(
    #             {
    #                 'url':  brand.find('a')['href'],
    #                 'name': brand.find('a').text.strip()
    #             })
    for brand in kidsSoup:
        if (brand.find('a') != -1):
            # print(brand.find('a')['href'])
            # print(brand.find('a').text.strip())
            kidsBrands.append(
                {
                    'url':  brand.find('a')['href'],
                    'name': brand.find('a').text.strip()
                })
    for brand in menSoup:
        if (brand.find('a') != -1):
            # print(brand.find('a')['href'])
            # print(brand.find('a').text.strip())
            menBrands.append(
                {
                    'url':  brand.find('a')['href'],
                    'name': brand.find('a').text.strip()
                })
    # print('womenBrands = ', womenBrands)
    print('menBrands = ', menBrands)
    print('kidsBrands = ', kidsBrands)

    driver.close()

try:
    ScrapProducts()
    # getAllLinks()
except Exception as el:
    print("Exception occured ", el)
    driver.close()

import random
from datetime import date,datetime
from bs4 import BeautifulSoup
import pymongo
from selenium import webdriver
myclient       = pymongo.MongoClient("mongodb://localhost:27017/")
mydb           = myclient["fypDb"]
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
menBrands = [{'url': 'https://www.uniworthshop.com/shirts/plain-shirts', 'name': 'Plain Shirts'}, {'url': 'https://www.uniworthshop.com/shirts/plain-shirts/regular-fit-plain-shirts', 'name': 'Regular Fit'}, {'url': 'https://www.uniworthshop.com/shirts/plain-shirts/smart-fit-plain-shirts', 'name': 'Smart Fit'}, {'url': 'https://www.uniworthshop.com/shirts/plain-shirts/tuxedo-shirt', 'name': 'Tuxedo Shirt'}, {'url': 'https://www.uniworthshop.com/shirts/check-shirts', 'name': 'Check Shirts'}, {'url': 'https://www.uniworthshop.com/shirts/check-shirts/regular-fit-check-shirts', 'name': 'Regular Fit'}, {'url': 'https://www.uniworthshop.com/shirts/check-shirts/smart-fit-check-shirts', 'name': 'Smart Fit'}, {'url': 'https://www.uniworthshop.com/shirts/stripe-shirts', 'name': 'Stripe Shirts'}, {'url': 'https://www.uniworthshop.com/shirts/stripe-shirts/regular-fit-stripe-shirts', 'name': 'Regular Fit'}, {'url': 'https://www.uniworthshop.com/shirts/stripe-shirts/smart-fit-stripe-shirts', 'name': 'Smart Fit'}, {'url': 'https://www.uniworthshop.com/shirts/double-cuff-plain-shirts', 'name': 'Double Cuff'}, {'url': 'https://www.uniworthshop.com/summer-soul/t-shirts', 'name': 'T-Shirts'}, {'url': 'https://www.uniworthshop.com/summer-soul/t-shirts/polo-t-shirts', 'name': 'Polo T-Shirts'}, {'url': 'https://www.uniworthshop.com/summer-soul/t-shirts/crew-neck-t-shirts', 'name': 'Crew Neck T-Shirts'}, {'url': 'https://www.uniworthshop.com/summer-soul/casual-shirts', 'name': 'Casual Shirts'}, {'url': 'https://www.uniworthshop.com/summer-soul/casual-shirts/full-sleeves-casual-shirts', 'name': 'Full Sleeves'}, {'url': 'https://www.uniworthshop.com/summer-soul/casual-shirts/half-sleeves-casual-shirts', 'name': 'Half Sleeves'}, {'url': 'https://www.uniworthshop.com/summer-soul/basic-tees', 'name': 'Basic Tees'}, {'url': 'https://www.uniworthshop.com/summer-soul/basic-tees/full-sleeve-basic-tees', 'name': 'Full Sleeve Basic Tees'}, {'url': 'https://www.uniworthshop.com/summer-soul/basic-tees/basic-tees', 'name': 'Half Sleeve Basic Tees'}, {'url': 'https://www.uniworthshop.com/summer-soul/cotton-trousers', 'name': 'Cotton Trousers'}, {'url': 'https://www.uniworthshop.com/trousers/formal-trousers', 'name': 'Formal Trousers'}, {'url': 'https://www.uniworthshop.com/trousers/formal-trousers/classic-fit', 'name': 'Classic Fit'}, {'url': 'https://www.uniworthshop.com/trousers/formal-trousers/smart-fit', 'name': 'Smart Fit'}, {'url': 'https://www.uniworthshop.com/trousers/denim-jeans', 'name': 'Denim Jeans'}, {'url': 'https://www.uniworthshop.com/trousers/mens-chinos', 'name': 'Mens Chinos'}, {'url': 'https://www.uniworthshop.com/ethnic-wear/shalwar-suit', 'name': 'Shalwar Suit'}, {'url': 'https://www.uniworthshop.com/ethnic-wear/kurtas', 'name': 'Kurtas'}, {'url': 'https://www.uniworthshop.com/ethnic-wear/loose-fabric', 'name': 'Fabric'}, {'url': 'https://www.uniworthshop.com/ethnic-wear/peshawari-chappal', 'name': 'Peshawari Chappal'}, {'url': 'https://www.uniworthshop.com/suiting/men-s-suiting', 'name': 'Suiting'}, {'url': 'https://www.uniworthshop.com/suiting/gift-box', 'name': 'Gift Box'}, {'url': 'https://www.uniworthshop.com/suiting/pocket-square-1', 'name': 'Pocket Square'}, {'url': 'https://www.uniworthshop.com/suiting/tiepin', 'name': 'Tie Pin'}, {'url': 'https://www.uniworthshop.com/relaxing-wear/woven-pajamas', 'name': 'Pajamas'}, {'url': 'https://www.uniworthshop.com/relaxing-wear/tshirt-pajama', 'name': 'T-Shirt & Pajama Set'}, {'url': 'https://www.uniworthshop.com/relaxing-wear/track-suit', 'name': 'Track Suits'}, {'url': 'https://www.uniworthshop.com/relaxing-wear/mens-shorts', 'name': 'Mens Shorts'}, {'url': 'https://www.uniworthshop.com/accessories/mens-perfumes', 'name': 'Perfumes'}, {'url': 'https://www.uniworthshop.com/accessories/ties', 'name': 'Ties'}, {'url': 'https://www.uniworthshop.com/accessories/ties/regular-ties', 'name': 'Regular Ties'}, {'url': 'https://www.uniworthshop.com/accessories/ties/slim-ties', 'name': 'Slim ties'}, {'url': 'https://www.uniworthshop.com/accessories/ties/bow-tie', 'name': 'Bow Tie Set'}, {'url': 'https://www.uniworthshop.com/accessories/belts', 'name': 'Belts'}, {'url': 'https://www.uniworthshop.com/accessories/belts/pin-buckles', 'name': 'Pin Buckles'}, {'url': 'https://www.uniworthshop.com/accessories/belts/fancy-buckles', 'name': 'Fancy Buckles'}, {'url': 'https://www.uniworthshop.com/accessories/belts/casual-belt', 'name': 'Casual Belt'}, {'url': 'https://www.uniworthshop.com/accessories/socks', 'name': 'Socks'}]
#This site has only men's brands products

def goToProductDetail(_productData,productUrl):
    #get colors and size of product
    # print('product url ', productUrl)
    driver.get(productUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # print("detail soup ",soup)
    sizeDiv = soup.findAll('select', attrs={'class' : 'required-entry super-attribute-select'})[0].findAll('option')[1:]
    colorRows = soup.find('div', attrs={'class' : 'ui-tabs-panel ui-widget-content ui-corner-bottom'}).findAll('tr')
    price = soup.find('span', attrs={'class': 'price'}).text.strip()[4:]
    # print('price__',price)
    pictures = []
    colors = []
    size = []

    for _size in sizeDiv:
        if(_size):
            # print('size => ',_size)
            size.append(_size.text)
    for colorRow in colorRows:
        # print('colorRow ', colorRow)
        if(colorRow.find('td').text.strip().lower() == 'colour'):
            # print('color => ',colorRow.findAll('td')[1].text.strip().lower())
            colors.append(colorRow.findAll('td')[1].text.strip().lower())
    _productData['colors'] = colors
    _productData['size'] = size
    # _productData['pictures'] = pictures
    _productData['price'] = price
    print('product data ', _productData)
    # mydb.products.insert_one(_productData)

def openSitePage(brandData, type):
    for sitePage in brandData:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],type)

jsonData = []
def processSitePageSoup(soup, brandName,gender):
    webUrl = "https://www.uniworthshop.com"
    products = soup.findAll('div', attrs={'class': 'product-box'})
    # print('products ', products)
    for product in products:
        if(product):
            # print("product======>>>>",product)
            title = product.find('a')['title'].strip()
            buyUrl = product.find('a')['href'].strip()
            _image = product.find('img')['data-src'].strip()
            pictures = [_image]

            dataObject = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                'name': title,
                'price': 0,
                'pictures': pictures,
                'stock': 'N/A',
                'discount': 0,
                'salePrice': 0,
                'description': '',
                'tags': [gender, brandName],
                'rating': 'N/A',
                'category': gender,
                'colors': [],
                'size': [],
                'buyUrl': buyUrl,
                'gender': gender,
                'brand': brandName,
                'date': datetime.today(),
                'mainBrand': 'uniworthshop'
            }
            # print('data_____',dataObject)
            goToProductDetail(dataObject,buyUrl)
            # print('...........................................................................................')

print('starting scrapping')

def getAllLinks(scrapeUrl):
    domainName = "https://www.uniworthshop.com"
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source,'lxml')
    for ultag in soup.find_all('ul', {'class': 'level1 num0'}):
        for brand in ultag.find_all('li'):
            print("brand_", brand)
            if(brand.find('a') != -1):
                print(brand.find('a')['href'])
                print(brand.find('a').text.strip())
                menBrands.append(
                        {
                            'url': brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
        print('........................................................................')

    driver.close()
    print('menBrands = ', menBrands)

##start point for getting all the links for men,women,kids brands urls and brand names
#try:
#     scrapeUrl = "https://www.uniworthshop.com"
#     getAllLinks(scrapeUrl)
# except Exception as el:
#     print("Error opening site  ", el)
#     driver.close()

#start point for scrapping all the data
try:
    openSitePage(menBrands, 'men')
except Exception as el:
    print("Exception occured ", el)
    driver.close()
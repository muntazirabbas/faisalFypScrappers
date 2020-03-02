from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
from datetime import date
menBrands = [{'url': 'https://www.engine.com.pk/collections/men-casual-shirts', 'name': 'Shirts'}, {'url': 'https://www.engine.com.pk/collections/men-t-shirts', 'name': 'T-Shirts'}, {'url': 'https://www.engine.com.pk/collections/men-jeans', 'name': 'Jeans'}, {'url': 'https://www.engine.com.pk/collections/men-pants', 'name': 'Pants'}, {'url': 'https://www.engine.com.pk/collections/men-trousers', 'name': 'Trousers'}, {'url': 'https://www.engine.com.pk/collections/men-hoodies-sweatshirts', 'name': 'Hoodies & Sweatshirts'}, {'url': 'https://www.engine.com.pk/collections/men-sweaters', 'name': 'Sweaters'}, {'url': 'https://www.engine.com.pk/collections/men-jackets', 'name': 'Jackets'}, {'url': 'https://www.engine.com.pk/collections/men-glasses', 'name': 'Glasses'}, {'url': 'https://www.engine.com.pk/collections/men-footwear', 'name': 'Footwear'}]
womenBrands = [{'url': 'https://www.engine.com.pk/collections/woven-top', 'name': 'Woven Tops'}, {'url': 'https://www.engine.com.pk/collections/women-kurties', 'name': 'Kurties'}, {'url': 'https://www.engine.com.pk/collections/women-bottoms', 'name': 'Jeans'}, {'url': 'https://www.engine.com.pk/collections/women-pants', 'name': 'Pants'}, {'url': 'https://www.engine.com.pk/collections/women-trousers', 'name': 'Trousers'}, {'url': 'https://www.engine.com.pk/collections/women-tights', 'name': 'Tights'}, {'url': 'https://www.engine.com.pk/collections/women-hoodies-sweatshirts', 'name': 'Hoodies & Sweatshirts'}, {'url': 'https://www.engine.com.pk/collections/women-sweaters', 'name': 'Sweaters'}, {'url': 'https://www.engine.com.pk/collections/ladies-jacket', 'name': 'Jackets'}, {'url': 'https://www.engine.com.pk/collections/women-sleepwear', 'name': 'Sleepwear'}, {'url': 'https://www.engine.com.pk/collections/women-footwear', 'name': 'Footwear'}]
kidsBrands =[{'url': 'https://www.engine.com.pk/collections/t-shirt', 'name': 'T-Shirts'}, {'url': 'https://www.engine.com.pk/collections/boys-bottom', 'name': 'Jeans'}, {'url': 'https://www.engine.com.pk/collections/boys-pants', 'name': 'Pants'}, {'url': 'https://www.engine.com.pk/collections/boys-trousers', 'name': 'Trousers'}, {'url': 'https://www.engine.com.pk/collections/boys-shorts', 'name': 'Shorts'}, {'url': 'https://www.engine.com.pk/collections/boys-hoodies-sweatshirts', 'name': 'Hoodies & Sweatshirts'}]

scrapeUrl = ""

def openSitePage(brandData, type):
    for sitePage in brandData:
        print('sitePage ', sitePage)
        driver.get(sitePage['url'])
        soup = BeautifulSoup(driver.page_source, 'lxml')
        processSitePageSoup(soup, sitePage['name'],type)

jsonData = []
def processSitePageSoup(soup, brandName,type):
    webUrl = "https://www.engine.com.pk"
    products = soup.findAll('div', attrs={'class': 'grid__item small--one-half medium-up--one-fifth'})
    # print('products ', products)
    for product in products:
        if(product):
            # print("product======>>>>",product.find('div',{'class':'details'}))
            title = product.find('div',{'class':'product-card__name'}).text.strip()
            buyUrl = webUrl + product.findAll('a')[0]['href']
            price = 0
            if (product.find('div',{'class':'product-card__price'})):
                price = product.find('div', attrs={'class': 'product-card__price'}).find(text=True, recursive=False)
                #>>> soup.div.find(text=True, recursive=False)

            else:
                price = "no price"
                # print("price tag ", price)
                # priceTag = product.find('div',{'class':'product-card__price'}).findAll('span')[1]) //.text.strip()
            # image = product.find('img')['src']
            print("Type = ", type)
            print("Brand = ", brandName)
            print("Title = ", title)
            print("Buy URL = ", buyUrl)
            print("Price = ", price)
            print("Date = ", date.today())
            # print('img = ', image)
            # jsonData.append({
            #     'name': title,
            #     'buyUrl': buyUrl,
            #     'price': price,
            #     'Type': type,
            #     'subType': brandName,
            #     'date': date.today(),
            #     'image': image
            # })
            print('jsonData ', jsonData)
            print('...........................................................................................')

print('starting scrapping')

def getAllLinks(scrapeUrl):
    webUrl = "https://www.engine.com.pk"
    driver.get(scrapeUrl)
    soup = BeautifulSoup(driver.page_source,'lxml')
    menSoup = soup.findAll('li', attrs={'class': 'drawer__nav-item'})[2:12]
    womenSoup = soup.findAll('li', attrs={'class': 'drawer__nav-item'})[14:25]
    kidsSoup = soup.findAll('li', attrs={'class': 'drawer__nav-item'})[27:33]

    for brand in menSoup:
        # print("brand_", brand)
        if(brand.find('a') != -1):
            print(brand.find('a')['href'])
            print(brand.find('a').text.strip())
            menBrands.append(
                        {
                            'url': webUrl + brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
        print('........................................................................')
    for brand in womenSoup:
        # print("brand_", brand)
        if(brand.find('a') != -1):
            print(brand.find('a')['href'])
            print(brand.find('a').text.strip())
            womenBrands.append(
                        {
                            'url': webUrl + brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
        print('........................................................................')
    for brand in kidsSoup:
        # print("brand_", brand)
        if(brand.find('a') != -1):
            print(brand.find('a')['href'])
            print(brand.find('a').text.strip())
            kidsBrands.append(
                        {
                            'url': webUrl + brand.find('a')['href'],
                            'name': brand.find('a').text.strip()
                        })
        print('........................................................................')
    driver.close()
    print('menBrands ', menBrands)
    print('womenBrands ', womenBrands)
    print('kidsBrands ', kidsBrands)


##start point for getting all the links for men,women,kids brands urls and brand names

# try:
#     scrapeUrl = "https://www.engine.com.pk/collections/men"
#     getAllLinks(scrapeUrl)
# except Exception as el:
#     print("Error opening site  ", el)
#     driver.close()


#start point for scrapping all the data
try:
    openSitePage(menBrands, 'kids')
except Exception as el:
    print("Exception occured ", el)
    driver.close()

driver.close()
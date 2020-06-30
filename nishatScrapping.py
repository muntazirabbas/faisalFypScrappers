import requests
import random
from datetime import datetime
import requests
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
from bs4 import BeautifulSoup
from fake_useragent import  UserAgent
ua          = UserAgent()
header      = {'user-agent':ua.chrome}
import time
from selenium import webdriver
driver  = webdriver.Chrome('C:/Users/MUNTAZIR/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
type_array = ['women','men','kids','accessories']

type_temp =0

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
    if(descriptionDiv.find('p')):
        colorP = descriptionDiv.findAll('p')
        for _para in colorP:
            # print('para ', _para)
            if('color:' in _para.text.strip().lower()):
                color = _para.text.strip().lower().split('color:')[1].strip()
    if(descriptionDiv.find('span')):
        colorP = descriptionDiv.findAll('span')
        for _para in colorP:
            # print('span ', _para)
            if('color:' in _para.text.strip().lower()):
                color = _para.text.strip().lower().split('color:')[1].strip()


    _productData['colors'] = [color]
    mydb.freshProducts.insert_one(_productData)
    print('product data ', _productData)
    print('................................................................................................')


while(type_temp < len(type_array)):
    if(type_array[type_temp] == "men"):
     pagecount=2
    else:
     pagecount=5
    while (pagecount > 0):

        print("pagecount = ", pagecount)
        url = "https://nishatlinen.com/pk/" + type_array[type_temp] + ".html?p="+str(pagecount)
        response = requests.get(url,headers=header)
        print(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        nishat = soup.findAll("li", {"class": "item product product-item"})
        for nish in nishat:
            price = nish.find('span', {'class': 'price'}).text[4:]
            buy_url = nish.find('a')['href']
            title = nish.find('a', {'class': "product-item-link"}).text.strip()
            color = ''
            if(type_array[type_temp] == 'kids'):
                color = colorAssignment(title.lower())
            imageUrl = nish.find('img')['src']

            dataObject = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(
                    list(range(55, 5000))),
                'name': title,
                'pictures': [imageUrl],
                'stock': 'N/A',
                'price': price,
                'discount': 0,
                'salePrice': 0,
                'description': '',
                'tags': [type_array[type_temp], title],
                'rating': random.choice(list(range(3, 5))),
                'category': type_array[type_temp],
                'colors': [color],
                'size': [],
                'buyUrl': buy_url,
                'gender': type_array[type_temp],
                'brand': title,
                'date': datetime.today(),
                'mainBrand': 'nishat'
            }
            if(type_array[type_temp] == 'kids'):
                mydb.freshProducts.insert_one(dataObject)
                print(dataObject)
            else:
                goToProductDetail(dataObject,buy_url)

        pagecount -=1

    type_temp += 1
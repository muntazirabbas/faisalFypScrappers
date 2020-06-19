import requests
from bs4 import BeautifulSoup
import requests
import random
from datetime import datetime
import requests
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
from fake_useragent import  UserAgent
ua          = UserAgent()
header      = {'user-agent':ua.chrome}
type_array = ['handbags','dupattas','necklaces','suits']
type_temp =0
counter=0
while(type_temp < len(type_array)):
    url = "https://www.limelight.pk/collections/" + type_array[type_temp]
    response = requests.get(url,headers=header)
    print(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for limeLight in soup.select('div[class*="product desktop-3"]'):
       Type = type_array[type_temp]
       buy_url = "https://www.limelight.pk"+limeLight.find('a')['href']
       title = limeLight.find('a')['title'].strip()
       price = limeLight.find('span', {'class': 'money'}).text.strip()[3:]
       imageUrl = "https:"+limeLight.find('img')['data-src']
       # print("Image URL", imageUrl)
       # print("Type = ",Type)
       # print("Title = ",title)
       # print("Buy URL = ", buy_url)
       # print("Price = ",price)
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
           'colors': [],
           'size': [],
           'buyUrl': buy_url,
           'gender': type_array[type_temp],
           'brand': title,
           'date': datetime.today(),
           'mainBrand': 'limelight'
       }
       print(dataObject)
       mydb.freshProducts.insert_one(dataObject)
       counter +=1
       print('...........................................\n')

    type_temp += 1
from bs4 import BeautifulSoup
import random
from datetime import datetime
import requests
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
from fake_useragent import  UserAgent
ua          = UserAgent()
header      = {'user-agent':ua.chrome}
type_array = ['girls','boys','accessories','infants']
type_temp =0
while(type_temp < len(type_array)):
    url = "https://minnieminors.com/pk/" + type_array[type_temp]
    response = requests.get(url,headers=header)
    print(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for minnieMinors in soup.select('ul[class*="products-grid my-list"]'):
       for nestedMini in minnieMinors.select('li[class*="item"]'):
           price =     nestedMini.find('span', {'class': 'price'}).text.strip()[4:-3]
           Type =      type_array[type_temp]
           title =     nestedMini.a['title'].strip()
           buy_url =   nestedMini.a['href']
           imageUrl = nestedMini.a.img['src']
           dataObject = {
               "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
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
               'mainBrand': 'minnieminors'
           }
           print(dataObject)
           # mydb.products.insert_one(dataObject)
           print('...........................................\n')

    type_temp += 1
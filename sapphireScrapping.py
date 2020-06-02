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
type_array = [
              {'url' : 'https://pk.sapphireonline.pk/collections/ready-to-wear', 'name': 'women'},
              {'url' : 'https://pk.sapphireonline.pk/collections/menswear' , 'name': 'men'},
              {'url' : 'https://pk.sapphireonline.pk/collections/kids', 'name': 'kids'}
              ]
type_temp =0
counter=0
while(type_temp < len(type_array)):
    response = requests.get(type_array[type_temp]['url'],headers=header)
    soup = BeautifulSoup(response.content, 'html.parser')
    print('page url ', type_array[type_temp]['url'] )
    for sapphire in soup.select('div[class*="grid-item col-6 col-md-4 col-xl-3 four-columns"]'):
       gender = type_array[type_temp]['name']
       buy_url = "https://pk.sapphireonline.pk"+sapphire.find('a')['href']
       title = sapphire.find('img')['alt'].strip()
       price = sapphire.find('span', {'class': 'money'}).text.strip()[3:-3]
       imageUrl = sapphire.find('div', attrs={'class' : 'product-top'}).find('img')['data-src']
       counter +=1
       dataObject = {
           "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
           'name': title,
           'pictures': [imageUrl],
           'stock': 'N/A',
           'price': price,
           'discount': 0,
           'salePrice': 0,
           'description': '',
           'tags': [title, gender],
           'rating': random.choice(list(range(3, 5))),
           'category': title,
           'colors': [],
           'size': [],
           'buyUrl': buy_url,
           'gender': gender,
           'brand': title,
           'date': datetime.today(),
           'mainBrand': 'sapphire'
       }
       print(dataObject)
       # mydb.products.insert_one(dataObject)
       print(".................................................................................................\n")

    type_temp += 1
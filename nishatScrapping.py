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
type_array = ['women','men','kids','accessories']
type_temp =0
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

            # print("Type = ", type_array[type_temp])
            # print("Title = ", title)
            # print("Price = ", price)
            # print("Buy URL = ", buy_url)
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
                'colors': [],
                'size': [],
                'buyUrl': buy_url,
                'gender': type_array[type_temp],
                'brand': title,
                'date': datetime.today(),
                'mainBrand': 'nishat'
            }
            print(dataObject)
            mydb.freshProducts.insert_one(dataObject)
        pagecount -=1

    type_temp += 1
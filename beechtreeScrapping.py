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
brand_array = ['pret','luxpret-festive-edition','unstitched','absolute','accessories/bags','accessories/shoes','accessories/stationery']
brand_count=0

while(brand_count < len(brand_array)):
    url = "https://www.beechtree.pk/pk/"+brand_array[brand_count]+".html"
    response = requests.get(url, headers=header)
    print("Site URL = ", url, "\n")
    soup = BeautifulSoup(response.content, 'html.parser')
    counter=0
    for rowdata in soup.findAll("li", {"class": "item"}):
        if (rowdata != None):
            buy_url = rowdata.find('a')['href']
            title = rowdata.find('a')['title']
            price = rowdata.find('span', {'class': 'price'}).text.strip()[4:]
            _gender=""
            brand_value=""
            if(brand_array[brand_count]==brand_array[0] or brand_array[brand_count]==brand_array[1] or brand_array[brand_count]==brand_array[2] or brand_array[brand_count]==brand_array[3]):
                _gender="women"
                brand_value = brand_array[brand_count]
            elif(brand_array[brand_count]==brand_array[4] or brand_array[brand_count]==brand_array[5] or brand_array[brand_count]==brand_array[6]  ):
                _gender = "women"
                brand_value = brand_array[brand_count].rsplit('/', 1)[-1]
            else:
                _gender = "women"

            # print("Type = ", Type)
            # print("Brand = ",brand_value)
            # print("price = ", price)
            # print("Buy URL = ", buy_url)
            # print("Title = ", title)
            seeImg = rowdata.findAll("img")
            ImageURL = ""
            for sImg in seeImg:
                if (sImg['src'] != "/pagespeed_static/1.JiBnMqyl6S.gif"):
                    ImageURL = sImg['src']
                else:
                    ImageURL = sImg['pagespeed_lazy_src']
                # print("ImageURL = ",ImageURL)
            dataObject = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                'name': title,
                'pictures': [ImageURL],
                'stock': 'N/A',
                'price': price,
                'discount': 0,
                'salePrice': 0,
                'description': '',
                'tags': [brand_value, _gender],
                'rating': random.choice(list(range(3, 5))),
                'category': brand_value,
                'colors': [],
                'size': [],
                'buyUrl': buy_url,
                'gender': _gender,
                'brand': title,
                'date': datetime.today(),
                'mainBrand': 'beechtree'
            }
            print(dataObject)
            # mydb.products.insert_one(dataObject)
            print(".................................................................................................")

            counter+=1
    brand_count += 1

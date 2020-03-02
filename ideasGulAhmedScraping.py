import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
from fake_useragent import  UserAgent
ua          = UserAgent()
header      = {'user-agent':ua.chrome}
type_array = ['women','mens-clothes']
type_temp =0
while(type_temp < len(type_array)):
    if(type_array[type_temp] == "accessories"):
     pagecount=2
    else:
     pagecount=5
    if(type_array[type_temp]=="mens-clothes"):
         type_array[type_temp]="men"
    while (pagecount > 0):
        print("pagecount = \n\n", pagecount)
        url = "https://www.gulahmedshop.com/" + type_array[type_temp] + "?p="+str(pagecount)
        response = requests.get(url,headers=header)
        print(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        khaadi = soup.findAll("li", {"class": "item product product-item"})
        for khad in khaadi:
            price = khad.find('span', {'class': 'price'}).text.strip()[4:]
            buy_url = khad.find('a')['href']
            title = khad.find('a', {'class': "product-item-link"}).text.strip()
            imageURL = khad.findAll('img')[0]['src']
            # print("Type = ", type_array[type_temp])
            # print("Title = ", title)
            # print("Price = ", price)
            # print("Buy URL = ", buy_url)
            # print("Image", imageURL)
            colors = ["black", "gray", "red", "pink", "white", "green", "blue"]
            size = random.choice(
                [
                    ['100 CM', '90 CM', '95 CM'],
                    ['M', 'L', 'XL'],
                    ['XS', 'S', '2T'],
                    ['3T', '4T', '7'],
                    ['8', '9']
                ])
            # mainBrands = ['bonanza', 'outfitters', 'breakout', 'khaadi', 'engine', 'gulahmed', 'junaidjamshed', 'levi']
            dataObject = {
                "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(list(range(55, 5000))),
                'name': title,
                'pictures': [imageURL],
                'stock': random.choice(list(range(10, 400))),
                # 'price': int(price.strip().replace(',', '')),
                'discount': random.choice(list(range(0, 100))),
                # 'salePrice': int(price.strip().replace(',', '')) + random.choice([0, 300]),
                'description': '',
                'tags': [type_array[type_temp]],
                'rating': random.choice(list(range(0, 5))),
                'category': type_array[type_temp],
                'colors': [random.choice(colors), random.choice(colors), random.choice(colors)],
                'size': size,
                'buyUrl': buy_url,
                'gender': type_array[type_temp],
                'brand': '',
                'date': datetime.today(),
                'mainBrand': 'gulahmed'
            }
            print('data__',dataObject)
            mydb.products.insert_one(dataObject)

        pagecount -=1

    type_temp += 1
import random
from datetime import date,datetime
import requests
from bs4 import BeautifulSoup
from datetime import date
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fypDb"]
from fake_useragent import  UserAgent
# ua = UserAgent()
# header = {'user-agent':ua.chrome}
brand_array=["men-shirts",'shirts','men-footwear','men-shorts','men-trousers','women-shirts','women-trouser',
             'women-footwear','boys-shirts','boys-shorts','boys-footwear','girls-shirts','girls-shorts','girls-footwear']
brand_count=0

print('starting Scrapping:')
jsonData = []
_date = date.today()
while(brand_count < len(brand_array)):
    url = "https://outfitters.com.pk/collections/"+brand_array[brand_count]
    response = requests.get(url)
    print("Site URL = ", url, "\n")
    soup = BeautifulSoup(response.content, 'html.parser')
    counter=0
    for outFitters in soup.select('div[class*="no_crop_image"]'):
           buy_url = "https://outfitters.com.pk"+outFitters.find('a')['href'].strip()
           title = outFitters.find('img')['alt'].strip()
           price = outFitters.find('span', {'class': 'money'}).text.strip()
           gender = brand_array[brand_count].split('-')[0]
           brand_value = brand_array[brand_count].split('-')[1]
           if(gender == "boys" or gender == "girls"):
               gender="kids"
           # print("Type = ",gender)
           # print("Brand = ", brand_value)
           # print("Title = ",title)
           # print("Buy URL = ", buy_url)
           # print("Price = ",price)
           # print("Date = ", _date)
           imageURL = ""
           for image in outFitters.findAll('img'):
               imageURL = "https:"+image['src']
               # print("Image URL",imageURL)
           counter +=1
           jsonData.append({
               'name':title,
               'buyUrl': buy_url,
               'price': price[3:0],
               'Type': gender,
               'subType': brand_value,
               'date': _date,
               'image': imageURL
           })
           colors = ["black", "gray", "red", "pink", "white", "green", "blue"]
           size = random.choice(
               [
                   ['100 CM', '90 CM', '95 CM'],
                   ['M', 'L', 'XL'],
                   ['XS', 'S', '2T'],
                   ['3T', '4T', '7'],
                   ['8', '9']
               ])
           mainBrands = ['bonanza', 'outfitters', 'breakout', 'khaadi', 'engine', 'gulahmed', 'junaidjamshed', 'levi']
           dataObject = {
               "id": random.choice(list(range(0, 100000))) + random.choice(list(range(77, 15400))) + random.choice(
                   list(range(55, 5000))),
               'name': title,
               'pictures': [imageURL],
               'stock': random.choice(list(range(10, 400))),
               'price': int(price[3:].strip().replace(',', '')),
               'discount': random.choice(list(range(0, 100))),
               'salePrice': int(price[3:].strip().replace(',', '')) + random.choice([0, 300]),
               'description': '',
               'tags': [gender, brand_value],
               'rating': random.choice(list(range(0, 5))),
               'category': gender,
               'colors': [random.choice(colors), random.choice(colors), random.choice(colors)],
               'size': size,
               'buyUrl': buy_url,
               'gender': gender,
               'brand': brand_value,
               'date': datetime.today(),
               'mainBrand': 'outfitters'
               # 'mainBrand': random.choice(mainBrands)
           }
           # jsonData.append(dataObject)
           print("data________", dataObject)
           # mydb.productslist.insert_one(dataObject)
           print("counter ",counter)
           print('...........................................................................................................\n')

    brand_count += 1

print("\n This is Outfitters Site Scrapping.......")
print('jsonData: => ', jsonData)

import requests
from bs4 import BeautifulSoup
from datetime import date
from fake_useragent import  UserAgent
# ua = UserAgent()
# header = {'user-agent':ua.chrome}
brand_array=["men-shirts",'men-footwear','men-shorts','men-trousers','women-shirts','women-trouser','women-footwear','boys-shirts','boys-shorts','boys-footwear','girls-shirts','girls-shorts','girls-footwear']
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
           Type = brand_array[brand_count].split('-')[0]
           brand_value = brand_array[brand_count].split('-')[1]
           if(Type == "boys" or Type == "girls"):
               Type="Kids"
           print("Type = ",Type)
           print("Brand = ", brand_value)
           print("Title = ",title)
           print("Buy URL = ", buy_url)
           print("Price = ",price)
           print("Date = ", _date)

           for image in outFitters.findAll('img'):
               image_url = "https:"+image['src']
               print("Image URL",image_url)
           counter +=1
           jsonData.append({
               'name':title,
               'buyUrl': buy_url,
               'price': price,
               'Type': Type,
               'subType': brand_value,
               'date': _date,
               'image': image_url
           })
           print("counter ",counter)
           print('...........................................................................................................\n')

    brand_count += 1

print("\n This is Outfitters Site Scrapping.......")
print('jsonData: => ', jsonData)
import requests
from bs4 import BeautifulSoup
from fake_useragent import  UserAgent
ua          = UserAgent()
header      = {'user-agent':ua.chrome}
type_array = ['women','mens-clothes','accessories']
type_temp =0
while(type_temp < len(type_array)):
    if(type_array[type_temp] == "accessories"):
     pagecount=2
    else:
     pagecount=5
    if(type_array[type_temp]=="mens-clothes"):
         type_array[type_temp]="Men"
    while (pagecount > 0):
        print("pagecount = \n\n", pagecount)
        url = "https://www.gulahmedshop.com/" + type_array[type_temp] + "?p="+str(pagecount)
        response = requests.get(url,headers=header)
        print(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        khaadi = soup.findAll("li", {"class": "item product product-item"})
        for khad in khaadi:
            price = khad.find('span', {'class': 'price'}).text
            buy_url = khad.find('a')['href']
            title = khad.find('a', {'class': "product-item-link"}).text.strip()

            print("Type = ", type_array[type_temp])
            print("Title = ", title)
            print("Price = ", price)
            print("Buy URL = ", buy_url)
            for i in khad.findAll('img'):
               print("Image", i['src'])
        pagecount -=1

    type_temp += 1
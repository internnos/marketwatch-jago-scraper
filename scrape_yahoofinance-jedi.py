import requests
from bs4 import BeautifulSoup

url = "https://www.marketwatch.com/investing/stock/arto?countrycode=id"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

key_data = soup.find('ul', class_="list list--kv list--col50")

with open('marketwatch/jago.txt', 'w') as writer:
    for info in key_data.find_all('li', class_='kv__item'):
        parameter_name = info.find('small', class_='label').text
        parameter_value = info.find('span', class_='primary').text
        # writer.write(f'{parameter_name}: {parameter_value} \n')
        writer.write(f'{parameter_name} {parameter_value} \n')


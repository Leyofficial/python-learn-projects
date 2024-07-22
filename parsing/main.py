import requests
import re
from bs4 import BeautifulSoup
URL = 'https://www.olx.ua/uk/transport/legkovye-avtomobili/q-bmw/?currency=UAH&search%5Border%5D=filter_float_price:asc&search%5Bfilter_float_price:from%5D=100000&search%5Bfilter_float_price:to%5D=150000'

req = requests.get(URL)
res = req.text

soap = BeautifulSoup(res, 'html.parser')

# BMW cars within budged 100.000 - 150.000 uan. Using OLX.UA website
all_products = soap.find_all('div', 'css-1sw7q4x')

bmw_cars = []

for card in all_products:
        name = card.find('h6', 'css-1wxaaza')
        price = card.find('p', 'css-13afqrm')
        date_place = card.find('p', 'css-1mwdrlh')
        in_top = card.find('div', 'css-1dyfc0k')
        link = card.find('a', href=True)
        if price:
            price_text = price.text
            price_match = re.search(r'\d[\d\s]*', price_text)
            price = price_match.group().replace(' ', '') if price_match else ''
        else:
            price = 0

        bmw_cars.append({
            'name': name.text if name else None,
            'price': price,
            'date_place': date_place.text if date_place else None,
            'in_top': True if in_top else False,
            'link': 'https://www.olx.ua/' + link['href'] if link else None
        })

bmw_cars.sort(key=lambda x: int(x['price']))

with open('results.txt', 'w', encoding='utf-8') as file:
    for item in bmw_cars:
        file.write(f"""
         Название: {item['name']} 
         Цена: {item['price']} 
         Дата публикации и место: {item['date_place']} 
         В топе: {"Да" if item['in_top'] else 'Нет'}
         Ссылка: {item['link']} 
          \n""")


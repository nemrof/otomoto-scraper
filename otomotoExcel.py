<<<<<<< HEAD
from bs4 import BeautifulSoup
from openpyxl import Workbook
import requests, datetime

# Time for name of the output file
now = datetime.datetime.now()
nowText = str(now.date())

workbook = Workbook()
sheet = workbook.active
sheet["A1"] = 'Auto'
sheet['B1'] = 'Cena'
sheet['C1'] = 'Rocznik'
sheet['D1'] = 'Przejechane'
sheet['E1'] = 'Pojemność'
sheet['F1'] = 'Silnik'
sheet['G1'] = 'Gdzie?'
sheet['H1'] = 'URL'
workbook.save(filename=f'./output/otomoto{nowText}.xlsx')

print('Wybierz czy chcesz szukać z własnymi filtrami, czy po marce?')
choice = int(input('Własne filtry - wpisz 1, marka - wpisz 2:  '))
if choice == 1:
    path = str(input('Wklej link:  '))
elif choice == 2:
    path = 'https://www.otomoto.pl/osobowe/'
    maker = str(input('Wybierz markę np. Audi, BMW '))
    loc = str(input('Jaka miejscowosc? '))
    priceLow = str(input('Podaj dolny limit cenowy '))
    priceHigh = str(input('Podaj górny limit cenowy '))
    path = (
        f'{path}{maker}/{loc}/?search%5Bfilter_float_price%3Afrom%5D={priceLow}&search%5Bfilter_float_price%3Ato%5D={priceHigh}&search%5Border%5D=filter_float_engine_power%3Adesc')
else:
    print('Wybierz cyfrę 1, lub 2!')
# get to the site

res = requests.get(path)
soup = BeautifulSoup(res.text, features='lxml')
try:
    numberPage = soup.select('.page')
    lastPage = int(numberPage[-1].getText())
except IndexError:
    lastPage = 2
run_time = datetime.datetime.now()

# Go through every page
for i in range(1, lastPage):
    # %3Fpage%3D3
    res = requests.get(path + '&page=' + str(i))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, features='lxml')
    titles = soup.select('.offer-title__link')
    prices = soup.select('.offer-price__number.ds-price-number')
    specs = soup.select('.ds-params-block')
    carLinks = soup.select('.offer-title__link', href=True)
    locations = soup.select('.ds-location-city')
    print(f'Właśnie patrzę na stronę numer: {i}.....')
    begin_time = datetime.datetime.now()
    for idx, item in enumerate(titles):
        j = len(sheet["A"]) + 1
        title = titles[idx].getText().strip().replace("  ", " ")
        price = prices[idx].getText().strip().replace("\n", " ")
        spec = specs[idx].getText().strip().replace("\n", " ")
        link = carLinks[idx].get('href').strip().replace(" ", "")
        try:
            year = specs[idx].find('li', {"data-code": 'year'}).getText().strip()
        except AttributeError:
            year = 'brak danych'
        try:
            mileage = specs[idx].find('li', {"data-code": 'mileage'}).getText().strip()
        except AttributeError:
            mileage = 'brak danych'
        try:
            engine_capacity = specs[idx].find('li', {"data-code": 'engine_capacity'}).getText().strip()
        except AttributeError:
            engine_capacity = 'brak danych'
        try:
            fuel_type = specs[idx].find('li', {"data-code": 'fuel_type'}).getText().strip()
        except AttributeError:
            fuel_type = 'brak danych'
        location = locations[idx].getText()
        sheet[f"A{j}"] = title
        sheet[f"B{j}"] = price
        sheet[f"C{j}"] = year
        sheet[f"D{j}"] = mileage
        sheet[f"E{j}"] = engine_capacity
        sheet[f"F{j}"] = fuel_type
        sheet[f"G{j}"] = location
        sheet[f"H{j}"] = link
    print('Gotowe!')
    workbook.save(filename=f'./output/otomoto{nowText}.xlsx')
    print(datetime.datetime.now() - begin_time)

endTime = datetime.datetime.now() - run_time
=======
from bs4 import BeautifulSoup
from openpyxl import Workbook
import requests, datetime

# Time for name of the output file
now = datetime.datetime.now()
nowText = str(now.date())

workbook = Workbook()
sheet = workbook.active
sheet["A1"] = 'Auto'
sheet['B1'] = 'Cena'
sheet['C1'] = 'Rocznik'
sheet['D1'] = 'Przejechane'
sheet['E1'] = 'Pojemność'
sheet['F1'] = 'Silnik'
sheet['G1'] = 'Gdzie?'
sheet['H1'] = 'URL'
workbook.save(filename=f'otomoto{nowText}.xlsx')

print('Wybierz czy chcesz szukać z własnymi filtrami, czy po marce?')
choice = int(input('Własne filtry - wpisz 1, marka - wpisz 2:  '))
if choice == 1:
    path = str(input('Wklej link'))
elif choice == 2:
    path = 'https://www.otomoto.pl/osobowe/'
    maker = str(input('Wybierz markę np. Audi, BMW '))
    loc = str(input('Jaka miejscowosc? '))
    priceLow = str(input('Podaj dolny limit cenowy '))
    priceHigh = str(input('Podaj górny limit cenowy '))
    path = (f'{path}{maker}/{loc}/?search%5Bfilter_float_price%3Afrom%5D={priceLow}&search%5Bfilter_float_price%3Ato%5D={priceHigh}&search%5Border%5D=filter_float_engine_power%3Adesc')
else:
    print('Wybierz cyfrę 1, lub 2!')
# get to the site

res = requests.get(path)
soup = BeautifulSoup(res.text, features='lxml')
try:
    numberPage = soup.select('.page')
    lastPage = int(numberPage[-1].getText())
except IndexError:
    lastPage = 2
run_time = datetime.datetime.now()

# Go through every page
for i in range(1, lastPage):
    res = requests.get(path + '%3Fpage%3D3&page=' + str(i))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, features='lxml')
    titles = soup.select('.offer-title__link')
    prices = soup.select('.offer-price__number.ds-price-number')
    specs = soup.select('.ds-params-block')
    carLinks = soup.select('.offer-title__link', href=True)
    locations = soup.select('.ds-location-city')
    print(f'Właśnie patrzę na stronę numer: {i}.....')
    begin_time = datetime.datetime.now()
    for idx, item in enumerate(titles):
        j = len(sheet["A"]) + 1
        title = titles[idx].getText().strip().replace("  ", " ")
        price = prices[idx].getText().strip().replace("\n", " ")
        spec = specs[idx].getText().strip().replace("\n", " ")
        link = carLinks[idx].get('href').strip().replace(" ", "")
        try:
            year = specs[idx].find('li', {"data-code": 'year'}).getText().strip()
        except AttributeError:
            year = 'brak danych'
        try:
            mileage = specs[idx].find('li', {"data-code": 'mileage'}).getText().strip()
        except AttributeError:
            mileage = 'brak danych'
        try:
            engine_capacity = specs[idx].find('li', {"data-code": 'engine_capacity'}).getText().strip()
        except AttributeError:
            engine_capacity = 'brak danych'
        try:
            fuel_type = specs[idx].find('li', {"data-code": 'fuel_type'}).getText().strip()
        except AttributeError:
            fuel_type = 'brak danych'
        location = locations[idx].getText()
        sheet[f"A{j}"] = title
        sheet[f"B{j}"] = price
        sheet[f"C{j}"] = year
        sheet[f"D{j}"] = mileage
        sheet[f"E{j}"] = engine_capacity
        sheet[f"F{j}"] = fuel_type
        sheet[f"G{j}"] = location
        sheet[f"H{j}"] = link
    print('Gotowe!')
    workbook.save(filename=f'otomoto{nowText}.xlsx')
    print(datetime.datetime.now() - begin_time)

endTime = datetime.datetime.now() - run_time
>>>>>>> 9fe3edb95d6b30237a93bb5841f119d2c5c16c67
print(f'Run time: {endTime}')
import requests
from bs4 import BeautifulSoup

def get_carsome_data(brand=None, year=None, vehicle_type=None):
    url = "https://www.carsome.my/"

    # Menentukan parameter pencarian berdasarkan merek, tahun, dan jenis kendaraan
    params = {}
    if brand:
        params['brand'] = brand
    if year:
        params['year'] = year
    if vehicle_type:
        params['type'] = vehicle_type

    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Mendapatkan data kendaraan dari hasil scraping
    cars = []
    car_elements = soup.find_all('div', class_='car-info')
    for car_element in car_elements:
        car = {}
        car['name'] = car_element.find('h3', class_='car-name').text.strip()
        car['price'] = car_element.find('div', class_='car-price').text.strip()
        car['location'] = car_element.find('div', class_='car-location').text.strip()
        car['type'] = car_element.find('div', class_='car-type').text.strip()  # Menambahkan jenis mobil
        cars.append(car)

    return cars

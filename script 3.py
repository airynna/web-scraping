import requests
from bs4 import BeautifulSoup

def scrape_vehicle_data(url):
    # Mengirim permintaan HTTP GET ke URL
    response = requests.get(url)

    # Cek apakah permintaan berhasil
    if response.status_code == 200:
        # Parsing konten HTML dengan BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Mencari informasi kendaraan
        car_elements = soup.find_all('div', class_='car-item')

        # Looping setiap kendaraan
        for car_element in car_elements:
            # Informasi Kendaraan
            name = car_element.find('h2').text.strip()
            year = car_element.find('span', class_='car-year').text.strip()
            price = car_element.find('span', class_='car-price').text.strip()
            type = car_element.find('span', class_='car-type').text.strip()

            # Menampilkan informasi kendaraan
            print("Nama: ", name)
            print("Tahun: ", year)
            print("Harga: ", price)
            print("Jenis Mobil: ", type)
            print()

    else:
        print('Gagal mengambil data. Status code:', response.status_code)

# URL untuk website Carsome, oto.com, atau OLX
url = 'https://www.oto.com/'

# Memanggil fungsi scrape_vehicle_data dengan URL
scrape_vehicle_data(url)

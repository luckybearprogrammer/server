import random
import time

import requests


# Отправка числа в API для записи в файл
def send_number_to_api(number, iduser):
    url = 'http://tinyurl.com/yc8mm6nn/write_number'
    data = {'number': number, 'iduser': iduser}
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response)
    if response.status_code == 200:
        print('Number has been sent to the API and written to the file')
    else:
        print('Failed to send the number to the API')


def can(iduser):
    url = 'http://tinyurl.com/yc8mm6nn/can'
    data = {'nick': iduser}
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response.json())
    if response.status_code == 200 and response.json()["can"]:
        print('cool')
    elif response.status_code == 200:
        print(response.json()["message"])
    else:
        print('Failed to send the number to the API')


send_number_to_api(12323, "as")

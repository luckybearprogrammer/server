import requests
import asyncio
import asyncio
import aiohttp

urlServer = "https://591e-79-165-25-253.ngrok-free.app"


async def mest(nick):
    data = {"iduser": nick}
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{urlServer}/mesto", json=data) as response:
            if response.status == 200:
                response_json = await response.json()
                return await wksajdbksaj(response_json['index'])
            else:
                return "-1"


async def wksajdbksaj(number):
    if number == 1:
        return f"{number}st"
    elif number == 2:
        return f"{number}nd"
    elif number == 3:
        return f"{number}rd"
    else:
        return f"{number}th"


def on_zapuck():
    result = asyncio.run(mest("пингвин42"))
    print(result)


# Вызовите не-асинхронную функцию on_zapuck()
on_zapuck()

# Запустить обычную функцию on_zapuck()
on_zapuck()


# Отправка числа в API для записи в файл
async def send_number_to_api(number, iduser):
    url = f'{urlServer}/write_number'
    data = {'number': number, 'iduser': iduser}
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response)
    if response.status_code == 200:
        print('Number has been sent to the API and written to the file')
    else:
        print('Failed to send the number to the API')
    await asyncio.sleep(1)


async def can(iduser):
    url = f'{urlServer}/can'
    data = {'nick': iduser}
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response.json())
    await asyncio.sleep(1)
    if response.status_code == 200 and response.json()["can"]:
        return True
    elif response.status_code == 200:
        return False
    else:
        return False


async def top():
    url = f'{urlServer}/top'
    response = requests.post(url)
    await asyncio.sleep(1)
    if response.status_code == 200:
        return response.json()["top"].split("lol")
    else:
        return "иди лесом"


async def result(nick):
    data = {"nick": nick}
    response = requests.post(f"{urlServer}/myresult", json=data)
    await asyncio.sleep(1)
    if response.status_code == 200:
        return response.json()["result"]

# def mesto(nick):
#     data = {"iduser": nick}
#     response = requests.post(f"{urlServer}/mesto", json=data)
#     if response.status_code == 200:
#         print(response.json()["index"])

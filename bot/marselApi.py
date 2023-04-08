import requests

link = "http://numbersapi.com/"  # get-запрос на определенный api
link2 = "https://catfact.ninja/facta"  # get-запрос на определенный api
response = requests.get(link2)  # отправка нашего запроса и запись в response
if response.ok:
    data = response.json()
    print(response)
    print(data['fact'])
    print(data['length'])
else:
    print("Ошибка запроса " + response.text)

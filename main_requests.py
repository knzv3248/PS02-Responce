"""
Задание 1: Получение данных
Импортируйте библиотеку requests.
Отправьте GET-запрос к открытому API (например, https://api.github.com) с параметром для поиска репозиториев с кодом html.
Распечатайте статус-код ответа.
Распечатайте содержимое ответа в формате JSON.
"""

import requests
import pprint

request_server = 'https://api.github.com/search/repositories'
params = {
            'q': 'html'
            }

response = requests.get(request_server, params=params)
print(f"\n1.1 Статус-код ответа от сервера {request_server} с параметром=\'{params['q']}\': {response.status_code}")
response_json = response.json()
print('\n1.2 Распечатка ответа в формате JSON:')
pprint.pprint(response_json)

print(f'\nКонец блока ответа сервера {request_server} в формате JSON')
print(f"Общее количество найденных ответов от сервера {request_server} с параметром=\'{params['q']}\': {response_json['total_count']}")

"""
Задание 2: Параметры запроса
Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
Отправьте GET-запрос с параметром userId, равным 1.
Распечатайте полученные записи.
"""
"""
Сделал так, как понял задание. Создал в браузере запрос. Сохранил скрины ответов. Пытался добавить файлы в проект через requests.
Благодаря Нейрокоту узнал, использовать `requests.get` для локального файла, неправильно. 
Для чтения локальных файлов используйте функции стандартной библиотеки Python.
"""
print("2. Добавляем в проект скрины ответа сервера на запрос https://jsonplaceholder.typicode.com/posts?userId=1")
img1 = r"C:\Users\Dima\Downloads\2024-06-13_00-55-55.jpg"
# Чтение локального файла
with open(img1, "rb") as file:
    img_data = file.read()

# Запись в новый файл
with open("file_json.jpg", "wb") as file:
    file.write(img_data)
print(f"Файл {img1} в проект добавлен")

img2 = r"C:\Users\Dima\Downloads\2024-06-13_00-56-11.jpg"
# Чтение локального файла
with open(img1, "rb") as file:
    img_data = file.read()
# Запись в новый файл
with open("file_raw.jpg", "wb") as file:
    file.write(img_data)
print(f"Файл {img2} в проект добавлен")

img3 = r"C:\Users\Dima\Downloads\2024-06-13_00-56-26.jpg"
# Чтение локального файла
with open(img1, "rb") as file:
    img_data = file.read()
# Запись в новый файл
with open("file_headers.jpg", "wb") as file:
    file.write(img_data)
print(f"Файл {img3} в проект добавлен")

"""
Задание 3: Отправка данных
Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
Отправьте POST-запрос с этими данными.
"""
url = "https://jsonplaceholder.typicode.com/posts"
mydata = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post(url, data=mydata)
print(f"\n3. Статус-код ответа от сервера {url} на запрос с данными {mydata}: {response.status_code}")
print(f"\nЗаголовки ответа: {response.headers}")
print(f"\nТекст ответа: {response.text}")

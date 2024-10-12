import requests
import configuration
import data


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
response = get_docs()
def get_log():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)
response = get_log()
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body)
# Определение функции для отправки POST-запроса на поиск наборов по продуктам
def  post_products_kits(product_ids):
    # Отправка POST-запроса с использованием URL из конфигурации, данных о продуктах и заголовков
    # Возвращается объект ответа, полученный от сервера
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                  json=product_ids,
                  headers=data.headers)
# Вызов функции с передачей списка ID продуктов из файла data.py
response = post_products_kits(data.product_ids)
# Вывод HTTP-статус кода ответа и тела ответа в формате JSON
# Это позволяет проверить успешность выполнения запроса и посмотреть результаты поиска наборов
# print(response.status_code)
# print(response.json())


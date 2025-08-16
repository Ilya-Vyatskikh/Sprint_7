class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'

    CREATE_COURIER_URL = f'{BASE_URL}/api/v1/courier'
    LOGIN_COURIER_URL = f'{BASE_URL}/api/v1/courier/login'
    DELETE_COURIER_URL = f'{BASE_URL}/api/v1/courier'
    ORDERS_URL = f'{BASE_URL}/api/v1/orders'


class DataForOrder:
    CREATE_ORDER_BODY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
    }

class DataForLogin:
    LOGIN_BODY = {
    "login": "ninja",
    "password": "1234"
    }
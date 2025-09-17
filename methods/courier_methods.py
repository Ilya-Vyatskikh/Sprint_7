import requests

import allure
from data import Url


class CourierMethods:
    @staticmethod
    @allure.step('Авторизация курьера')
    def login_courier(login, password):
        response = requests.post(Url.LOGIN_COURIER_URL, json={'login':login, 'password':password})
        return response

    @staticmethod
    @allure.step('Создание курьера')
    def create_courier(create_body):
        return requests.post(Url.CREATE_COURIER_URL, json=create_body)


    @staticmethod
    @allure.step('Удаление курьера по id')
    def delete_courier(courier_id):
        return requests.delete(f'{Url.DELETE_COURIER_URL}/{courier_id}')






import allure
import requests

from data import Url


class OrderMethods:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(body):
        return requests.post(Url.ORDERS_URL, json = body)


    @staticmethod
    @allure.step('Получение списка заказов')
    def get_orders_list():
        return requests.get(Url.ORDERS_URL)

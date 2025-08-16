import requests

from data import Url


class OrderMethods:
    @staticmethod
    def create_order(body):
        return requests.post(Url.ORDERS_URL, json = body)


    @staticmethod
    def get_orders_list():
        response = requests.get(Url.ORDERS_URL)
        return response

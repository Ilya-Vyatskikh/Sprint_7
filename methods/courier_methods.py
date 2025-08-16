import requests


from data import Url


class CourierMethods:
    @staticmethod
    def login_courier(login, password):
        response = requests.post(Url.LOGIN_COURIER_URL, json={'login':login, 'password':password})
        return response

    @staticmethod
    def create_courier(create_body):
        return requests.post(Url.CREATE_COURIER_URL, json=create_body)


    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f'{Url.DELETE_COURIER_URL}/{courier_id}')






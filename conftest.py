import pytest


from generators import generate_create_courier_body
from methods.courier_methods import CourierMethods


@pytest.fixture
def create_and_delete_courier():
    courier_body = generate_create_courier_body()
    login = courier_body['login']
    password = courier_body['password']
    response_create = CourierMethods.create_courier(courier_body)
    courier_id = None
    if response_create.status_code == 201:
        login_courier = CourierMethods.login_courier(login, password)
        if login_courier.status_code == 200:
            courier_id = login_courier.json().get('id')
    yield [courier_body, login, password]
    if courier_id:
        CourierMethods.delete_courier(courier_id)




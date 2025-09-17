import pytest
import allure

from generators import generate_create_courier_body
from methods.courier_methods import CourierMethods
from data import MessageError


@allure.feature('API: Курьер')
@allure.story('Создание курьера')
class TestCreateCourier:
    @allure.title('Успешное создание курьера')
    def test_success_create_courier(self, delete_courier):
        courier_body = generate_create_courier_body()
        login = courier_body['login']
        password = courier_body['password']
        with allure.step('Отправляем запрос на создание курьера'):
            response = CourierMethods.create_courier(courier_body)
        with allure.step('Проверяем, что вернулся статус ответа 201'):
            assert response.status_code == 201
        with allure.step('Проверяем тело ответа {"ok": True}'):
            assert response.json() == {'ok': True}
        delete_courier.append((login, password))


    @allure.title('Нельзя создать курьера с существующим логином')
    def test_cannot_create_duplicate_courier(self, delete_courier):
        courier_body = generate_create_courier_body()
        login = courier_body['login']
        password = courier_body['password']
        with allure.step('Создаём курьера в первый раз'):
            first_response = CourierMethods.create_courier(courier_body)
        with allure.step('Проверяем, что курьер создан в первый раз'):
            assert first_response.status_code == 201
            delete_courier.append((login, password))
        with allure.step('Повторно отправляем запрос с теми же данными'):
            second_response = CourierMethods.create_courier(courier_body)
        with allure.step('Проверяем, что сервер вернул 409'):
            assert second_response.status_code == 409
        with allure.step(f'Проверяем сообщение об ошибке:"{MessageError.COURIER_EXISTS}"'):
            assert 'message' in second_response.json()
            assert MessageError.COURIER_EXISTS in second_response.json()['message']


    @allure.title('Нельзя создать курьера без обязательного поля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_empty_field_failed(self, field):
        courier_body = generate_create_courier_body()
        with allure.step(f'Удаляем обязательное поле: {field}'):
            del courier_body[field]
        with allure.step('Отправляем запрос на создание курьера'):
            response = CourierMethods.create_courier(courier_body)
        with allure.step('Ожидаем статус 400 — недостаточно данных'):
            assert response.status_code == 400
        with allure.step(f'Проверяем, что в ответе есть сообщение об ошибке:"{MessageError.MISSING_CREATOR_DATA}"'):
            assert 'message' in response.json()
            assert MessageError.MISSING_CREATOR_DATA in response.json()['message']




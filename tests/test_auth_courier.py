import pytest
import allure
from methods.courier_methods import CourierMethods
from data import MessageError

@allure.feature('API: Авторизация курьера')
class TestAuthCourier:
    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверяем, что зарегистрированный курьер может успешно авторизоваться и получить id')
    def test_success_auth_courier(self, create_and_delete_courier):
        login, password = create_and_delete_courier
        with allure.step('Отправляем запрос на авторизацию с валидными данными'):
            auth_response = CourierMethods.login_courier(login, password)
        with allure.step('Проверяем, что сервер возвращает статус 200 и в теле ответа есть id курьера'):
            assert auth_response.status_code == 200
            assert 'id' in auth_response.json()
        with allure.step('Проверяем, что значение поля "id" — число'):
            assert isinstance(auth_response.json()['id'], int)


    @allure.title('Ошибка при пустом логине')
    @allure.description('Проверяем, что нельзя авторизоваться, если логин пустой')
    def test_auth_courier_empty_login(self, create_and_delete_courier):
        login, password = create_and_delete_courier
        with allure.step('Отправка запроса на авторизацию с пустым логином'):
            response = CourierMethods.login_courier('', password)
        with allure.step(f'Проверка статуса ответа: должен быть 400 и '
                         f'в теле ответа есть сообщение об ошибке: "{MessageError.MISSING_LOGIN_DATA}"'):
            assert response.status_code == 400
            assert 'message' in response.json()
            assert MessageError.MISSING_LOGIN_DATA in response.json()['message']


    @allure.title("Ошибка при пустом пароле")
    @allure.description("Проверяем, что нельзя авторизоваться, если пароль пустой")
    def test_auth_courier_empty_password(self, create_and_delete_courier):
        login, password = create_and_delete_courier
        with allure.step('Отправка запроса на авторизацию с пустым паролем'):
            response = CourierMethods.login_courier(login, '')
        with allure.step(f'Проверка статуса ответа: должен быть 400 и '
                         f'в теле ответа есть сообщение об ошибке: "{MessageError.MISSING_LOGIN_DATA}"'):
            assert response.status_code == 400
            assert 'message' in response.json()
            assert MessageError.MISSING_LOGIN_DATA in response.json()['message']


    @allure.title('Ошибка при неверном логине')
    @allure.description('Проверяем, что нельзя авторизоваться с несуществующим логином')
    def test_failure_auth_courier_invalid_login(self, create_and_delete_courier):
        login, password = create_and_delete_courier
        with allure.step('Отправка запроса на авторизацию с несуществующим логином'):
            response = CourierMethods.login_courier('none_login', password)
        with allure.step(f'Проверка статуса ответа: должен быть 404 '
                         f'и в теле ответа есть сообщение об ошибке: "{MessageError.COURIER_NOT_FOUND}"'):
            assert response.status_code == 404
            assert 'message' in response.json()
            assert MessageError.COURIER_NOT_FOUND in response.json()['message']


    @allure.title('Ошибка при неверном пароле')
    @allure.description('Проверяем, что нельзя авторизоваться с несуществующим паролем')
    def test_failure_auth_courier_invalid_password(self, create_and_delete_courier):
        login, password = create_and_delete_courier
        with allure.step('Отправка запроса на авторизацию с несуществующим логином'):
            response = CourierMethods.login_courier(login, 'none_password')
        with allure.step(f'Проверка статуса ответа: должен быть 404 '
                         f'и в теле ответа есть сообщение об ошибке: "{MessageError.COURIER_NOT_FOUND}"'):
            assert response.status_code == 404
            assert 'message' in response.json()
            assert MessageError.COURIER_NOT_FOUND in response.json()['message']
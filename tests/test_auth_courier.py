import pytest
import allure
from methods.courier_methods import CourierMethods

@allure.feature('API: Авторизация курьера')
class TestAuthCourier:
    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверяем, что зарегистрированный курьер может успешно авторизоваться и получить id')
    def test_success_auth_courier(self, create_and_delete_courier):
        login, password = create_and_delete_courier
        with allure.step('Отправляем запрос на логин с валидными данными'):
            auth_response = CourierMethods.login_courier(login, password)
        with allure.step('Проверяем, что сервер возвращает статус 200 и в теле ответа есть id курьера'):
            assert auth_response.status_code == 200
            assert 'id' in auth_response.json()
        with allure.step('Проверяем, что значение поля "id" — число'):
            assert isinstance(auth_response.json()['id'], int)

    @allure.title('Ошибка при входе с незаполненными обязательными полями')
    @allure.description('Проверяем, что нельзя авторизоваться, если одно из обязательных полей — пустое')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_failure_auth_courier_empty_fields(self, create_and_delete_courier, field):
        login, password = create_and_delete_courier
        empty_login = '' if field == 'login' else login
        empty_password = '' if field == 'password' else password
        with allure.step(f'Отправляем запрос с пустым полем: {field}'):
            response = CourierMethods.login_courier(empty_login, empty_password)
        with allure.step(f'Ожидаем статус 400 и проверяем, что в ответе есть сообщение об ошибке'):
            assert response.status_code == 400
            assert 'message' in response.json()
            assert 'Недостаточно данных для входа' in response.json()['message']

    @allure.title('Ошибка при неверном логине или пароле')
    @allure.description('Проверяем, что нельзя авторизоваться с несуществующими учётными данными')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_failure_auth_courier_invalid_data(self, create_and_delete_courier, field):
        login, password = create_and_delete_courier
        invalid_login = 'none_login' if field == 'login' else login
        invalid_password = 'none_pass' if field == 'password' else password
        with allure.step(f'Отправляем запрос с неверным {field}'):
            response = CourierMethods.login_courier(invalid_login, invalid_password)
        with allure.step(f'Ожидаем статус 404 и проверяем, что в ответе есть сообщение об ошибке'):
            assert response.status_code == 404
            assert 'message' in response.json()
            assert 'Учетная запись не найдена' in response.json()['message']








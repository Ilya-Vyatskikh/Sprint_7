import pytest
import allure

from methods.order_methods import OrderMethods

@allure.feature('API: Заказы')
@allure.story('Получение списка заказов')
class TestGetOrdersList:
    @allure.title('Получение списка всех заказов')
    @allure.description('Проверяем, что эндпоинт возвращает список всех заказов с кодом 200.'
                        'Ответ должен содержать поле "orders", которое является массивом.')
    def test_get_orders_list(self):
        with allure.step('Отправляем GET-запрос для получения списка всех заказов'):
            response = OrderMethods.get_orders_list()
        with allure.step('Проверяем, что сервер возвращает статус 200'):
            assert response.status_code == 200
        with allure.step('Проверяем, что в ответе присутствует поле "orders"'):
            assert 'orders' in response.json()
        with allure.step('Проверяем, что значение поля "orders" — это список'):
            assert isinstance(response.json()['orders'], list)
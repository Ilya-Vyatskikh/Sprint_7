import allure
import pytest

from methods.order_methods import OrderMethods
from helper import modify_order_body
from generators import generate_order_body

@allure.feature('API: Создание заказа')
@allure.story('Создание заказа на самокат')
class TestCreateOrder:
    @allure.title('Создание заказа с разными вариантами цвета')
    @allure.description(
        'Проверяем, что заказ можно создать с цветом BLACK, GREY, с обоими цветами или без цвета.'
        'Успешный запрос возвращает статус 201 и номер заказа (track).'
    )
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], [], ['BLACK', 'GREY']])
    def test_create_order_with_different_color_combinations(self, color):
        with allure.step(f'Формируем тело заказа с цветом: {color if color else 'не указан'}'):
            order_body = modify_order_body('color', color)
        with allure.step('Отправляем запрос на создание заказа'):
            response = OrderMethods.create_order(order_body)
        with allure.step('Проверяем, что сервер вернул статус 201 (Created)'):
            assert response.status_code == 201
        with allure.step('Проверяем, что в ответе есть номер заказа (track)'):
            assert 'track' in response.json()




class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'

    CREATE_COURIER_URL = f'{BASE_URL}/api/v1/courier'
    LOGIN_COURIER_URL = f'{BASE_URL}/api/v1/courier/login'
    DELETE_COURIER_URL = f'{BASE_URL}/api/v1/courier'
    ORDERS_URL = f'{BASE_URL}/api/v1/orders'

class MessageError:
    # Авторизация курьера
    MISSING_LOGIN_DATA = "Недостаточно данных для входа"
    COURIER_NOT_FOUND = "Учетная запись не найдена"

    # Создание курьера
    MISSING_CREATOR_DATA = "Недостаточно данных для создания учетной записи"
    COURIER_EXISTS = "Этот логин уже используется"



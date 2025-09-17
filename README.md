# Sprint_7
# 🛵 API Тесты для сервиса "Яндекс Самокат" [Яндекс Самокат](https://qa-scooter.praktikum-services.ru)
В этом проекте предстоит протестировать API учебного сервиса Яндекс Самокат.
Его документация доступна по адресу [Документация API](https://qa-scooter.praktikum-services.ru)

## 🧪 Тестируемые сценарии
### 1. Создание курьера `(POST /api/v1/courier)`

`test_success_create_courier` Проверяем успешное создание нового курьера

`test_duplicate_courier_failed` Проверяем, что нельзя создать курьера с существующим логином
   
`test_create_courier_empty_field_failed` Проверяем, что нельзя создать курьера без заполнения обязательных полей

### 2. Авторизация курьера `(POST /api/v1/courier/login)`

`test_success_auth_courier` Проверяем, что зарегистрированный курьер может успешно авторизоваться и получить id

`test_failure_auth_courier_empty_fields` Проверяем, что нельзя авторизоваться, если одно из обязательных полей — пустое
   
`test_failure_auth_courier_invalid_data` Проверяем, что нельзя авторизоваться с несуществующими учётными данными

### 3. Создание заказа `(POST /api/v1/orders)`

`test_create_order_with_different_color_combinations` Проверяем, что заказ можно создать с цветом BLACK, GREY, с обоими цветами или без цвета

### 4. Получение списка заказов `(GET /api/v1/orders)`

`test_get_orders_list` Проверяем, что эндпоинт возвращает список всех заказов.

## 🗂 Структура проекта
````
📁 Sprint_7/
├── 📁 methods/
│   ├── __init__.py           # 🧩 Инициализация модуля
│   ├── courier_methods.py    # 🛵 Методы для курьера
│   └── order_methods.py      # 📦 Методы для заказов
│
├── 📁 tests/
│   ├── __init__.py           # 🧩 Инициализация
│   ├── test_create_courier.py   # ✅ Тест: создание курьера
│   ├── test_auth_courier.py     # 🔐 Тест: авторизация
│   ├── test_create_order.py     # 📦 Тест: создание заказа
│   └── test_get_list_orders.py  # 📋 Тест: список заказов
│
├── 📁 target/
│   ├── allure-results/       # 📊 JSON-результаты Allure
│   └── allure-report/        # 🌐 HTML-отчёт Allure
│
├── 🧪 conftest.py            # 🔁 Фикстуры (setup/teardown)
├── 📄 data.py                # 🔗 Константы и URL
├── 🧰 generators.py          # 🎲 Генераторы тестовых данных
├── 🛠 helper.py               # 🔧 Вспомогательные функции
├── 📄 requirements.txt       # ⚙️ Зависимости
├── 📄 .gitignore             # 🚫 Игнорируемые файлы
└── 📄 README.md              # 📘 Документация проекта



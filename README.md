# Sprint_7
# 🛵 API Тесты для сервиса "Яндекс Самокат" https://qa-scooter.praktikum-services.ru/
В этом проекте предстоит протестировать API учебного сервиса Яндекс Самокат.
Его документация доступна по адресу https://qa-scooter.praktikum-services.ru/docs/#api

## 🧪 Тестируемые сценарии
### 1. Создание курьера `(POST /api/v1/courier)`

   `test_success_create_courier` проверяем успешное создание нового курьера

   `test_duplicate_courier_failed` проверяем, что нельзя создать курьера с существующим логином
   
   `test_create_courier_empty_field_failed` проверяем, что нельзя создать курьера без заполнения обязательных полей

### 2. Авторизация курьера `(POST /api/v1/courier/login)`





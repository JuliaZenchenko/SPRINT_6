# Sprint_6
Задача спринта:
сделать автотесты, чтобы проверить сервис для заказа самокатов https://qa-scooter.praktikum-services.ru/
1. Тесты в PyCharm (Selenium, Pytest, Allure)
2. Автотесты написаны с помощью Page Object Model и подключением Allure-отчёт.
3. Команда для запуска тестов — pytest 
4. Команда для запуска с записью отчета в allure_results: pytest --alluredir allure_results

Проект:
* allure_results - папка с отчетами allure
* locators - папка с локаторами:
  main_page_locators.py - локаторы для главной страницы 
  order_page_locators.py - локаторы для страницы заказа
* pages - папка с методами,
  base_page.py - общие методы 
  main_page.py - методы для главной страницы 
  order_page.py - методы для страницы заказа
* tests - папка с тестами:
  test_main_page.py - тесты для главной страницы 
  test_order_page.py - тесты для страницы заказа
  test_redirects.py - тесты для редиректа
* conftest.py - фикстуры
* data.py - данные для параметризации
* README.md - описание проекта
* requirements - файл с внешними зависимостями

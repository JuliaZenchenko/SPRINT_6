import allure

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data import Urls


class TestRedirects:
    @allure.title('Проверка перехода на страницу "Дзен" с помощью логотипа "Яндекс"')
    def test_go_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_element(MainPageLocators.LOGO_YANDEX)
        main_page.jump_new_tab()
        main_page.wait_for_load_page(Urls.DZEN_URL)
        assert Urls.DZEN_URL in main_page.get_url_for_page_for_test()

    @allure.title('Проверка перехода на главную страницу')
    def test_go_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_header_order_button()
        result = main_page.click_to_logo_and_get_content()
        assert "Вопросы о важном" in result
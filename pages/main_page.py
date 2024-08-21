import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Проскроллить до блока с вопросами')
    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.BLOCK_QUESTIONS)

    @allure.step('Кликнуть на вопрос')
    def click_questions(self, locator):
        self.click_on_element(locator)

    @allure.step('Нажатие на кнопку Заказ в верхней части сайта')
    def click_to_header_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Клик по лого "Самокат" и получение текста "Самокат на пару дней"')
    def click_to_logo_and_get_content(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)
        self.scroll_to_element(MainPageLocators.QUESTIONS)
        return self.get_text_from_element(MainPageLocators.QUESTIONS)





import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import *

class OrderPage(BasePage):
    order_url = Urls.ORDER_URL

    @allure.step(f"Переход на страницу оформления заказа {order_url}")
    @allure.step("Перейти на страницу заказа")
    def go_to_order_url(self):
        self.driver.get(self.order_url)

    @allure.step('Открытие формы "Метро" и выбор станции')
    def get_metro(self, locator_metro, locator_station):
        self.click_on_element(locator_metro)
        self.click_on_element(locator_station)

    @allure.step('Заполнение поля "Дата"')
    def set_text_to_date_form(self, date_locator, date):
        self.set_text_to_element(date_locator, date)

    @allure.step("Выбор срока аренды")
    def period_of_time(self, combox_locator, period_locator):
        self.click_on_element(combox_locator)
        self.click_on_element(period_locator)

    @allure.step("Клик на кнопку Далее")
    def next_button(self):
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Ожидание и клик по кнопке Заказать")
    def order_button(self):
        self.wait_until_clickable(OrderPageLocators.BUTTON_ORDER)
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step("Заполнение формы Для кого Самокат")
    def first_form_metro(self):
        self.set_text_to_element(OrderPageLocators.NAME, DataOrderForm.name)
        self.set_text_to_element(OrderPageLocators.SURNAME, DataOrderForm.surname)
        self.set_text_to_element(OrderPageLocators.ADDRESS, DataOrderForm.street)
        self.get_metro(OrderPageLocators.METRO, OrderPageLocators.METRO_STATION)
        self.set_text_to_element(OrderPageLocators.PHONE_NUMBER, DataOrderForm.number)


    @allure.step("Заполнение формы Про аренду")
    def second_form(self):
        self.set_text_to_date_form(OrderPageLocators.DATE, DataOrderForm.date_20082024)
        self.click_on_element(OrderPageLocators.BLACK_COLOR)
        self.period_of_time(OrderPageLocators.RENT_PERIOD, OrderPageLocators.THREE_DAYS)

    @allure.step('Нажать на кнопку "Да" в модальном окне Хотите оформить заказ?')
    def click_yes_button(self):
        return self.wait_until_clickable(OrderPageLocators.YES_BUTTON)

    @allure.step('Дождаться открытия модального окна Хотите оформить заказ?')
    def wait_confirm_modal(self):
        return self.wait_and_find_element(OrderPageLocators.CONFIRM_MODAL)

    @allure.step("Нажатие на кнопки заказа")
    def result(self):
        self.wait_and_find_element(OrderPageLocators.BUTTON_ORDER)
        self.order_button()
        self.wait_confirm_modal()
        self.click_yes_button()
        self.click_on_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Дождаться открытия модального окна с оформлением заказа')
    def wait_order_confirm(self):
        return self.wait_and_find_element(OrderPageLocators.ORDER_MODAL)
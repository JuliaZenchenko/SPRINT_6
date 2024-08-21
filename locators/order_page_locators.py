from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME = (By.XPATH, './/input[@placeholder = "* Имя"]')
    SURNAME = (By.XPATH, './/input[@placeholder = "* Фамилия"]')
    ADDRESS = (By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]')
    PHONE_NUMBER = (By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]')
    DATE = (By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]')
    METRO = (By.XPATH, './/div[@class="select-search"]')
    METRO_STATION = (By.XPATH, './/button[@value="4"]')  # Сокольники
    RENT_PERIOD = (By.XPATH, './/div[text() = "* Срок аренды"]')
    THREE_DAYS = (By.XPATH, './/div[text()="трое суток"]')
    BUTTON_NEXT = (By.XPATH, './/button[text() = "Далее"]')
    BLACK_COLOR = (By.XPATH, './/label[@for = "black"]')
    BUTTON_ORDER = (By.XPATH, './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]')
    YES_BUTTON = (By.XPATH, './/button[text() = "Да"]')
    CONFIRM_MODAL = (By.CLASS_NAME, 'Order_Modal__YZ-d3')
    ORDER_MODAL = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
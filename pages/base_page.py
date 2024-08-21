import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

class BasePage:
    @allure.step("Открыть браузер")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать и найти элемент")
    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Проскроллить до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получить текст из элемента")
    def get_text_from_element(self, locator):
        element = self.wait_and_find_element(locator)
        return element.text

    @allure.step("Дождаться пока элемент станет кликабельный")
    def wait_until_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
    @allure.step("Кликнуть по элементу")
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element = self.wait_and_find_element(locator)
        element.click()


    @allure.step("Заполнить поле")
    def set_text_to_element(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.send_keys(text)

    @allure.step("Переход на другую страницу")
    def jump_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Получить текущий url")
    def get_url_for_page_for_test(self):
        return self.driver.current_url

    @allure.step("Дождаться загрузки страницы")
    def wait_for_load_page(self, url):
        WebDriverWait(self.driver, timeout=15).until(EC.url_to_be(url))

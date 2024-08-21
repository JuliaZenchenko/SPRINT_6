from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_HEADER = (By.XPATH, './/button[@class = "Button_Button__ra12g"]')
    SCOOTER_LOGO = (By.XPATH, './/a[@class = "Header_LogoScooter__3lsAR"]')
    LOGO_YANDEX = (By.XPATH, './/a[@href="//yandex.ru"]')
    QUESTIONS = (By.XPATH, './/div[text() = "Вопросы о важном"]')
    BLOCK_QUESTIONS = (By.ID, "accordion__heading-7")

    # локатор поля «Сколько это стоит? И как оплатить?»
    QUESTION_1 = (By.ID, "accordion__heading-0")
    # локатор поля «Хочу сразу несколько самокатов! Так можно?»
    QUESTION_2 = (By.ID, "accordion__heading-1")
    # локатор поля «Как рассчитывается время аренды?»
    QUESTION_3 = (By.ID, "accordion__heading-2")
    # локатор поля «Можно ли заказать самокат прямо на сегодня?»
    QUESTION_4 = (By.ID, "accordion__heading-3")
    # локатор поля «Можно ли продлить заказ или вернуть самокат раньше?»
    QUESTION_5 = (By.ID, "accordion__heading-4")
    # локатор поля «Вы привозите зарядку вместе с самокатом?»
    QUESTION_6 = (By.ID, "accordion__heading-5")
    # локатор поля «Можно ли отменить заказ?»
    QUESTION_7 = (By.ID, "accordion__heading-6")
    # локатор поля «Я жизу за МКАДом, привезёте?»
    QUESTION_8 = (By.ID, "accordion__heading-7")

    # ответ на вопрос 1
    ANSWER_1 = (By.ID, "accordion__panel-0")
    # ответ на вопрос 2
    ANSWER_2 = (By.ID, "accordion__panel-1")
    # ответ на вопрос 3
    ANSWER_3 = (By.ID, "accordion__panel-2")
    # ответ на вопрос 4
    ANSWER_4 = (By.ID, "accordion__panel-3")
    # ответ на вопрос 5
    ANSWER_5 = (By.ID, "accordion__panel-4")
    # ответ на вопрос 6
    ANSWER_6 = (By.ID, "accordion__panel-5")
    # ответ на вопрос 7
    ANSWER_7 = (By.ID, "accordion__panel-6")
    # ответ на вопрос 8
    ANSWER_8 = (By.ID, "accordion__panel-7")



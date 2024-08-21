import pytest
import allure

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data import Urls, DataAnswer


class TestMainPage:
    @allure.title("Cравнение с ожидаемым ответом")
    @pytest.mark.parametrize('question, answer, expected_result',
                             [(MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1, DataAnswer.ANSWER_1),
                              (MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2, DataAnswer.ANSWER_2),
                              (MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3, DataAnswer.ANSWER_3),
                              (MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4, DataAnswer.ANSWER_4),
                              (MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5, DataAnswer.ANSWER_5),
                              (MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6, DataAnswer.ANSWER_6),
                              (MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7, DataAnswer.ANSWER_7),
                              (MainPageLocators.QUESTION_8, MainPageLocators.ANSWER_8, DataAnswer.ANSWER_8)
                              ]
                             )
    def test_success_text_of_response(self, driver, question, answer, expected_result):
        main_page = MainPage(driver)
        main_page.scroll_to_questions()
        main_page.click_questions(question)
        text_answer = main_page.get_text_from_element(answer)
        assert text_answer == expected_result

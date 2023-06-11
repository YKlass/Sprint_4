import pytest
import allure
from locators import MainPageLocators
from pages.main_page import MainPage
from data import QuestionsAnswers


class TestQuestions:

    @allure.title("Проверка соответствия вопросов и ответов")
    @pytest.mark.parametrize('question_index', [i for i in range(8)])
    def test_questions_and_answers(self, question_index, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.scroll_down()
        main_page.check_answers_for_important_questions(question_index)
        actual_result = main_page.find_elements(MainPageLocators.IMPORTANT_ANSWERS)[question_index].text
        expected_result = QuestionsAnswers.questions_and_answers[main_page.find_elements(
            MainPageLocators.IMPORTANT_QUESTIONS)[question_index].text]
        assert actual_result == expected_result, 'Ответ не соответствует вопросу'

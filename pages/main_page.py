import allure
from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Клик на вопрос")
    def check_answers_for_important_questions(self, question_index):
        base_page = BasePage(self.driver)
        list_of_questions = base_page.find_elements(MainPageLocators.IMPORTANT_QUESTIONS)
        base_page.wait_element(MainPageLocators.IMPORTANT_QUESTIONS)
        list_of_questions[question_index].click()

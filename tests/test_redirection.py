import allure

from locators import MainPageLocators, BasePageLocators
from pages.base_page import BasePage
from data import Urls


class TestTransitions:

    @allure.title("Проверка перехода на главную страницу Самоката при клике на лого Самоката")
    def test_click_scooter_logo_go_to_samokat_page(self, driver):
        base_page = BasePage(driver)
        driver.get(Urls.SAMOKAT_ORDER_PAGE_URL)
        base_page.click_scooter_logo()
        assert base_page.find_element(MainPageLocators.DELIVER_SCOOTER_FOR_YOU), \
            'При клике на лого Самоката переход на главную страницу Самоката не произошел'

    @allure.title("Проверка перехода на главную страницу Яндекса при клике на лого Яндекса")
    def test_press_yandex_logo_go_to_yandex_page(self, driver):
        base_page = BasePage(driver)
        base_page.click_yandex_logo()
        base_page.wait_element(BasePageLocators.YANDEX_LOGO)
        driver.switch_to.window(driver.window_handles[1])
        assert base_page.find_element(BasePageLocators.YANDEX_SEARCH), \
            'При клике на лого Яндекса переход на главную страницу Яндекса не произошел'

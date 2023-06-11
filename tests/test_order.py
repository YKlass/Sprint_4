import pytest
import allure
from locators import OrderPageLocators
from pages.order_page import OrderPage
from data import user_1, user_2


class TestOrder:

    @allure.title("Проверка оформления заказа кнопкой Заказать в хэдере")
    @pytest.mark.parametrize('user', [user_1, user_2])
    def test_order_by_click_header_order_button(self, driver, user):
        order_page = OrderPage(driver)
        order_page.accept_cookies()
        order_page.click_order_button_header()
        order_page.make_order(user)
        order_text = order_page.find_element(OrderPageLocators.SUCCESS_ORDER_MODAL_WINDOW).text
        assert "Заказ оформлен" in order_text, 'Ошибка во время оформления заказа'


    @allure.title("Проверка оформления заказа кнопкой Заказать в центре страницы")
    @pytest.mark.parametrize('user', [user_1, user_2])
    def test_order_by_click_order_button_middle(self, driver, user):
        order_page = OrderPage(driver)
        order_page.accept_cookies()
        order_page.click_order_button_middle()
        order_page.make_order(user)
        order_text = order_page.find_element(OrderPageLocators.SUCCESS_ORDER_MODAL_WINDOW).text
        assert "Заказ оформлен" in order_text, "Ошибка во время оформления заказа"

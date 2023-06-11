import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators import OrderPageLocators


class OrderPage(BasePage):
    def send_key(self, locator, key):
        return self.find_element(locator).send_keys(key)

    @allure.step("Клик на кнопку 'Заказать' в шапке")
    def click_order_button_header(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Нажимаем на кнопку 'Заказать' в центре главной страницы")
    def click_order_button_middle(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_MIDDLE)

    @allure.step("Заполнение поля Имя")
    def input_name(self, name):
        self.send_key(OrderPageLocators.USER_NAME, name)

    @allure.step("Заполнение поля 'Фамилия'")
    def input_surname(self, surname):
        self.send_key(OrderPageLocators.USER_SURNAME, surname)

    @allure.step("Заполняем поле 'Адрес'")
    def input_address(self, address):
        self.send_key(OrderPageLocators.USER_ADDRESS, address)

    @allure.step("Выбор станции метро")
    def choose_subway_station(self, station):
        self.click_element(OrderPageLocators.METRO_DROPDOWN)
        self.send_key(OrderPageLocators.METRO_DROPDOWN, station)
        self.send_key(OrderPageLocators.METRO_DROPDOWN, Keys.ARROW_DOWN + Keys.ENTER)

    @allure.step("Заполняем поле 'Телефон'")
    def input_user_phone(self, phone):
        self.send_key(OrderPageLocators.USER_PHONE, phone)

    @allure.step("Нажимаем 'Далее'")
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбираем дату")
    def choose_order_date(self, date):
        self.send_key(OrderPageLocators.ORDER_DATE, date)
        self.send_key(OrderPageLocators.ORDER_DATE, Keys.ENTER)

    @allure.step("Выбираем срок аренды")
    def choose_rental_duration(self, period):
        self.click_element(OrderPageLocators.RENTAL_DURATION)
        self.click_element(OrderPageLocators.rental_duration_option(period))

    @allure.step("Выбираем цвет самоката")
    def choose_scooter_color(self, black_color, grey_color):
        if black_color:
            self.click_element(OrderPageLocators.SCOOTER_COLOR_CHECKBOX_BLACK)
        if grey_color:
            self.click_element(OrderPageLocators.SCOOTER_COLOR_CHECKBOX_GREY)

    @allure.step("Пишем комментарий")
    def write_comment(self, comment):
        self.send_key(OrderPageLocators.COMMENTS, comment)

    @allure.step("Нажимаем 'Заказать'")
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.click_element(OrderPageLocators.YES_ORDER_BUTTON)

    @allure.step("Оформляем заказ")
    def make_order(self, user):
        self.input_name(user.name)
        self.input_surname(user.surname)
        self.input_address(user.address)
        self.choose_subway_station(user.station)
        self.input_user_phone(user.phone)
        self.click_next_button()
        self.choose_order_date(user.date)
        self.choose_rental_duration(user.period)
        self.choose_scooter_color(user.black_color, user.grey_color)
        self.write_comment(user.comment)
        self.click_order_button()
        self.confirm_order()

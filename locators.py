from selenium.webdriver.common.by import By


class BasePageLocators:
    ACCEPT_COOKIES_BUTTON = [By.XPATH, ".//button[text()='да все привыкли']"]
    YANDEX_LOGO = [By.XPATH, ".//*[@alt='Yandex']"]  # Логотип яндекса
    SCOOTER_LOGO = [By.XPATH, ".//*[@alt='Scooter']"]  # Логотип самоката
    ORDER_STATUS_BUTTON = [By.XPATH, ".//button[text()='Статус заказа']"]
    YANDEX_SEARCH = [By.XPATH, './/iframe[@aria-label="Поиск Яндекса"]']


class MainPageLocators:

    IMPORTANT_QUESTIONS_HEADER = (By.XPATH, './/div[text()]="Вопросы о важном"')  # Заголовок Вопросы о важном
    IMPORTANT_QUESTIONS = (By.XPATH, './/*[contains(@id, "accordion__heading-")]')  # Важный вопрос
    IMPORTANT_ANSWERS = (By.XPATH, './/*[contains(@id, "accordion__panel-")]/p')  # Важный ответ
    QUESTIONS_ANSWERS_FIELD = [By.XPATH, './/*[@class="accordion"]']  # Поле с вопросами и ответами
    DELIVER_SCOOTER_FOR_YOU = (By.XPATH, './/*[text()[contains(., "Привезём его прямо к вашей")]]')  # Заголовок на главной странице


class OrderPageLocators:

    @classmethod
    def rental_duration_option(cls, period):
        return [By.XPATH, f"//div[@role='option' and text() = '{period}']"]

    ORDER_BUTTON_HEADER = [By.XPATH, "//button[@class = 'Button_Button__ra12g' and text()='Заказать']"]  # Кнопка Заказать в шапке
    ORDER_BUTTON_MIDDLE = [By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"]  # Кнопка Заказать внизу
    USER_NAME = [By.XPATH, "//input[contains(@placeholder,'Имя')]"]  # Имя
    USER_SURNAME = [By.XPATH, "//input[contains(@placeholder, '* Фамилия')]"]  # Фамилия
    USER_ADDRESS = [By.XPATH, "//input[contains(@placeholder, '* Адрес: куда привезти заказ')]"]  # Адрес
    METRO_DROPDOWN = [By.XPATH, "//input[contains(@placeholder, '* Станция метро')]"]  # Cтанция метро
    USER_PHONE = [By.XPATH, "//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]"]  # Телефон
    NEXT_BUTTON = [By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Далее']"]  # Кнопка Далее
    ORDER_DATE = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]  # Выбор даты заказа
    RENTAL_DURATION = [By.XPATH, "//div[text()='* Срок аренды']"]  # Срок аренды (поле)
    RENTAL_DURATION_DROPDOWN = [By.XPATH, "//div[@role='option']"]  # Дропдаун со сроками аренды
    SCOOTER_COLOR_CHECKBOX_BLACK = [By.ID, 'black']  # Выбор черного самоката
    SCOOTER_COLOR_CHECKBOX_GREY = [By.ID, 'grey']  # Выбор серого самоката
    COMMENTS = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]  # Комментарий
    ORDER_BUTTON = [By.XPATH, "//button[text()='Назад']/parent::div/button[text()='Заказать']"]  # Кнопка Заказать
    BACK_BUTTON = [By.XPATH, "//button[text()='Назад']"]  # Кнопка Назад
    CONFIRMATION_MODAL_WINDOW = [By.XPATH, "//div[starts-with(text(), 'Хотите')]"]  # Модалка подтверждения заказа
    YES_ORDER_BUTTON = [By.XPATH, ".//button[text()='Да']"]  # Кнопка Да, хочу оформить заказ
    SUCCESS_ORDER_MODAL_WINDOW = [By.XPATH, "//div[starts-with(text(), 'Заказ')]"]  # Модалка успешно созданного заказа
    ORDER_NUMBER = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"]  # Текст с номером заказа на модалке
    STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"]  # Кнопка Посмотреть статус



from selenium.webdriver.common.by import By

from data import BASE_URL
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

# Page object главной страницы Самоката.

class MainPage(BasePage):

    def open_main_page(self):
        # Открыть главную страницу сайта
        self.open_page(BASE_URL)

    def accept_cookies(self):
        # Принять куки, если баннер появился
        if self.driver.find_elements(*MainPageLocators.COOKIE_ACCEPT_BUTTON):
            self.click_on_element(MainPageLocators.COOKIE_ACCEPT_BUTTON)

    def click_order_button_top(self):
        # Нажать верхнюю кнопку «Заказать»
        self.click_on_element(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        # Прокрутить страницу к нижней кнопке и нажать её
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_faq_question(self, index):
        # Собрать локатор вопроса FAQ по индексу
        question_locator = (
            By.ID,
            MainPageLocators.FAQ_QUESTION_ID_TEMPLATE.format(index)
        )
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)

    def get_faq_answer_text(self, index):
        # Собрать локатор ответа FAQ по индексу вопроса
        answer_locator = (
            By.XPATH,
            MainPageLocators.FAQ_ANSWER_XPATH_TEMPLATE.format(index)
        )
        return self.get_text_from_element(answer_locator)

    def click_scooter_logo(self):
        # Нажать логотип Самоката
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        # Нажать логотип Яндекса
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

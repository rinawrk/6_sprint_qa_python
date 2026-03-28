from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

# Page object страницы заказа самоката.

class OrderPage(BasePage):

    def fill_first_step(self, order_data):
        # Заполнить первый шаг заказа: имя, фамилию, адрес, метро и телефон.
        self.fill_input(OrderPageLocators.NAME_INPUT, order_data["name"])
        self.fill_input(OrderPageLocators.SURNAME_INPUT, order_data["surname"])
        self.fill_input(OrderPageLocators.ADDRESS_INPUT, order_data["address"])
        self.select_metro_station(order_data["metro"])
        self.fill_input(OrderPageLocators.PHONE_INPUT, order_data["phone"])
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    def select_metro_station(self, station_name):
        # Выбрать станцию метро из выпадающего списка по её названию.
        self.fill_input(OrderPageLocators.METRO_INPUT, station_name)

        metro_option = (
            By.XPATH,
            OrderPageLocators.METRO_OPTION_XPATH_TEMPLATE.format(station_name)
        )
        self.click_on_element(metro_option)

    def fill_second_step(self, order_data):
        # Заполнить второй шаг заказа: дату, срок аренды, цвет и комментарий.
        self.set_delivery_date(order_data["delivery_date"])
        self.select_rent_period(order_data["rent_period"])

        if order_data["color"] == "black":
            self.click_on_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        elif order_data["color"] == "grey":
            self.click_on_element(OrderPageLocators.GREY_COLOR_CHECKBOX)

        self.fill_input(OrderPageLocators.COMMENT_INPUT, order_data["comment"])

    def set_delivery_date(self, delivery_date):
        # Ввести дату доставки в поле и подтвердить ввод клавишей Enter.
        date_input = self.find_visible_element(OrderPageLocators.DELIVERY_DATE_INPUT)
        date_input.clear()
        date_input.send_keys(delivery_date)
        date_input.send_keys(Keys.ENTER)

    def select_rent_period(self, rent_period):
        # Выбрать срок аренды из выпадающего списка по тексту.
        self.click_on_element(OrderPageLocators.RENT_PERIOD_DROPDOWN)

        rent_option = (
            By.XPATH,
            OrderPageLocators.RENT_PERIOD_OPTION_XPATH_TEMPLATE.format(rent_period)
        )
        self.click_on_element(rent_option)

    def click_order_button(self):
        # Нажать кнопку «Заказать» на втором шаге оформления.
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        # Подтвердить оформление заказа в модальном окне.
        self.click_on_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    def is_order_success_visible(self):
        # Проверить, что появилось модальное окно с успешным оформлением заказа.
        return self.find_visible_element(
            OrderPageLocators.SUCCESS_MODAL_HEADER
        ).is_displayed()

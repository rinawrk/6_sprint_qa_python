import pytest

from data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage

# Тесты позитивного сценария оформления заказа.

class TestOrder:

    @pytest.mark.parametrize("order_data", ORDER_DATA)
    def test_create_order_successfully(self, driver, order_data):
        # Создать объекты страниц
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Открыть главную страницу и принять куки
        main_page.open_main_page()
        main_page.accept_cookies()

        # Открыть форму заказа через нужную кнопку
        if order_data["entry_point"] == "top":
            main_page.click_order_button_top()
        elif order_data["entry_point"] == "bottom":
            main_page.click_order_button_bottom()

        # Заполнить первый и второй шаг заказа
        order_page.fill_first_step(order_data)
        order_page.fill_second_step(order_data)

        # Нажать кнопку оформления и подтвердить заказ
        order_page.click_order_button()
        order_page.confirm_order()

        # Проверить, что появилось успешное модальное окно
        assert order_page.is_order_success_visible()

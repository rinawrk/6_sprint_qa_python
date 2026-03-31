import allure

from data import ORDER_DATA_TOP, ORDER_DATA_BOTTOM
from pages.main_page import MainPage
from pages.order_page import OrderPage

# Тесты позитивного сценария оформления заказа.

class TestOrder:

    @allure.title("Успешное оформление заказа через верхнюю кнопку")
    @allure.description("Проверка полного позитивного сценария оформления заказа через верхнюю кнопку 'Заказать'")
    
    def test_create_order_from_top_button(self, driver):
        # Создать объекты страниц
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Открыть главную страницу и принять куки
        main_page.open_main_page()
        main_page.accept_cookies()

        # Открыть форму заказа через верхнюю кнопку
        main_page.click_order_button_top()

        # Заполнить первый и второй шаг заказа
        order_page.fill_first_step(ORDER_DATA_TOP)
        order_page.fill_second_step(ORDER_DATA_TOP)

        # Нажать кнопку оформления и подтвердить заказ
        order_page.click_order_button()
        order_page.confirm_order()

        # Проверить, что появилось успешное модальное окно
        assert order_page.is_order_success_visible()

    @allure.title("Успешное оформление заказа через нижнюю кнопку")
    @allure.description("Проверка полного позитивного сценария оформления заказа через нижнюю кнопку 'Заказать'")
    
    def test_create_order_from_bottom_button(self, driver):
        # Создать объекты страниц
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Открыть главную страницу и принять куки
        main_page.open_main_page()
        main_page.accept_cookies()

        # Открыть форму заказа через нижнюю кнопку
        main_page.click_order_button_bottom()

        # Заполнить первый и второй шаг заказа
        order_page.fill_first_step(ORDER_DATA_BOTTOM)
        order_page.fill_second_step(ORDER_DATA_BOTTOM)

        # Нажать кнопку оформления и подтвердить заказ
        order_page.click_order_button()
        order_page.confirm_order()

        # Проверить, что появилось успешное модальное окно
        assert order_page.is_order_success_visible()

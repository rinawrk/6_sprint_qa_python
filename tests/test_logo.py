from data import BASE_URL, DZEN_URL_PART
from pages.main_page import MainPage

# Тесты логотипов в шапке сайта.

class TestLogo:

    def test_scooter_logo_redirects_to_main_page(self, driver):
        # Создать объект главной страницы
        main_page = MainPage(driver)

        # Открыть главную страницу и принять куки
        main_page.open_main_page()
        main_page.accept_cookies()

        # Перейти на страницу заказа через верхнюю кнопку
        main_page.click_order_button_top()

        # Нажать логотип Самоката
        main_page.click_scooter_logo()

        # Проверить, что открылась главная страница
        assert main_page.get_current_url() == BASE_URL

    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        # Создать объект главной страницы
        main_page = MainPage(driver)

        # Открыть главную страницу и принять куки
        main_page.open_main_page()
        main_page.accept_cookies()

        # Нажать логотип Яндекса
        main_page.click_yandex_logo()

        # Переключиться на новую вкладку
        main_page.switch_to_new_tab()

        # Дождаться финального URL после редиректов
        main_page.wait_for_url_contains(DZEN_URL_PART)

        # Проверить, что открылась страница Дзена
        assert DZEN_URL_PART in main_page.get_current_url()

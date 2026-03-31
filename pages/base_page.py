import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Базовый класс: общие методы работы с браузером и элементами страницы.

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу: {url}")
    def open_page(self, url):
        # Открыть страницу по переданному URL
        self.driver.get(url)

    @allure.step("Найти видимый элемент")
    def find_visible_element(self, locator):
        # Найти элемент после ожидания его видимости
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти кликабельный элемент")
    def find_clickable_element(self, locator):
        # Найти элемент после ожидания, что по нему можно кликнуть
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть по элементу")
    def click_on_element(self, locator):
        # Кликнуть по элементу
        self.find_clickable_element(locator).click()

    @allure.step("Заполнить поле значением: {text}")
    def fill_input(self, locator, text):
        # Ввести текст в поле
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text_from_element(self, locator):
        # Получить текст элемента
        return self.find_visible_element(locator).text

    @allure.step("Прокрутить страницу до элемента")
    def scroll_to_element(self, locator):
        # Прокрутить страницу до элемента
        element = self.find_visible_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        # Получить текущий URL страницы
        return self.driver.current_url

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self):
        # Дождаться открытия второй вкладки и переключиться на неё
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Дождаться, пока URL будет содержать: {text}")
    def wait_for_url_contains(self, text):
        # Дождаться, пока в URL появится нужный текст
        self.wait.until(EC.url_contains(text))

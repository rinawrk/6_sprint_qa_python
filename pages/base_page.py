from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    # Базовый класс: общие методы работы с браузером и элементами страницы.
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Открыть страницу по переданному URL
    def open_page(self, url):
        self.driver.get(url)

    # Найти элемент после ожидания его видимости
    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    # Найти элемент после ожидания, что по нему можно кликнуть
    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    # Кликнуть по элементу
    def click_on_element(self, locator):
        self.find_clickable_element(locator).click()

    # Ввести текст в поле
    def fill_input(self, locator, text):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)

    # Получить текст элемента
    def get_text_from_element(self, locator):
        return self.find_visible_element(locator).text

    # Прокрутить страницу до элемента
    def scroll_to_element(self, locator):
        element = self.find_visible_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Получить текущий URL страницы
    def get_current_url(self):
        return self.driver.current_url

    # Дождаться открытия второй вкладки и переключиться на неё
    def switch_to_new_tab(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

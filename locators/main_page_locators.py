from selenium.webdriver.common.by import By


class MainPageLocators:

    # Кнопка принятия куки внизу страницы
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

    # Верхняя кнопка «Заказать» в шапке сайта
    ORDER_BUTTON_TOP = (
        By.XPATH,
        "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']"
    )

    # Нижняя кнопка «Заказать» внизу главной страницы
    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']"
    )

    # Логотип Яндекса в шапке сайта
    YANDEX_LOGO = (By.CSS_SELECTOR, 'a[class*="Header_LogoYandex"]')

    # Логотип Самоката в шапке сайта
    SCOOTER_LOGO = (By.CSS_SELECTOR, 'a[class*="Header_LogoScooter"]')

    @staticmethod
    def faq_question_by_index(index: int):

        # Локатор вопроса в FAQ по его индексу
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def faq_answer_by_index(index: int):

        # Локатор текста ответа в FAQ по индексу вопроса
        return By.XPATH, f"//div[@id='accordion__panel-{index}']/p"
    
from selenium.webdriver.common.by import By


class MainPageLocators:
    
    # Кнопка принятия куки
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

    # Шаблон id вопроса в FAQ по индексу
    FAQ_QUESTION_ID_TEMPLATE = "accordion__heading-{}"

    # Шаблон xpath ответа в FAQ по индексу
    FAQ_ANSWER_XPATH_TEMPLATE = "//div[@id='accordion__panel-{}']/p"

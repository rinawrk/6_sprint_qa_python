from selenium.webdriver.common.by import By


class OrderPageLocators:
    
    # --- Первый шаг заказа: «Для кого самокат» ---

    # Поле ввода имени
    NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')

    # Поле ввода фамилии
    SURNAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')

    # Поле ввода адреса доставки
    ADDRESS_INPUT = (
        By.CSS_SELECTOR,
        'input[placeholder="* Адрес: куда привезти заказ"]'
    )

    # Поле выбора станции метро
    METRO_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')

    # Шаблон xpath для станции метро по её названию
    METRO_OPTION_XPATH_TEMPLATE = "//div[text()='{}']"

    # Поле ввода телефона
    PHONE_INPUT = (
        By.CSS_SELECTOR,
        'input[placeholder="* Телефон: на него позвонит курьер"]'
    )

    # Кнопка перехода ко второму шагу заказа
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # --- Второй шаг заказа: «Про аренду» ---

    # Поле ввода даты доставки
    DELIVERY_DATE_INPUT = (
        By.CSS_SELECTOR,
        'input[placeholder="* Когда привезти самокат"]'
    )

    # Выпадающий список срока аренды
    RENT_PERIOD_DROPDOWN = (
        By.XPATH,
        "//div[contains(@class, 'Dropdown-control')]"
    )

    # Шаблон xpath для пункта срока аренды по его тексту
    RENT_PERIOD_OPTION_XPATH_TEMPLATE = (
        "//div[contains(@class, 'Dropdown-option') and text()='{}']"
    )

    # Чекбокс цвета «чёрный жемчуг»
    BLACK_COLOR_CHECKBOX = (By.ID, "black")

    # Чекбокс цвета «серая безысходность»
    GREY_COLOR_CHECKBOX = (By.ID, "grey")

    # Поле комментария для курьера
    COMMENT_INPUT = (
        By.CSS_SELECTOR,
        'input[placeholder="Комментарий для курьера"]'
    )

    # Кнопка оформления заказа на втором шаге
    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"
    )

    # --- Модальные окна ---

    # Кнопка подтверждения заказа «Да»
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Заголовок модального окна успешного заказа
    SUCCESS_MODAL_HEADER = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader') and contains(., 'Заказ оформлен')]"
    )

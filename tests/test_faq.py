import pytest

from data import FAQ_DATA
from pages.main_page import MainPage

# Тесты блока «Вопросы о важном».

class TestFAQ:

    @pytest.mark.parametrize("question_index, expected_answer", FAQ_DATA)
    def test_faq_answer_text(self, driver, question_index, expected_answer):
        # Создать объект главной страницы
        main_page = MainPage(driver)

        # Открыть главную страницу и принять куки
        main_page.open_main_page()
        main_page.accept_cookies()

        # Раскрыть нужный вопрос FAQ
        main_page.click_faq_question(question_index)

        # Получить текст ответа
        actual_answer = main_page.get_faq_answer_text(question_index)

        # Проверить, что текст ответа совпадает с ожидаемым
        assert actual_answer == expected_answer

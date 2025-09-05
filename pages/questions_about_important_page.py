from pages.base_page import BasePage


class QuestionAboutImportantPage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)

    def check_answer_to_question(self, locator, text):
        """Проверяем ответ на вопрос через сравнение текстов"""
        self.check_text_matches(locator, text)

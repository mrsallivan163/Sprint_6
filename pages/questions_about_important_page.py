from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class QuestionAboutImportantPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 5)

    def check_answer_to_question(self, locator, text):
        """Проверяем ответ на вопрос через сравнение текстов"""
        self.check_text_matches(locator, text)

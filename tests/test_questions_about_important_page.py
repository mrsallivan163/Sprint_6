from selenium import webdriver
import allure

from pages.questions_about_important_page import QuestionAboutImportantPage
from locators.question_about_important_page_lct import QuestionAboutImportantPageLocators
from locators.base_lct import BaseLocators
from data_layer.question_about_important_page_dl import DataLayer
from config import Url


@allure.suite('Яндекс Самокат. Блок "Вопросы о важном"')
class TestAnswersToImportantQuestions():

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.question = QuestionAboutImportantPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def setup_method(self):
        self.driver.get(Url.MAIN_URL)
        self.question.confirm_cookies(BaseLocators.CONFIRM_COOKIES)

    @allure.title('Проверка ответа на вопрос "Сколько это стоит? И как оплатить?"')
    def test_answer_cost_rent(self):
        with allure.step('Кликаем на вопрос'):
            self.question.click_on_element(QuestionAboutImportantPageLocators.QUESTIONS_COST_RENT)
        with allure.step('Проверяем ответ на вопрос'):
            self.question.check_answer_to_question(QuestionAboutImportantPageLocators.ANSWER_COST_RENT, DataLayer.ANSWER_COST_RENT)

    @allure.title('Проверка ответа на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def test_answer_count_scooter(self):
        with allure.step('Кликаем на вопрос'):
            self.question.click_on_element(QuestionAboutImportantPageLocators.QUESTIONS_COUNT_SCOOTER)
        with allure.step('Проверяем ответ на вопрос'):
            self.question.check_answer_to_question(QuestionAboutImportantPageLocators.ANSWER_COUNT_SCOOTER, DataLayer.ANSWER_COUNT_SCOOTER)

    @allure.title('Проверка ответа на вопрос "Как рассчитывается время аренды?"')
    def test_answer_time_rent(self):
        with allure.step('Кликаем на вопрос'):
            self.question.click_on_element(QuestionAboutImportantPageLocators.QUESTIONS_TIME_RENT)
        with allure.step('Проверяем ответ на вопрос'):
            self.question.check_answer_to_question(QuestionAboutImportantPageLocators.ANSWER_TIME_RENT,DataLayer.ANSWER_TIME_RENT)

    @allure.title('Проверка ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def test_answer_today_rent(self):
        with allure.step('Кликаем на вопрос'):
            self.question.click_on_element(QuestionAboutImportantPageLocators.QUESTIONS_TODAY_RENT)
        with allure.step('Проверяем ответ на вопрос'):
            self.question.check_answer_to_question(QuestionAboutImportantPageLocators.ANSWER_TODAY_RENT,DataLayer.ANSWER_TODAY_RENT)

    @allure.title('Проверка ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_answer_extend_rent(self):
        with allure.step('Кликаем на вопрос'):
            self.question.click_on_element(QuestionAboutImportantPageLocators.QUESTIONS_EXTEND_RENT)
        with allure.step('Проверяем ответ на вопрос'):
            self.question.check_answer_to_question(QuestionAboutImportantPageLocators.ANSWER_EXTEND_RENT,DataLayer.ANSWER_EXTEND_RENT)

    @allure.title('Проверка ответа на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def test_answer_charge_scooter(self):
        with allure.step('Кликаем на вопрос'):
            self.question.click_on_element(QuestionAboutImportantPageLocators.QUESTIONS_CHARGE_SCOOTER)
        with allure.step('Проверяем ответ на вопрос'):
            self.question.check_answer_to_question(QuestionAboutImportantPageLocators.ANSWER_CHARGE_SCOOTER, DataLayer.ANSWER_CHARGE_SCOOTER)

    @allure.title('Проверка ответа на вопрос "Можно ли отменить заказ?"')
    def test_answer_cancel_rent(self):
        with allure.step('Кликаем на вопрос'):
            self.question.click_on_element(QuestionAboutImportantPageLocators.QUESTIONS_CANCEL_RENT)
        with allure.step('Проверяем ответ на вопрос'):
            self.question.check_answer_to_question(QuestionAboutImportantPageLocators.ANSWER_CANCEL_RENT,DataLayer.ANSWER_CANCEL_RENT)

    @allure.title('Проверка ответа на вопрос "Я жизу за МКАДом, привезёте?"')
    def test_answer_area_rent(self):
        with allure.step('Кликаем на вопрос'):
            self.question.click_on_element(QuestionAboutImportantPageLocators.QUESTIONS_AREA_RENT)
        with allure.step('Проверяем ответ на вопрос'):
            self.question.check_answer_to_question(QuestionAboutImportantPageLocators.ANSWER_AREA_RENT,DataLayer.ANSWER_AREA_RENT)

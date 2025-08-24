import pytest
import allure

from pages.questions_about_important_page import QuestionAboutImportantPage
from locators.question_about_important_page_lct import QuestionAboutImportantPageLocators
from data_layer.question_about_important_page_dl import DataLayer
from config import Url


@allure.suite('Яндекс Самокат. Блок "Вопросы о важном"')
class TestAnswersToImportantQuestions():

    @classmethod
    def setup_class(cls):
        cls.question = QuestionAboutImportantPage()

    @classmethod
    def teardown_class(cls):
        cls.question.quit()

    def setup_method(self):
        self.question.go_to(Url.MAIN_URL)
        self.question.confirm_cookies()

    @allure.title(f'Проверка ответа на вопроc')
    @pytest.mark.parametrize('question_title, question_locator, answer_locator, expected_text_answer',
        [
            ["Сколько это стоит? И как оплатить?",
             QuestionAboutImportantPageLocators.QUESTIONS_COST_RENT,
             QuestionAboutImportantPageLocators.ANSWER_COST_RENT,
             DataLayer.ANSWER_COST_RENT
             ],
            ["Хочу сразу несколько самокатов! Так можно??",
             QuestionAboutImportantPageLocators.QUESTIONS_COUNT_SCOOTER,
             QuestionAboutImportantPageLocators.ANSWER_COUNT_SCOOTER,
             DataLayer.ANSWER_COUNT_SCOOTER],
            ["Как рассчитывается время аренды?",
             QuestionAboutImportantPageLocators.QUESTIONS_TIME_RENT,
             QuestionAboutImportantPageLocators.ANSWER_TIME_RENT,
             DataLayer.ANSWER_TIME_RENT],
            ["Можно ли заказать самокат прямо на сегодня?",
             QuestionAboutImportantPageLocators.QUESTIONS_TODAY_RENT,
             QuestionAboutImportantPageLocators.ANSWER_TODAY_RENT,
             DataLayer.ANSWER_TODAY_RENT],
            ["Можно ли продлить заказ или вернуть самокат раньше?",
             QuestionAboutImportantPageLocators.QUESTIONS_EXTEND_RENT,
             QuestionAboutImportantPageLocators.ANSWER_EXTEND_RENT,
             DataLayer.ANSWER_EXTEND_RENT],
            ["Вы привозите зарядку вместе с самокатом?",
             QuestionAboutImportantPageLocators.QUESTIONS_CHARGE_SCOOTER,
             QuestionAboutImportantPageLocators.ANSWER_CHARGE_SCOOTER,
             DataLayer.ANSWER_CHARGE_SCOOTER],
            ["Можно ли отменить заказ?",
             QuestionAboutImportantPageLocators.QUESTIONS_CANCEL_RENT,
             QuestionAboutImportantPageLocators.ANSWER_CANCEL_RENT,
             DataLayer.ANSWER_CANCEL_RENT],
            ["Я жизу за МКАДом, привезёте?",
             QuestionAboutImportantPageLocators.QUESTIONS_AREA_RENT,
             QuestionAboutImportantPageLocators.ANSWER_AREA_RENT,
             DataLayer.ANSWER_AREA_RENT]
        ]
    )

    def test_answer_to_question(self, question_title, question_locator, answer_locator, expected_text_answer):
        with allure.step(f'Кликаем на вопрос "{question_title}"'):
            self.question.click_on_element(question_locator)
        with allure.step(f'Проверяем ответ на вопрос "{question_title}"'):
            self.question.check_answer_to_question(answer_locator, expected_text_answer)

from selenium import webdriver
import allure
import pytest

from data_layer.create_order_scooter_page_dl import DataLayer
from locators.base_lct import BaseLocators
from locators.create_order_page_lct import CreateOrderPageLocators
from config import Url
from pages.create_order_scooter_page import CreateOrderScooterPage


@allure.suite('Яндекс Самокат. "Оформление заказа"')
class TestCreateOrdersScooter():

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.create_order = CreateOrderScooterPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def setup_method(self):
        self.driver.get(Url.MAIN_URL)
        self.create_order.confirm_cookies(BaseLocators.CONFIRM_COOKIES)

    @allure.title(f'Проверка оформления заказа')
    @pytest.mark.parametrize(
        "test_id, order_button, metro_locator, user_name, user_surname, address, phone_number, date_rent, time_rent, color, comment",
        [
            ("в хедере", CreateOrderPageLocators.HEADER_ORDER_BUTTON, CreateOrderPageLocators.METRO_SOKOLNIKI, DataLayer.NAME_MALE,
             DataLayer.SURNAME_MALE, DataLayer.ADDRESS_SHORT, DataLayer.PHONE_WITH_8,
             CreateOrderPageLocators.DATE_SELECT_13_DAY, CreateOrderPageLocators.TIME_RENT_SELECT_2_DAY,
             CreateOrderPageLocators.COLOR_SELECT_BLACK, DataLayer.COMMENT_SMALL),
            ("в теле сайта", CreateOrderPageLocators.BODY_ORDER_BUTTON, CreateOrderPageLocators.METRO_CHERKIZOVSKAYA,
             DataLayer.NAME_FEMALE, DataLayer.SURNAME_FEMALE, DataLayer.ADDRESS_LONG, DataLayer.PHONE_WITH_PLUS,
             CreateOrderPageLocators.DATE_SELECT_29_DAY, CreateOrderPageLocators.TIME_RENT_SELECT_3_DAY,
             CreateOrderPageLocators.COLOR_SELECT_GREY, DataLayer.COMMENT_LONG,)
        ]
    )
    def test_create_order_scooter(self, test_id, order_button, metro_locator, user_name, user_surname, address, phone_number, date_rent, time_rent, color, comment):
        with allure.step(f'Кликаем по кнопке "Заказать" {test_id}'):
            self.create_order.click_on_element(order_button)
        with allure.step('Заполняем форму заказа "Для кого самокат"'):
            self.create_order.fill_personal_info(user_name, user_surname, address, phone_number, metro_locator)
        with allure.step('Кликаем по кнопке "Далее"'):
            self.create_order.click_on_element(CreateOrderPageLocators.NEXT_BUTTON)
        with allure.step('Заполняем форму заказа "Про аренду"'):
            self.create_order.fill_rent_info(date_rent, time_rent, color)
        with allure.step('Кликаем на кнопку подтверждения заказа "Да"'):
            self.create_order.click_on_element(CreateOrderPageLocators.CONFIRM_ORDER_BUTTON)
        with allure.step('Проверяем отображение модального окна "Заказ оформлен"'):
            self.create_order.check_success_order_modal(CreateOrderPageLocators.SUCCESS_ORDER_MODAL, DataLayer.TEXT_MODAL_SUCCESS_ORDER)
        with allure.step('Кликаем по кнопке "Посмотреть статус"'):
            self.create_order.click_on_element(CreateOrderPageLocators.CHECK_ORDER_STATUS)
        with allure.step('Проверяем переход на главную страницу, при клике по логотипу "Самокат" в хедере'):
            self.create_order.click_on_element(BaseLocators.LOGO_SCOOTER)
            self.create_order.check_current_url(Url.MAIN_URL)
        with allure.step('Кликаем на лого "Яндекс" в хедере и проверяем открытие страницы "Дзен" в новой вкладке'):
            self.create_order.check_url_new_window_page(BaseLocators.LOGO_YANDEX, Url.DZEN_URL)

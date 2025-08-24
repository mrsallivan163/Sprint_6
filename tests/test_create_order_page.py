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
        cls.create_order = CreateOrderScooterPage()

    @classmethod
    def teardown_class(cls):
        cls.create_order.quit()

    def setup_method(self):
        self.create_order.go_to(Url.MAIN_URL)
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
            self.create_order.click_button_next()
        with allure.step('Заполняем форму заказа "Про аренду"'):
            self.create_order.fill_rent_info(date_rent, time_rent, color, comment)
        with allure.step('Кликаем на кнопку подтверждения заказа "Да"'):
            self.create_order.click_comfirm_order_button()
        with allure.step('Проверяем отображение модального окна "Заказ оформлен"'):
            self.create_order.check_success_order_modal()
        with allure.step('Кликаем по кнопке "Посмотреть статус"'):
            self.create_order.click_button_status_order()
        with allure.step('Проверяем переход на главную страницу, при клике по логотипу "Самокат" в хедере'):
            self.create_order.click_on_logo_scooter()
            self.create_order.check_current_url_main_scooter()
        with allure.step('Кликаем на лого "Яндекс" в хедере и проверяем открытие страницы "Дзен" в новой вкладке'):
            self.create_order.check_current_url_new_window_is_dzen()

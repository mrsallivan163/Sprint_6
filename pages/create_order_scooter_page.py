from locators.create_order_page_lct import CreateOrderPageLocators
from locators.base_lct import BaseLocators
from pages.base_page import BasePage
from data_layer.create_order_scooter_page_dl import DataLayer
from config import Url


class CreateOrderScooterPage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)

    def check_success_order_modal(self):
        """Проверяем отображение модального окна на странице успещного 'оформления заказа и текста Заказ оформлен'"""
        self.check_element_displayed(CreateOrderPageLocators.SUCCESS_ORDER_MODAL)
        assert DataLayer.TEXT_MODAL_SUCCESS_ORDER in self.find_element_text(CreateOrderPageLocators.SUCCESS_ORDER_MODAL)

    def check_current_url_main_scooter(self):
        self.check_current_url(Url.MAIN_URL)

    def check_current_url_new_window_is_dzen(self):
        self.check_url_new_window_page(BaseLocators.LOGO_YANDEX, Url.DZEN_URL)

    def fill_personal_info(self, user_name, user_surname, address, phone_number, metro_locator):
        """Заполняем информация о пользователе"""
        self.enter_text(CreateOrderPageLocators.NAME_INPUT, user_name)
        self.enter_text(CreateOrderPageLocators.SURNAME_INPUT, user_surname)
        self.enter_text(CreateOrderPageLocators.ADDRESS_INPUT, address)
        self.enter_text(CreateOrderPageLocators.PHONE_INPUT, phone_number)
        self.click_on_element(CreateOrderPageLocators.METRO_INPUT)
        self.click_on_element(metro_locator)

    def fill_rent_info(self, date_rent, time_rent, color, comment):
        """Заполняем информацию об аренде"""
        self.click_on_element(CreateOrderPageLocators.DATE_INPUT)
        self.click_on_element(date_rent)
        self.click_on_element(CreateOrderPageLocators.TIME_RENT_INPUT)
        self.click_on_element(time_rent)
        self.click_on_element(color)
        self.enter_text(CreateOrderPageLocators.COMMENT, comment)
        self.click_on_element(CreateOrderPageLocators.FORM_ORDER_BUTTON)

    def click_button_next(self):
        """Кликаем по кнопке 'Далее'"""
        self.click_on_element(CreateOrderPageLocators.NEXT_BUTTON)

    def click_comfirm_order_button(self):
        """Кликаем по кнопке 'Да'"""
        self.click_on_element(CreateOrderPageLocators.CONFIRM_ORDER_BUTTON)

    def click_button_status_order(self):
        """Кликаем по кнопке 'Посмотреть статус'"""
        self.click_on_element(CreateOrderPageLocators.CHECK_ORDER_STATUS)

    def click_on_logo_scooter(self):
        """Кликаем по логтипу 'Самокат''"""
        self.click_on_element(BaseLocators.LOGO_SCOOTER)
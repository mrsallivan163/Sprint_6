from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from locators.create_order_page_lct import CreateOrderPageLocators
from pages.base_page import BasePage


class CreateOrderScooterPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 5)

    def check_success_order_modal(self, locator, text):
        """Проверяем отображение модального окна на странице успещного 'оформления заказа и текста Заказ оформлен'"""
        self.check_element_displayed(locator)
        assert text in self.driver.find_element(*locator).text

    def fill_personal_info(self, user_name, user_surname, address, phone_number, metro_locator):
        """Заполняем информация о пользователе"""
        self.enter_text(CreateOrderPageLocators.NAME_INPUT, user_name)
        self.enter_text(CreateOrderPageLocators.SURNAME_INPUT, user_surname)
        self.enter_text(CreateOrderPageLocators.ADDRESS_INPUT, address)
        self.enter_text(CreateOrderPageLocators.PHONE_INPUT, phone_number)
        self.click_on_element(CreateOrderPageLocators.METRO_INPUT)
        self.click_on_element(metro_locator)

    def fill_rent_info(self, date_rent, time_rent, color):
        """Заполняем информацию об аренде"""
        self.click_on_element(CreateOrderPageLocators.DATE_INPUT)
        self.click_on_element(date_rent)
        self.click_on_element(CreateOrderPageLocators.TIME_RENT_INPUT)
        self.click_on_element(time_rent)
        self.click_on_element(color)
        self.enter_text(CreateOrderPageLocators.COMMENT, color)
        self.click_on_element(CreateOrderPageLocators.FORM_ORDER_BUTTON)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_lct import BaseLocators
from selenium import webdriver

class BasePage():

    def __init__(self, driver=None):
        if driver is None:
            self.driver = webdriver.Firefox()
        else:
            self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def find_element(self, locator):
        """Находим элемент по локатору"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_element_text(self, locator):
        """Возвращаем текст элемента"""
        element = self.find_element(locator)
        return element.text

    def enter_text(self, locator, text):
        """Ввод текст в поле ввода"""
        self.driver.find_element(*locator).send_keys(text)

    def click_on_element(self, locator):
        """Кликаем по элементу на странице"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def check_text_matches(self, locator, text):
        """Проверяем полное совпадение двух текстов между собой"""
        self.wait.until(EC.visibility_of_element_located(locator))
        assert self.driver.find_element(
            *locator).text == text, f'ОЖИДАЛСЯ: "{text}", ПОЛУЧЕН: "{self.driver.find_element(*locator).text}"'

    def check_element_displayed(self, locator):
        """Проверяем что элемент отображается на странице"""
        assert self.driver.find_element(*locator).is_displayed()

    def check_current_url(self, url):
        """Cравниваем текущий URL с ожидаемым"""
        assert self.driver.current_url == url

    def check_url_new_window_page(self, locator, url):
        """Проверяем url в новой вкладке браузера"""
        original_window = self.driver.current_window_handle
        self.driver.find_element(*locator).click()
        self.wait.until(EC.number_of_windows_to_be(2))
        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break
        assert self.wait.until(
            EC.url_to_be(url)), f"Текущий url: {self.driver.current_url} не совпадает с ожидаемым"
        self.driver.close()
        self.driver.switch_to.window(original_window)

    def confirm_cookies(self):
        """Закрываем баннер с Cookies, если он есть"""
        try:
            button = self.driver.find_element(*BaseLocators.CONFIRM_COOKIES)
            if button.is_displayed() and button.is_enabled():
                button.click()
        except:
            pass

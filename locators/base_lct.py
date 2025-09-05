from selenium.webdriver.common.by import By

class BaseLocators():
    CONFIRM_COOKIES = (By.ID, 'rcc-confirm-button')
    LOGO_SCOOTER = (By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")
    LOGO_YANDEX = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")
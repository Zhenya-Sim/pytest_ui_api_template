import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configuration.ConfigProvider import ConfigProvider


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.url = ConfigProvider().get("ui", "base_url")
        self.__url = self.url + "/u/user97567633/boards"
        self.__driver = driver

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("Открыть боковое меню")
    def open_menu(self):
        self.__driver.find_element(
            By.CSS_SELECTOR,
            '[data-testid="header-member-menu-avatar"]').click()

    @allure.step("Получить имя и email пользователя")
    def get_account_info(self) -> list[str]:
        (WebDriverWait(self.__driver, 10).
         until(
             EC.visibility_of_element_located((By.CSS_SELECTOR,
                                               'div[data-testid="account-menu-account-section"]'))))
        container = self.__driver.find_element(
            By.CSS_SELECTOR,
            'div[data-testid="account-menu-account-section"]>div>div:last-child')
        fields = container.find_elements(By.CSS_SELECTOR, "div")
        names = fields[0].text
        email = fields[1].text

        return [names, email]

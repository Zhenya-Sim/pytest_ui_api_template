import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from api.BoardApi import BoardApi
from configuration.ConfigProvider import ConfigProvider


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):

        timeout = ConfigProvider().get_int("ui", "timeout")

        browser_name = ConfigProvider().get("ui", "browser_name")

        if browser_name == 'chrome':
            browser = webdriver.Chrome()
        else:
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def api_client() -> BoardApi:
    url = ConfigProvider().get("api", "base_url")
    return BoardApi(url, "token", "api_key")


# фикстура для неавторизованного пользователя
# не используя промежуточную переменную из примера выше
@pytest.fixture
def api_client_no_auth() -> BoardApi:
    return BoardApi(ConfigProvider().get("api", "base_url"), "", "")


# фикстура для создания доски, которую точно удалят
@pytest.fixture
def creat_del_board() -> BoardApi:
    api = BoardApi("https://api.trello.com/1", "token", "api_key")
    resp = api.create_board("Board to be deleted").get("id")
    return resp


# фикстура для удаления только что созданной доски
@pytest.fixture
def delete_board():
    dictionary = {"board_id": ""}
    yield dictionary

    api = BoardApi("https://api.trello.com/1", "token", "api_key")
    api.delete_board_by_id(dictionary.get("board_id"))

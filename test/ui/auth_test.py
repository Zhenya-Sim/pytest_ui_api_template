import allure
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
import pytest


@pytest.mark.skip
def test_auth(browser):
    email = "simonova.evd21597@gmail.com"
    password = "Qw210597fox"
    username = "Евгения"

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    # Проверка, что URL заканчивается заданной подстрокой
    current_url = main_page.get_current_url()
    with allure.step("Проверить, что URL " + current_url +
                     "заканчивается на user97567633/boards"):
        assert current_url.endswith("user97567633/boards")

    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Проверить, что имя пользователя " + username):
            assert info[0] == username
        with allure.step("Проверить, что email пользователя " + email):
            assert info[1] == email

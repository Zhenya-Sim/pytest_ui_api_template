from pages.AuthPage import AuthPage
from pages.MainPage import MainPage


def test_auth(browser):
    email = "simonova.evd21597@gmail.com"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, "Qw210597fox")

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    # Проверка, что URL заканчивается заданной подстрокой
    assert main_page.get_current_url().endswith("user97567633/boards")
    assert info[0] == "Евгения"
    assert info[1] == email

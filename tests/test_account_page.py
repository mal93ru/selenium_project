import pytest
import allure


@allure.feature('Учетная запись пользователя')
@allure.story('Содержимое на странице аутентификации пользователя')
@allure.title('Отображение элементов страницы')
@pytest.mark.parametrize('path', ['login'])
def test_login_page_elements(account_page):
    account_page.should_be_login_elements()


@allure.feature('Учетная запись пользователя')
@allure.story('Регистрация пользователя')
@allure.title('Успешная регистрация пользователя и создание новой УЗ')
# TODO: Для данного теста необходимо реализовать фикстуру предварительного удаления учетной записи с данными параметрами
@pytest.mark.parametrize('path', ['register'])
def test_register_form(account_page):
    with allure.step('Ввод имени'):
        account_page.input_reg_first_name()
    with allure.step('Ввод фамилии'):
        account_page.input_reg_last_name()
    with allure.step('Ввод электронной почты'):
        account_page.input_reg_email()
    with allure.step('Ввод номера телефона'):
        account_page.input_reg_telephone()
    with allure.step('Ввод пароля'):
        account_page.input_reg_pass()
    with allure.step('Повторный ввод пароля'):
        account_page.input_reg_pass_confirm()
    with allure.step('Подтверждение политик'):
        account_page.accept_reg_policy()
    with allure.step('Отправка формы'):
        account_page.accept_reg_form()
    with allure.step('Ожидание страницы успешного создания УЗ'):
        account_page.new_account_created()

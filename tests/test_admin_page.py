import allure


@allure.feature('Раздел администрирования')
@allure.story('Содержимое в разделе администратора')
@allure.title('Проверка заголовка страницы')
def test_title(admin_page):
    admin_page.should_be_login_elements()


@allure.feature('Раздел администрирования')
@allure.story('Аутентификация')
@allure.title('Аутентификация и выход из учетной записи')
def test_login_logout(admin_page):
    admin_page.login_successful()
    admin_page.logout()


@allure.feature('Раздел администрирования')
@allure.story('Содержимое в разделе администратора')
@allure.title('Отображение таблицы с товарами')
def test_product_list(admin_page, admin_login):
    with allure.step('Переход к администрированию Catalog » Products'):
        admin_page.open_menu_products()
    with allure.step('Поиск таблицы с товарами'):
        admin_page.check_product_list()


@allure.feature('Раздел администрирования')
@allure.story('Содержимое в разделе администратора')
@allure.title('Отображение фильтров поиска')
def test_filter(admin_page, admin_login):
    with allure.step('Переход к администрированию Catalog » Products'):
        admin_page.open_menu_products()
    with allure.step('Поиск фильтров поиска'):
        admin_page.check_panel_filter()

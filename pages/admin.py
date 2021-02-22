import allure
from selenium.webdriver.common.by import By
from .base import BasePage


class AdminPage(BasePage):
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    FORGOTTEN_PASS_LINK = (By.CSS_SELECTOR, "[href=\'https://demo.opencart.com/admin/index.php?route=common/forgotten']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")
    HEADER_LOGO = (By.CSS_SELECTOR, ".navbar-brand")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".fa.fa-sign-out")
    MENU_CATALOG = (By.ID, "menu-catalog")
    MENU_PRODUCTS = (By.CSS_SELECTOR, "#collapse1 li:nth-child(2)")
    PRODUCT_LIST = (By.CSS_SELECTOR, "#content div.container-fluid div div.col-md-9.col-md-pull-3.col-sm-12 div")
    PANEL_FILTER = (By.CSS_SELECTOR, ".panel.panel-default")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def should_be_login_elements(self):
        with allure.step('Поиск поля ввода имени'):
            self.find_element(locator=self.USERNAME_INPUT)
        with allure.step('Поиск поля ввода пароля'):
            self.find_element(locator=self.PASSWORD_INPUT)
        with allure.step('Поиск гиперрсылки на страницу восстановления пароля'):
            self.find_element(locator=self.FORGOTTEN_PASS_LINK)
        with allure.step('Поиск кнопки аутентификации'):
            self.find_element(locator=self.LOGIN_BUTTON)
        with allure.step('Поиск лого в хэдере'):
            self.find_element(locator=self.HEADER_LOGO)

    def login_successful(self):
        with allure.step('Ввод имени'):
            self.find_element(locator=self.USERNAME_INPUT).clear()
            self.find_element(locator=self.USERNAME_INPUT).send_keys('demo')
        with allure.step('Ввод пароля'):
            self.find_element(locator=self.PASSWORD_INPUT).clear()
            self.find_element(locator=self.PASSWORD_INPUT).send_keys('demo')
        with allure.step('Подтверждение'):
            self.find_element(locator=self.PASSWORD_INPUT).submit()
        with allure.step('Ожидание заголовка «Dashboard»'):
            self.wait_for_title('Dashboard')

    def logout(self):
        with allure.step('Выход из учетной записи администратора'):
            self.find_element(locator=self.LOGOUT_BUTTON).click()
        with allure.step('Ожидание заголовка «Administration»'):
            self.wait_for_title('Administration')

    def open_menu_products(self):
        with allure.step('Раскрытие выпадающего списка с навигацией по разделам администрирования каталога'):
            self.find_element(locator=self.MENU_CATALOG).click()
            self.wait_for_element_clickable(locator=self.MENU_PRODUCTS)
        with allure.step('Переход к разделу администрирования «Products»'):
            self.find_element(locator=self.MENU_PRODUCTS).click()

    def check_product_list(self):
        self.wait_for_element_clickable(locator=self.PRODUCT_LIST)
        self.find_element(locator=self.PRODUCT_LIST)

    def check_panel_filter(self):
        self.wait_for_element_clickable(locator=self.PANEL_FILTER)
        self.find_element(locator=self.PANEL_FILTER)

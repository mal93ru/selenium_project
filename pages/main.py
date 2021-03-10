from selenium.webdriver.common.by import By
from .base import BasePage
import allure


class MainPage(BasePage):
    HEADER_TABLETS = (By.LINK_TEXT, "Tablets")
    HEADER_SOFTWARE = (By.LINK_TEXT, "Software")
    HEADER_PHONES = (By.LINK_TEXT, "Phones & PDAs")
    HEADER_CAMERAS = (By.LINK_TEXT, "Cameras")
    HEADER_DESKTOPS = (By.LINK_TEXT, "Desktops")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn.btn-default.btn-lg")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def should_be_header_elements(self):
        with allure.step('Поиск в хэдере элемента Tablets'):
            self.find_element(locator=self.HEADER_TABLETS)
        with allure.step('Поиск в хэдере элемента Software'):
            self.find_element(locator=self.HEADER_SOFTWARE)
        with allure.step('Поиск в хэдере элемента Phones'):
            self.find_element(locator=self.HEADER_PHONES)
        with allure.step('Поиск в хэдере элемента Cameras'):
            self.find_element(locator=self.HEADER_CAMERAS)
        with allure.step('Поиск в хэдере элемента Desktops'):
            self.find_element(locator=self.HEADER_DESKTOPS)

    def search(self, value):
        with allure.step(f'Ввод «{value}» в строку поиска'):
            self.find_element(locator=self.SEARCH_INPUT).send_keys(value)
        with allure.step('Клик по кнопке Search'):
            self.find_element(locator=self.SEARCH_BUTTON).click()

    def title_is(self, expected_title):
        with allure.step(f'Заголовок соответствует «{expected_title}»'):
            self.wait_for_title(expected_title)

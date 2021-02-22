import logging
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = "https://demo.opencart.com/"
        self.logger = logging.getLogger(type(self).__name__)

    def find_element(self, locator, timeout=10):
        with allure.step(f'Поиск элемента «{locator}»'):
            self.logger.info("Finding element: «{}»".format(locator))
            try:
                return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            except TimeoutException:
                raise AssertionError(f"Can't find elements by locator {locator}")

    def find_elements(self, locator, timeout=10):
        with allure.step(f'Поиск элементов «{locator}»'):
            self.logger.info("Finding elements: «{}»".format(locator))
            return WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator),
                                                           message=f"Can't find elements by locator {locator}")

    def go_to(self, url):
        with allure.step(f'Переход к странице «{url}»'):
            self.logger.info("Go to url: «{}»".format(url))
            return self.browser.get(f"{self.base_url}{url}")

    def wait_for_title(self, expected_title, timeout=10):
        with allure.step(f'Ожидание страницы «{expected_title}»'):
            self.logger.info("Wait for title: «{}»".format(expected_title))
            try:
                return WebDriverWait(self.browser, timeout).until(EC.title_is(expected_title))
            except TimeoutException:
                actual_title = self.browser.title
                raise AssertionError(f"Title is \"{actual_title}\"")

    def wait_for_element_clickable(self, locator, timeout=3):
        with allure.step(f'Ожидание интерактивности элемента «{locator}»'):
            self.logger.info("Wait for element «{}» clickable".format(locator))
            try:
                return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((locator)))
            except TimeoutException:
                raise AssertionError(f"Element {locator} not interactable")

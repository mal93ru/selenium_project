import allure
from selenium.webdriver.common.by import By
from .base import BasePage


class CatalogPage(BasePage):
    IPHONE_PHOTO = (By.CSS_SELECTOR, "[alt='iPhone']")
    IPHONE_PRICE = (By.CSS_SELECTOR, "div:nth-child(5) p.price")
    IPHONE_ADD_CART = (By.CSS_SELECTOR, "div:nth-child(5) div div:nth-child(2) button:nth-child(1)")
    IPHONE_ADD_WISHLIST = (By.CSS_SELECTOR, "div:nth-child(5) div div:nth-child(2) button:nth-child(2)")
    IPHONE_COMPARE = (By.CSS_SELECTOR, "div:nth-child(5) div div:nth-child(2) button:nth-child(3)")

    PRODUCT_DESCRIPTION = (By.ID, "tab-description")
    PRODUCT_ADD_CART = (By.ID, "button-cart")
    CART_BUTTON = (By.ID, "cart")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content div div.col-sm-4 h1")
    PRICE_VALUE = (By.CSS_SELECTOR, "#content div div.col-sm-4 ul:nth-child(4) li:nth-child(1) h2")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def should_be_catalog_elements(self):
        with allure.step('Проверка фото товара'):
            self.find_element(locator=self.IPHONE_PHOTO)
        with allure.step('Поиск параметра стоимости'):
            self.find_element(locator=self.IPHONE_PRICE)
        with allure.step('Поиск кнопки добавления в корзину'):
            self.find_element(locator=self.IPHONE_ADD_CART)
        with allure.step('Поиск кнопки добавления в список желаемого'):
            self.find_element(locator=self.IPHONE_ADD_WISHLIST)
        with allure.step('Поиск кнопки режима сравнения'):
            self.find_element(locator=self.IPHONE_COMPARE)

    def should_be_product_card_elements(self):
        with allure.step('Поиск описания продукта'):
            self.find_element(locator=self.PRODUCT_DESCRIPTION)
        with allure.step('Поиск кнопки «Add to Cart»'):
            self.find_element(locator=self.PRODUCT_ADD_CART)
        with allure.step('Поиск кнопки перехода к корзине'):
            self.find_element(locator=self.CART_BUTTON)
        with allure.step('Поиск названия продукта'):
            self.find_element(locator=self.PRODUCT_NAME)
        with allure.step('Поиск кнопки «Add to Cart»'):
            self.find_element(locator=self.PRICE_VALUE)

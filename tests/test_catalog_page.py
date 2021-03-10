import pytest
import allure


@allure.feature('Отображение содержимого на страницах')
@allure.story('Содержимое в каталоге')
@allure.title('Проверка элементов в каталоге')
@pytest.mark.parametrize('path', ['category&path=20'])
def test_catalog_page(catalog_page):
    catalog_page.should_be_catalog_elements()


@allure.feature('Отображение содержимого на страницах')
@allure.story('Содержимое в каталоге')
@allure.title('Проверка элементов в карточке товара')
@pytest.mark.parametrize('path', ['product&path=57&product_id=49'])
def test_product_card_page(catalog_page):
    catalog_page.should_be_product_card_elements()

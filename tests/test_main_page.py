import pytest
import allure


@allure.feature('Отображение содержимого на страницах')
@allure.story('Содержимое на главной странице')
@allure.title('Проверка заголовка страницы')
def test_title(main_page):
    assert main_page.driver.title == 'Your Store'


@allure.feature('Отображение содержимого на страницах')
@allure.story('Содержимое на главной странице')
@allure.title('Проверка элементов навигации в хэдере')
def test_main_page(main_page):
    main_page.should_be_header_elements()


@allure.feature('Отображение содержимого на страницах')
@allure.story('Запрос в поисковой строке')
@allure.title('Поиск {search_input}')
@pytest.mark.parametrize('search_input, expected_title', [('iPhone', 'Search - iPhone'),
                                                          ('MacBook', 'Search - MacBook'),
                                                          ('Canon', 'Search - Canon')])
def test_main_search(main_page, search_input, expected_title):
    with allure.step('Поиск'):
        main_page.search(search_input)
    with allure.step('Проверка соответствия заголовка страницы запросу'):
        main_page.title_is(expected_title)

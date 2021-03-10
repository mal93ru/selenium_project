import pytest
import allure
import os
import logging
from selenium import webdriver
from pages.main import MainPage
from pages.catalog import CatalogPage
from pages.account import LoginPage
from pages.admin import AdminPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


logging.basicConfig(filename="selenium.log",
                    format='%(asctime)s:%(levelname)s:%(name)s - %(message)s',
                    encoding='utf-8',
                    datefmt='%m/%d/%Y %I:%M:%S',
                    level=logging.INFO
                    )


class Listener(AbstractEventListener):
    logger = logging.getLogger('ListenerLoger')

    def before_navigate_to(self, url, driver):
        self.logger.info(f"Navigating to «{url}»")

    def after_navigate_to(self, url, driver):
        self.logger.info(f"On «{url}»")

    def before_navigate_back(self, driver):
        self.logger.info(f"Navigating back")

    def after_navigate_back(self, driver):
        self.logger.info(f"Back!")

    def before_find(self, by, value, driver):
        self.logger.info(f"Looking for «{value}» with «{by}»")

    def after_find(self, by, value, driver):
        self.logger.info(f"Found «{value}» with «{by}»")

    def before_click(self, element, driver):
        self.logger.info(f"Clicking «{element}»")

    def after_click(self, element, driver):
        self.logger.info(f"Clicked «{element}»")

    def before_execute_script(self, script, driver):
        self.logger.info(f"Executing '{script}'")

    def after_execute_script(self, script, driver):
        self.logger.info(f"Executed «{script}»")

    def before_quit(self, driver):
        self.logger.info(f"Getting ready to terminate «{driver}»")

    def after_quit(self, driver):
        self.logger.info(f"The session has ended")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--bversion", action="store", required=True)
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--mobile", action="store_true")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    version = request.config.getoption("--bversion")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    executor_url = f"http://{executor}:4444/wd/hub"
    mobile = request.config.getoption("--mobile")
    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name

    caps = {
        "browserName": browser,
        "browserVersion": version,
        "screenResolution": "1280x720",
        "name": "Malkov",
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": videos,
            "enableLog": logs,
        },
    }

    if browser == "chrome" and mobile:
        caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}

    wd = EventFiringWebDriver(webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=caps
    ), Listener())

    logger.info("Test {} started with {} {}".format(test_name, browser, version))

    def fin():
        wd.quit()
        logger.info("Browser {} closed".format(browser))
        logger.info("Test {} finished".format(test_name))

    request.addfinalizer(fin)
    return wd


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


@pytest.fixture()
def main_page(browser):
    with allure.step('Переход к главной странице сайта'):
        page = MainPage(browser)
        page.go_to('/')
        return page


@pytest.fixture()
def catalog_page(browser, path):
    with allure.step('Переход к каталогу'):
        page = CatalogPage(browser)
        page.go_to(f'/index.php?route=product/{path}')
        return page


@pytest.fixture()
def account_page(browser, path):
    with allure.step('Переход к странице аккаунта'):
        page = LoginPage(browser)
        page.go_to(f'/index.php?route=account/{path}')
        return page


@pytest.fixture()
def admin_page(browser):
    with allure.step('Переход в раздел администрирования'):
        page = AdminPage(browser)
        page.go_to(f'/admin/')
        return page


@pytest.fixture(scope="function")
def admin_login(browser, admin_page):
    with allure.step('Аутентификация на странице администрирования'):
        page = AdminPage(browser)
        with allure.step('Переход в раздел администрирования'):
            page.go_to(f'/admin/')
        with allure.step('Ввод пароля и подтверждение'):
            browser.find_element(By.ID, "input-password").submit()
        with allure.step('Ожидания заголовка «Dashboard»'):
            WebDriverWait(browser, 5).until(EC.title_is('Dashboard'))
        return True

import time
from datetime import datetime

import pytest
from pytest_bdd import given
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from testCases import test_Login

driver = None


@pytest.fixture()
def setup():
    global driver
    print("Initializing the driver....")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    yield driver
    print("Closing the browser")
    driver.close()

    # @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    # def pytest_runtest_makereport(item, call):
    #     outcome = yield
    #     rep = outcome.get_result()
    #     print(rep)
    #     print(f"\n{rep}")
    #     if rep.when == "call":
    #         print(f'{rep.outcome}')
    #     if rep.when == 'call' and rep.failed:
    #         now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #         driver.save_screenshot(f"C:\\Users\\Sures\\PycharmProjects\\nopCommerce\\Screenshots\\fail_{now}.png")


@given("User is valid")
def test_browser(setup):
    setup.get("https://admin-demo.nopcommerce.com/")

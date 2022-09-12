import os
import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.BaseClass import BaseClass

driver = None


def pytest_addoption(parser):  # get the data from the CLI
    # -B will let the user provide browser name from command-line
    # For E.g. C:\users\..\...\..>pytest -B chrome
    # action = "store", action = "append"

    parser.addoption("-B", "--browser",
                     dest="browser",
                     action="store",
                     default="edge",
                     help="Browser. Valid options are firefox, ie and chrome")


# ------- Come back here to tackle cross-browser testing --------
# def pytest_generate_tests(metafunc):
#     "test generator function to run tests across different parameters"
#     if "browser" in metafunc.fixturenames:
#         print("MetaBrowser", metafunc.config.option.browser)
#         metafunc.parameterize("browser", metafunc.config.option.browser)


@pytest.fixture()
def setup(request):
    global driver
    print("Initializing the driver....")
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif browser_name == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.instance.driver = driver

    yield driver
    print("Closing the browser")
    driver.close()


def pytest_configure(config):
    config._metadata['Project Name'] = 'nopCommerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Suresh G'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Plugins', None)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # Disabled coz of below added code
        # feature_request = item.funcargs['request']
        #
        # driver = feature_request.getfixturevalue('setup')
        # driver.save_screenshot(r'C:\Users\Sures\PycharmProjects\nopCommerce\Screenshots\scr'+timestamp+'.png')
        # extra.append(pytest_html.extras.image(r'C:\Users\Sures\PycharmProjects\nopCommerce\Screenshots\scr'+timestamp+'.png'))
        # Disabled coz of below added code

        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):

            file_name_with_dir = report.nodeid.replace("::", "_") + "_" + timestamp + ".png"
            file_name_split_list = file_name_with_dir.split('/')
            file_name_only = file_name_split_list[1]
            file_name_with_path = rf"./Screenshots/fail_{file_name_only}"
            URL = BaseClass.setRootDir() + rf"\Screenshots\fail_{file_name_only}"
            _capture_screenshot(file_name_with_path)
            if file_name_with_path:
                html = '<div><img src= "%s" alt="screenshot" ' \
                       'style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name_with_path
                extra.append(pytest_html.extras.html(html))
            # only add additional html on failure
            # extra.append(pytest_html.extras.image('D:/report/scr.png'))
            # extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        # always add url to report
        extra.append(pytest_html.extras.url("https://google.com"))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

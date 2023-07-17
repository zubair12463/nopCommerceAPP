from selenium import webdriver
import pytest
import logging
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# # *************** Generate Reports *****************
def pytest_configure(config):
    config._metadata = {
                "Project Name": "nop Commerce",
                "Module Name": "Customers",
                "Tester": "Zubair"
            }
@pytest.mark.optionalhook 
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


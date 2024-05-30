import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# setup browser
@pytest.fixture(scope="function")
def init_driver(request) :
    options = Options()
    options.add_argument("start-maximized")
    web_driver = webdriver.Chrome(options=options)
    request.cls.driver = web_driver
    yield
    web_driver.close()

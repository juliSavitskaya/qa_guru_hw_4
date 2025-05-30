import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def browser():
    options = Options()
   #options.add_argument('--headless')
    options.add_argument('--window-size=1280,760')

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

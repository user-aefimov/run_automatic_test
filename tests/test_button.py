# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import pytest


# @pytest.fixture()
# def browser():
#     options = Options()
#     options.add_argument('--headless')
#     chrome_browser = webdriver.Chrome(options=options)
#     return chrome_browser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    
    # Автоматическое скачивание и использование правильного ChromeDriver
    service = Service(ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(service=service, options=options)
    
    yield chrome_browser
    chrome_browser.quit()



def test_button_exist(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()


def test_button_exist_2(browser):
    browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    assert browser.find_element(By.PARTIAL_LINK_TEXT, 'Click').is_displayed()


def test_me():
    assert 1 == 1

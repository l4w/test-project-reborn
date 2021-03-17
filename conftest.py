from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import time 
import pytest

def pytest_addoption(parser):
    parser.addoption(
        '--lang', action='store', default='en', help='Set the language of the website'
    )
    
@pytest.fixture
def browser(request):
    print('\nOpening Chrome...')
    language = request.config.getoption('--lang')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    print('\nClosing the browser...')
    time.sleep(2)
    browser.quit()

    

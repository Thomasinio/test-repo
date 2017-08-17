import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def app(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    request.addfinalizer(driver.quit())

def test_get(app):
    driver.get('https://google.com')
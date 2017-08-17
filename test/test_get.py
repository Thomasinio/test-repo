from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def test_get(app):
    app.driver.get('https://google.com')
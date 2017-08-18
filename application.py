from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def destroy(self):
        self.driver.quit()

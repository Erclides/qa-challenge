from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Browser:
    def __init__(self, headless=True):
        """
        Inicializa o WebDriver Chrome com opções headless ou visível.
        """
        options = Options()
        options.headless = headless
        self.driver = webdriver.Chrome(options=options)

    def quit(self):
        self.driver.quit()

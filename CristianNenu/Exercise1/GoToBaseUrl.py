from selenium import webdriver

from Excercise1.Platform_Contants import Platform


class GoToUrl:

    def setUp(self, url, platform):
        if platform == Platform.CHROME:
            self.web_browser = webdriver.Chrome()
        if platform == Platform.FIREFOX:
            self.web_browser = webdriver.Firefox()
        self.web_browser.get("http://wwww." + url)
        self.web_browser.maximize_window()
        self.addCleanup(self.web_browser.quit)

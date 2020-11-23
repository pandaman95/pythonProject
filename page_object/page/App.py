from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage
from page_object.page.MainPage import MainPage


class App(BasePage):
    @classmethod
    def main(cls):
        # cls.driver=BasePage.driver
        cls.getClient().restartApp()
        return MainPage()
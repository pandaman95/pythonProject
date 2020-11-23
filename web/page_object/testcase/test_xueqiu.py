from time import sleep

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from web.page_object.page.MainPage import MainPage
from web.page_object.page.ProfilePage import ProfilePage
from web.page_object.testcase.BaseTestCase import BaseTestCase


class TestXueqiu(BaseTestCase):

    def setup(self):
        # self.driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        self.driver = webdriver.Chrome(r'E:\webdrivers\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.get("https://xueqiu.com/")
        self.main=MainPage(self.driver)


    def test_search(self):
        self.main.search("alibaba").follow("9988")
        #todo:add assertion

    def test_profile(self):
        profile=ProfilePage(self.driver)
        profile.login()
        selected=profile.gotoSelected()
        # self.driver.get("https://xueqiu.com/setting/user")
        selected.selected("alibaba","9988")

    def test_log(self):

        self.log.warning("warning demo")
        self.log.debug("debug demo")
    def teardown(self):
        sleep(1)
        self.driver.quit()

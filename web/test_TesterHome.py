import json
from selenium import webdriver
import time

class TestTesterHome(object):
    def setup(self):
        # self.driver=webdriver.chrome()
        self.driver=webdriver.Chrome(r'E:\webdrivers\chromedriver.exe')
        # webdriver.Remote()
        self.driver.implicitly_wait(10)
        self.driver.get("https://testerhome.com")

    def test_mtsc2019(self):
        self.driver.find_element_by_partial_link_text("MTSC2020 中国互联网测试开发大会 所有议题放出！总有你兴趣的议题！").click()
        self.driver.find_element_by_xpath('//*[@data-toggle="dropdown" and @class="btn btn-default"]').click()
        self.driver.find_element_by_partial_link_text("大会合作伙伴").click()
        self.driver.find_element_by_partial_link_text("知识产权保护协议").click()

    def test_basic(self):
        self.driver.maximize_window()

    def test_execute_script(self):
        raw=self.driver.execute_script("return JSON.stringify(window.performance.timing)")
        print(raw)
        print(json.dumps(json.loads(raw),indent=4))

    def teardown(self):
        time.sleep(5)
        self.driver.quit()
        self.driver.add_cookie()
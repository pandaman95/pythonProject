from selenium import webdriver

class TestTesterHome(object):
    def setup(self):
        self.driver=webdriver.chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://testerhome.com")

    #def test_mtsc2019(self):
        #self.driver.find_element_by_id()
        #self.driver
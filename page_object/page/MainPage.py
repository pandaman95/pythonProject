from selenium.webdriver.common.by import By

from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage
from page_object.page.ProfilePage import ProfilePage
from page_object.page.SearchPage import SearchPage
from page_object.page.SelectedPage import SelectedPage


class MainPage(BasePage):
    _profile_button=(By.ID,"post_status")
    _search_button=(By.ID,"home_search")
    # #调用appium启动app
    # def __init__(self):
    #     AndroidClient.restartApp()


    def gotoSelected(self):
        #调用全局的driver对象使用webdriver api操作app
        # self.driver.find_element(By.xpath,"//*[@text='行情']")
        zixuan="自选"
        self.findByText(zixuan)
        # self.driver.find_element_by_xpath("//*[@text='行情']")
        self.findByText(zixuan).click()
        # self.driver.find_element_by_xpath("//*[@text='行情']").click()
        return SelectedPage()

    def gotoSearch(self)->SearchPage:

        self.find(self._search_button).click()
        return SearchPage()

    def gotoProfile(self):
        # self.find(MainPage._profile_button).click()
        self.loadSteps("../data/MainPage.yaml","gotoProfile")
        return ProfilePage()
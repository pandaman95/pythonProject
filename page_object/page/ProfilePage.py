from page_object.page.BasePage import BasePage
from page_object.page.LoginPage import LoginPage


class ProfilePage(BasePage):
    def gotoLogin(self):
        # self.findByText("手机及其他登录").click()
        self.loadSteps("../data/ProfilePage.yaml","gotoLogin")
        return LoginPage()
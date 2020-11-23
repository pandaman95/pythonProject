from page_object.page.App import App
import pytest

class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.profilePage= App.main().gotoProfile()

    def setup_method(self):
        self.loginPage=self.profilePage.gotoLogin()
        exit()
    @pytest.mark.parametrize("user,pw,msg",[("1234567","1111111","手机号码"),("1234567000","1111111","密码错误")])
    def test_login_password(self,user,pw,msg):
        self.loginPage.loginByPassword(user,pw)
        assert msg in self.loginPage.getErrorMsg()


    def tearDown_method(self):
        self.loginPage.back()
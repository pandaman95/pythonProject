from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidClient(object):
    driver:WebDriver=""
    @classmethod
    def installApp(cls)->WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "test"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"]="true"
        # caps["noReset"] = True
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(20)
        return cls.driver

    @classmethod
    def restartApp(cls)->WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "test"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        caps["unicodeKeyboard"]=True
        caps["resetKeyboard"]=True
        # caps["noReset"] = True
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(20)
        return cls.driver
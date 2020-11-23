# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiuAndroid(object):

    driver=WebDriver
    @classmethod
    def setup_class(cls):
        print("setup class")
        #cls.driver=cls.init_appium()
        cls.driver=cls.restart_appium()
        cls.driver.find_element_by_xpath("//android.widget.RelativeLayout[3]/android.widget.ImageView").click()

    def setup_method(self):
        print("setup method")

        #TestXueqiuAndroid.driver=self.restart_appium()
        self.driver = TestXueqiuAndroid.driver
        self.driver.find_element_by_xpath("//android.widget.RelativeLayout[3]/android.widget.ImageView").click()

    def test_login(self):

        el1 = TestXueqiuAndroid.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[4]/android.widget.ImageView")
        el1.click()
        el2 = TestXueqiuAndroid.driver.find_element_by_id("com.xueqiu.android:id/tv_login_phone")
        el2.click()

    def test_swipe(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/action_message")
        for i in range(5):
            self.driver.swipe(500,500,200,200)
            time.sleep(2)

    def test_action(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/action_message")
        action=TouchAction(self.driver)
        for i in range(5):
            action.press(x=500,y=500).move_to(x=200,y=200).release().perform()
            time.sleep(2)

    def test_action_p(self):
        rect=self.driver.get_window_rect()

        self.driver.find_element_by_id("com.xueqiu.android:id/action_message")
        action=TouchAction(self.driver)
        for i in range(5):
            action.press(x=rect['width']*0.8,y=rect['height']*0.8).move_to(x=rect['width']*0.2,y=rect['height']*0.2).release().perform()
            time.sleep(2)

    def test_webview_simulator_native(self):
        self.driver.find_element_by_xpath("//*[@text='A股开户']").click()
        self.driver.find_element_by_xpath("//*[@text='立即开户']")
        WebDriverWait(self.driver,10).\
            until(EC.presence_of_element_located((MobileBy.XPATH,"//*[@text='立即开户']")))

    def test_webview_simulator_css(self):
        print(self.driver.contexts)
        print(self.driver.current_context)
        self.driver.switch_to.context(self.driver.contexts[0])
        print(self.driver.current_context)

    def test_message(self):
        TestXueqiuAndroid.driver.find_element_by_id("com.xueqiu.android:id/action_message").click()


    @classmethod
    def init_appium(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "test"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        #caps["noReset"] = True
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(20)
        return driver




    def teardown_method(self):
        self.driver.back()

    @classmethod
    def restart_appium(cls)->WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "test"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"]=True
        driver = webdriver.Remote("http://localhost:5723/wd/hub", caps)
        driver.implicitly_wait(20)
        return driver
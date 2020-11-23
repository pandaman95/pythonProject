import time

import pytest

from page_object.page.MainPage import MainPage
from page_object.page.App import App



class TestSelected(object):

    mainPage:MainPage
    @classmethod
    def setup_class(cls):
        cls.mainPage=App.main()


    def setup_method(self):
        self.mainPage: MainPage=TestSelected.mainPage
        self.searchPage=self.mainPage.gotoSearch()


    def test_is_selected_stock(self):
        # searchPage=App.main().gotoSearch().search("alibaba")
        self.searchPage.search("alibaba")
        # time.sleep(5)
        # self.find("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView").click()
        # self.driver.implicitly_wait(20)
        assert self.searchPage.isInSelected("BABA")==True
        assert self.searchPage.isInSelected("9988")==False

    @pytest.mark.parametrize("key,code",[
        ["招商银行","SH600036"],
        ["平安银行","SZ000001"],
        ["pingan","SH601318"]
    ])
    def test_is_selected_stock_hs(self,key,code):
        self.searchPage.search(key)
        assert self.searchPage.isInSelected(code)==False
    def teardown_method(self):
        self.searchPage.cancel()

    def test_add_stock_hs(self):
        key="招商银行"
        code="SH600036"
        searchPage=self.searchPage.search(key)
        if searchPage.isInSelected(code)==False:
            searchPage.addToSelected(code)
        else:
            searchPage.removeFromSeleted(code)
            searchPage.addToSelected(code)
        assert searchPage.isInSelected(code)==True
    def test_is_follow_user(self):
        #todo
        pass
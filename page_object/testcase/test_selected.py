import time

import pytest

from page_object.page.MainPage import MainPage
from page_object.page.App import App



class TestSelected(object):

    # mainPage:MainPage
    @classmethod
    def setup_class(cls):
        cls.mainPage=App.main()




    def test_price(self):

        assert self.mainPage.gotoSelected().gotoHS().getPriceByName("阿里巴巴") != 257


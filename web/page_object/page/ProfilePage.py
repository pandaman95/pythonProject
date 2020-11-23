from web.page_object.page.BasePage import BasePage
from web.page_object.page.SelectedPage import SelectedPage


class ProfilePage(BasePage):
    def login(self):
        print(self.driver.get_cookies())
        self.driver.add_cookie({"name": "device_id", "value": "24700f9f1986800ab4fcc880530dd0ed"})
        self.driver.add_cookie({"name": "remember", "value": "1"})
        self.driver.add_cookie({"name": "u", "value": "9174226523"})
        self.driver.add_cookie({"name": "bid", "value": "69b46f193365d77661e789abc85e3488_khqgpxea"})
        self.driver.add_cookie(
            {"name": "__utmz", "value": "1.1605888787.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"})
        self.driver.add_cookie({"name": "is_overseas", "value": "0"})
        self.driver.add_cookie({"name": "Hm_lvt_1db88642e346389874251b5a1eded6e3", "value": "1605887174,1605925644"})
        self.driver.add_cookie({"name": "snbim_minify", "value": "true"})
        self.driver.add_cookie({"name": "Hm_lpvt_1db88642e346389874251b5a1eded6e3", "value": "1605925651"})
        self.driver.add_cookie({"name": "__utmb", "value": "1.2.10.1605925651"})
        self.driver.add_cookie({"name": "xq_a_token", "value": "e1e910b417b673b9340b47f9227f36fa550f3498"})
        self.driver.add_cookie({"name": "xq_id_token", "value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9"})
        self.driver.add_cookie({"name": "xqat", "value": "e1e910b417b673b9340b47f9227f36fa550f3498"})
        self.driver.add_cookie({"name": "xq_r_token", "value": "249594bc47ee1604b3b657410451f828b4136eaf"})
        self.driver.add_cookie({"name": "xq_is_login", "value": "1"})
        self.driver.add_cookie({"name": "s", "value": "e712ict4um"})
        self.driver.add_cookie(
            {"name": "acw_tc", "value": "2760825216059256431216855e24aa840342a1721dc8b3fbed237834a9b1cc"})
        self.driver.add_cookie({"name": "snbim_minify", "value": "true"})
        self.driver.add_cookie({"name": "Hm_lpvt_1db88642e346389874251b5a1eded6e3", "value": "1605925651"})
        print(self.driver.get_cookies())
        self.driver.refresh()
    def gotoSelected(self):
        return  SelectedPage(self.driver)
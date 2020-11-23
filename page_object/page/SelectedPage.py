from selenium.webdriver.common.by import By

from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage


class SelectedPage(BasePage):
    def addDefault(self):
        return self
    def gotoHS(self):
        self.findByText("沪深").click()
        return self
    def getPriceByName(self,name)->float:

        # price=self.driver.find_element_by_xpath("//*[contains(@resource-id,'stockName') and @text='"+name+"']/../../../..//*[contains(@resource-id,'currentPrice')]").text
        # // *[contains( @ resource - id, 'portfolio_stockName') and contains( @ text, '阿里巴巴')]
        # // *[contains( @ resource - id, 'portfolio_stockName') and @text='阿里巴巴']
        priceLocator=(By.XPATH,"//*[contains(@resource-id,'stockName') and @text='%s']/../../../..//*[contains(@resource-id,'currentPrice')]" %name)
        price=self.find(priceLocator).text
        return float(price)
from genericlib.WebdriverUtils import webUtils

class Wallet:
    _walletIcon='//li[@class="makeFlex hrtlCenter lhMyWallet"]'
    _balance='//p[@data-cy="walletAmt"]'

    def __init__(self,driver):
        self.driver=driver

    def get_walletIcon(self):
        return self.driver.find_element_by_xpath(self._walletIcon)

    def get_balance(self):
        return self.driver.find_element_by_xpath(self._balance)

    def walletBalance(self):
        self.get_walletIcon().click()
        Title=self.driver.title
        obj_webUtils = webUtils(self.driver)
        obj_webUtils.windowHandler(Title)
        Balance=self.get_balance().text
        print("Wallet Balance is : ",Balance)

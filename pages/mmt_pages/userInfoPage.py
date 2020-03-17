from genericlib.WebdriverUtils import webUtils
class userInfo:
    _accountBtn = '//li[@data-cy="account"]'
    _myProfile = '//p[text()="My Profile"]'
    _keys = '//span[contains(@class,"darkGreyText ")]'
    _values = '//span[contains(@class,"blackText latoBold")]'

    def __init__(self, driver):
        self.driver = driver

    def get_accountBtn(self):
        return self.driver.find_element_by_xpath(self._accountBtn)

    def get_myProfile(self):
        return self.driver.find_element_by_xpath(self._myProfile)

    def get_keys(self):
        obj_keys = self.driver.find_elements_by_xpath(self._keys)
        keys = []
        for i in range(1, len(obj_keys)):
            keys = keys.append(self.driver.find_element_by_xpath('(//span[contains(@class,"darkGreyText ")])[{}]'.format(i)).text)
        return keys

    def get_values(self):
        obj_values = self.driver.find_elements_by_xpath(self._keys)
        values = []
        for i in range(1, len(obj_values)):
            values = values.append(
                self.driver.find_element_by_xpath('//span[contains(@class,"blackText latoBold")]'.format(i)).text)
        return values

    def get_userInfoDict(self):
        userInfo = dict()
        keys = self.get_keys()
        values = self.get_values()
        for i in range(len(keys) + 1):
            userInfo[keys[i]] = values[i]
        return userInfo

    def get_userDetails(self):
        self.get_accountBtn().click()
        self.get_myProfile().click()
        Title = self.driver.title
        obj_web = webUtils(self.driver)
        obj_web.windowHandler(Title)
        userdetails = self.get_userInfoDict()
        return userdetails

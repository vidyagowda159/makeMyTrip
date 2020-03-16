class Logout:
    _accountbtn = '//li[@data-cy="account"]'
    _logout = '//p[text()="Logout"]'

    def __init__(self,driver):
        self.driver = driver

    def get_Account(self):
        return self.driver.find_element_by_xpath(self._accountbtn)

    def get_logout(self):
        return self.driver.find_element_by_xpath(self._logout)

    def logout(self):
        self.get_Account().click()
        self.get_logout().click()

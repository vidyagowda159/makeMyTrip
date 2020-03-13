class clearTrip:
    _username = ''
    _password = ''
    _loginbtn = ''

    def __init__(self,driver):
        self.driver = driver

    def get_username(self):
        return self.driver.find_element_by_xpath(self._username)

    def get_password(self):
        return self.driver.find_element_by_xpath(self._password)

    def get_loginbtn(self):
        return self.driver.find_element_by_xpath(self._loginbtn)

    def login(self,username,password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_loginbtn().click()
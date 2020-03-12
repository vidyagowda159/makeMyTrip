class webUtils:
    def __init__(self,driver):
        self.driver=driver

    def implicitTime(self,time):
        self.driver.implicitly_wait(time)

    def windowHandler(self,pageTitle):
       handles = self.driver.window_handles
       for handle in handles:
           self.driver.switch_to.window(handle)
           Title=self.driver.title
           if Title!=pageTitle:
               self.driver.switch_to.window(handle)
               break


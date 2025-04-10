from abc import ABC , abstractmethod

class BankApp(ABC):
    @abstractmethod
    def secuirty(self):
        pass


class MobileApp(BankApp):
    def secuirty(self):
        print("Secured Gateway for Mobile !!")

    def MobileLogin(self):
        print('Mobile Login Successfully!')


class Website(BankApp):
    def secuirty(self):
        print("Secured Gateway for Website!!")

    def WebsiteLogin(self):
        print('Website Login Successfully!')



MobileObj = MobileApp()
MobileObj.secuirty()
WebsiteObj = Website()
WebsiteObj.secuirty()
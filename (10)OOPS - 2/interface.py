from abc import ABC , abstractmethod

class interface(ABC):
    @abstractmethod
    def absMethod1(self):
        pass

    @abstractmethod
    def absMethod2(self):
        pass


class Derived(interface):
    def absMethod1(self):
        print('Abstract Method 1 defined !')

   
    def absMethod2(self):
        print('Abstract Method 2 defined !')

obj = Derived()
obj.absMethod1()
obj.absMethod2()

from abc import ABC , abstractmethod


class AbstractBaseClass(ABC):
    def __init__(self):
        print('Costructor of the abstract method!')

    @abstractmethod
    def absMethod(self):
        print('Abstract Method from the base class!')
    
    def concreteMethod(self):
        print('Concrete Method from the base class!')


class Derived(AbstractBaseClass):
    def absMethod(self):
        super().absMethod()
        print('Redfined abstract method!')


obj = Derived()
obj.absMethod()
obj.concreteMethod()
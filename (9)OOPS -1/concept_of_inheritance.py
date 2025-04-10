class BaseClass:
    def __init__(self):
        print('Constructor of the base class!')

    def BaseMethod(self):
        print('Base class Method!')

class Derived(BaseClass):
    def __init__(self):
        print('Constructor of the Derived class!')

    def DerivedMethod(self):
        print('Dervied class Method!')

obj1 = Derived()
obj2 = BaseClass()
obj1.BaseMethod()
obj1.DerivedMethod()

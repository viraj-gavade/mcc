class Parent1:
    def Method1(self):
        print('Method of the parent-1')
    
class Parent2:
    def Method2(self):
        print('Method of the parent-2')

class Child(Parent1,Parent2):
    def Method3(self):
        print('Method od the child class')



obj = Child()
obj.Method1()
obj.Method2()
obj.Method3()
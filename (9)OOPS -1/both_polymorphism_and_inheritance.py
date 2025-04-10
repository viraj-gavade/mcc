class Parent1:
    def Method1(self):
        print('Method of the parent-1')

    def DefaultMthod(self):
        print('Default-Method-Parent-1')
    
class Parent2:
    def Method2(self):
        print('Method of the parent-2')

    def DefaultMthod(self):
        print('Default-Method-Parent-2')

class Child(Parent1,Parent2):
    def Method3(self):
        print('Method od the child class')

    def DefaultMthod(self):
        print('Default-Method-child')



obj = Child()
obj.Method1()
obj.Method2()
obj.Method3()
obj.DefaultMthod()
class Parent:
    def __init__(self):
        self.show="Hi! I am Parent class!"
    def display_parent(self):
        print(self.show)
            
class Child(Parent):
    def display_child(self):
            print("Hi! You are in the method of the child class ")

obj=Child()
obj.display_parent()
obj.display_child()

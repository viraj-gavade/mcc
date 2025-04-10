class Program():
    def __init__(self):
        self.string = ""
        #first method to input string
    def  inp(self):
        self.string=input("enter a string")
        #second method to display
    def display(self):
        print("User entered the following string:")
        print(self.string)

obj=Program()
obj.inp()
obj.display()

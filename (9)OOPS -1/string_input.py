class DemoClass :
    def takeInput(self):
        self.string = input('Enter a string:- ')

    def DisplayInput(self):
        print(self.string)


obj = DemoClass()
obj.takeInput()
obj.DisplayInput()
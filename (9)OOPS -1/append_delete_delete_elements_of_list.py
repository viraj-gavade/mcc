class Program:
    def __init__(self):
        self.n =[]

    def AddElement(self,element):
      return self.n.append(element)

    def RemoveElement(self,element):
      return self.n.remove(element)
    
    def DisplayList(self,):
      return self.n

obj = Program()

print('1.Add Element')
print('2.Remove Element')
print('3.Display List')
print('3.Exit')

try:
    choice = int(input('Enter Your Choice:-'))
    if(choice == 1):
        n = int(input('Enter a element you wish to add'))
        obj.AddElement(n)
        print('List is :-',obj.DisplayList())

    elif(choice == 2):
        n = int(input('Enter a element you wish to remove'))
        obj.RemoveElement(n)
        print('List is :-',obj.DisplayList())

    elif(choice == 3):
        print('List is :-',obj.DisplayList())

    elif(choice == 4):
        print('Exiting')

    else:
        print('Invalid Choice')

except Exception as e:
    print(e)

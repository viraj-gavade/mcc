class Program():
    def __init__(self):
        self.n=[]
    def add(self,a):
        return self.n.append(a)
    def remove(self,b):
        self.n.remove(b)
    def diplay(self):
        return (self.n)

obj = Program()
select = 1
while select !=0:
    print("1 . Add an elemet to the list")1
    
    print("2.Delete an element from a list")
    print("3.Display list")
    print("4.Exit")
    select=int(input("Enter your choice "))
    if select ==1:
        n=int(input("Enter a number to add"))
        obj.add(n)
        print("List is:-",obj.diplay())

    elif select ==2:
        n=int(input("Enter a number to be removed"))
        obj.remove(n)
        print("List is:-",obj.diplay())

    elif select ==3:
        print("List is:-",obj.diplay())

    elif select ==4:
        print("Exiting")
    else:
        print("Please enter  valid choice")
print()

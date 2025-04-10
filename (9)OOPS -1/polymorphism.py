class Maths : 
    def addition(a):
        return a 

class Dervied1(Maths):
     def addition(a:int,b:int):
        return a + b 


class Dervied2(Maths):
     def addition(a:int,b:int,c:int):
        return a + b + c


obj1 = Maths()
print(Maths.addition(2))

obj2 = Dervied1()
print(Dervied1.addition(2,3))

obj3 = Dervied2()
print(Dervied2.addition(2,3,4))
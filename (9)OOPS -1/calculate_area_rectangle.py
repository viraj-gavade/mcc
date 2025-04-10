class Shape :
    def __init__(self,length, breadth):
        self.length = int(input('Enter the length of rectangle:- '))
        self.breadth = int(input('Enter the breadth of rectangle:- '))
    
    def CalculateArea(self):
        res = self.length*self.breadth
        print('Area of rectangle:- ' , res)


obj = Shape(2,4)
obj.CalculateArea()
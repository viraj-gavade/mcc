class Area():
    def __init__(self, r_length,r_breadth):
         self.r_breadth = r_breadth
         self.r_length = r_length
    def calculate(self):
        return self.r_breadth*self.r_length


first = int(input("please enter the length of the rectangle"))

second = int(input("please enter the breadth of the rectangle"))

obj=Area(first,second)
print("Area of rectangle: " , obj.calculate())

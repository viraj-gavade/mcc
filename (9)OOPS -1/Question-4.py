class Comp_Number:
    def __init__(self , r=0,i=0):
        self.real = r
        self.imag = i
    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

#creating new complex number
c1=Comp_Number(2,3)
c1.getData()


c2=Comp_Number(5)
c2.attr= 10
c2.getData()


print((c2.real,c2.imag,c2.attr))

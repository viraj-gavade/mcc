class subset:
    def func1(self,s1):
        return self.func2([],sorted(s1))
    def func2(self,curr,s1):
        if s1:
            return self.func2(curr,s1[1:])+self.func2(curr+[s1[0]],s1[1:])
        return [curr]

x=[]
n=int(input("enter no. of elements of list"))
for i in range(0,n):
    y=int(input("Enter an element"))
    x.append(y)


print("Subsets are :")
print(subset().func1(x))

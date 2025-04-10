#program to handle multiple errors with one except statement
try:
    variable = 55
    if variable<100:
        varaible2=varaible2/(varaible2-55)
        #this statement throws NameError
        print("Value of varaible2=",b)
        varaible3=[1,2,3]
        #this statement throws IndexError
        print(varaible3[5])

except(IndexError,ZeroDivisionError,NameError):
    print("\n This is program throws multiple errors like IndexError,ZeroDivisionError,NameError")

#Q.2 Write a python program to use multiple 'except'.
first=3
second=9
third=second/first
print("Ans = ",third)
try:
    #code with possibilities of multiple exception
    fourth=int(input("Enter a Number"))
    third=second/fourth
    print("Ans = ",third)
except ValueError:
    print("please enter valid input")
    
except ZeroDivisionError:
    print("zero not allowed")

except ArithmeticError:
    print("please enter value greater than zero")
    

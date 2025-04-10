#esle block
first=3
second=9
third=second/first
print("Ans = ",third)
try:
    #code with possibilities of multiple exception
    fourth=int(input("Enter a Number"))
    third=second/fourth
    print("Ans = ",third)
except Exception:
    print("please enter value greater than zero")
    
else:
    print("Success!!")
    

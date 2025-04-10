class objulator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Bruh, division by zero?"
        return a / b


obj = objulator()
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = input("Enter choice (1/2/3/4): ")
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", obj.add(num1, num2))
    elif choice == '2':
        print("Result:", obj.subtract(num1, num2))
    elif choice == '3':
        print("Result:", obj.multiply(num1, num2))
    elif choice == '4':
        print("Result:", obj.divide(num1, num2))
    else:
        print("Invalid choice.")
except Exception as e :
    print(e)

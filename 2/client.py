import sys
from omniORB import CORBA
import Calculator

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# Read the IOR from the file
with open("calculator.ior", "r") as f:
    ior = f.read().strip()

# Convert the IOR string to an object reference
obj = orb.string_to_object(ior)

# Narrow the object reference to the Calculator interface
calculator = obj._narrow(Calculator.Calculator)

if calculator is None:
    print("Object reference is not a Calculator")
    sys.exit(1)

while True:
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "0":
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        result = calculator.add(num1, num2)
        print("Addition result:", result)
    elif choice == "2":
        result = calculator.subtract(num1, num2)
        print("Subtraction result:", result)
    elif choice == "3":
        result = calculator.multiply(num1, num2)
        print("Multiplication result:", result)
    elif choice == "4":
        try:
            result = calculator.divide(num1, num2)
            print("Division result:", result)
        except Calculator.DivisionByZero:
            print("Error: Division by zero")
    else:
        print("Invalid choice. Please try again.")


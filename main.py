from utils import *

operación = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit): ").lower()
while operación != "exit":
    if operación not in ("add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide", "absolute", "exit"):
        print("Invalid option!")
        operación = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit): ").lower()
    else:
        if operación == "absolute":
            num = int(input("Enter the number: "))
        else:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            
        if operación == "divide":
            num_2 = divide(num1, num2)
            if num_2 == "Error: Division by zero is not allowed.":
                print(num_2)
            else:
                print(f"The result is: {num_2}")
        elif operación == "modulo":
            num_2 = modulo(num1, num2)
            if num_2 == "Error: Division by zero is not allowed.":
                print(num_2)
            else:
                print(f"The result is: {num_2}")
        elif operación == "floor_divide":
            num_2 = floor_divide(num1, num2)
            if num_2 == "Error: Division by zero is not allowed.":
                print(num_2)
            else:
                print(f"The result is: {num_2}")
        elif operación == "add":
            operar = add(num1, num2)
            print(f"The result is: {operar}")
        elif operación == "subtract":
            operar = sub(num1, num2)
            print(f"The result is: {operar}")
        elif operación == "multiply":
            operar = multiply(num1, num2)
            print(f"The result is: {operar}")
        elif operación == "absolute":
            operar = absolute(num)
            print(f"The result is: {operar}")
        elif operación == "exponent":
            operar = exponent(num1, num2)
            print(f"The result is: {operar}")
    operación = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit): ").lower()


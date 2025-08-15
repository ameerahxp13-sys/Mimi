print("Welcome to Ameerah's Super Calculator!")

# Get numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask for operation
print("Choose operation: +, -, *, /, **, %, //")
print("Or type: add, subtract, multiply, divide, power, mod, floor")
operation = input("Enter operation: ").lower()

# Perform operation
if operation in ["+", "add"]:
    print("Result:", num1 + num2)
elif operation in ["-", "subtract"]:
    print("Result:", num1 - num2)
elif operation in ["*", "multiply"]:
    print("Result:", num1 * num2)
elif operation in ["/", "divide"]:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero!")
elif operation in ["**", "power"]:
    print("Result:", num1 ** num2)
elif operation in ["%", "mod"]:
    if num2 != 0:
        print("Result:", num1 % num2)
    else:
        print("Error: Cannot divide by zero!")
elif operation in ["//", "floor"]:
    if num2 != 0:
        print("Result:", num1 // num2)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operation!")
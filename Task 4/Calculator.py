def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation in operations:
            return operation, operations[operation]
        print("Invalid operation. Please enter one of +, -, *, /.")

def calculator():
    print("Simple Command-line Calculator")
    while True:
        num1 = get_number("Enter the first number: ")
        operation, func = get_operation()
        num2 = get_number("Enter the second number: ")

        result = func(num1, num2)
        print(f"The result of {num1} {operation} {num2} is: {result}")

        cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    calculator()

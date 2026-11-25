def safe_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input, enter a number.")

def safe_div(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

a = safe_input("Enter first number: ")
b = safe_input("Enter second number: ")
print("Result =", safe_div(a, b))

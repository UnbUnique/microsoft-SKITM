from add import add
from sub import sub
from mul import mul
from div import div

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result =", add(num1, num2))
elif op == "-":
    print("Result =", sub(num1, num2))
elif op == "*":
    print("Result =", mul(num1, num2))
elif op == "/":
    print("Result =", div(num1, num2))
else:
    print("Invalid operator")

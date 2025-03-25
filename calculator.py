num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = str(input("Enter operation (+, -, *, /): "))

if op == '+':
    total = num1 + num2

elif op == '-':
    total = num1 - num2

elif op == '*':
    total = num1 * num2

elif op == '/':
    if num2 != 0:
        total = num1 / num2
    else:
        total = "Please dont use 0"

else:
    total = str("Please enter valid operation")

print("Answer:", total)
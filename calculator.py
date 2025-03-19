print("Welcome to the calculator")
print("Please input two numbers and an operation as asked\n")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
answer=0
print("Choices: \n + \n - \n / \n *\n")
operation=input("Enter operation: ")
if operation == "+":
    answer=num1+num2
    print(f"{num1} + {num2} = {answer}")
elif operation == "-":
    answer=num1-num2
    print(f"{num1} - {num2} = {answer}")
elif operation == "/":
    answer=num1/num2
    print(f"{num1} / {num2} = {answer}")
elif operation == "*":
    answer=num1*num2
    print(f"{num1} * {num2} = {answer}")
else:
    print("Invalid operation")

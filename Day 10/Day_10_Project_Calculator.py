def addCalc(num1, num2):
    return float(num1) + float(num2)

def subCalc(num1, num2):
    return float(num1) - float(num2)

def mulCalc(num1, num2):
    return float(num1) * float(num2)

def divCalc(num1, num2):
    if num2 == 0:
        txt = "Denominator cannot be 0!"
        return txt
    else:
        return float(num1) / float(num2)

def logic(n1):
    print("+ - * /")
    operation = input("Pick the operation: ")
    number2 = float(input("What's the second number? "))
    if operation == "+":
        value = addCalc(n1, number2)
        print(f"{n1} + {number2} = {value}")
    elif operation == "-":
        value = subCalc(n1, number2)
        print(f"{n1} - {number2} = {value}")
    elif operation == "*":
        value = mulCalc(n1, number2)
        print(f"{n1} * {number2} = {value}")
    elif operation == "/":
        value = divCalc(n1, number2)
        print(f"{n1} / {number2} = {value}")

    choice = input("Want to contnue with same number? Enter 'y'").lower()

    if choice == 'y':
        logic(value)
    elif choice == 'n':
        start()
    else:
        print("Wrong choice!")

def start():

    number1 = float(input("What's the first number? "))
    logic(number1)

start()
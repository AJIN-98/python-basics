def addition(num1, num2):
    num1 += num2
    print("sum is :", num1)


def subtraction(num1, num2):
    num1 -= num2
    print("difference is :", num1)


def mul(num1, num2):
    num1 *= num2
    print("product is :", num1)


def division(num1, num2):
    num1 /= num2
    print("quotient is :", num1)


def default(num1, num2):
    print("invalid option")


switcher = {
    1: addition,
    2: subtraction,
    3: mul,
    4: division
}


def switch(operation, num1, num2):
    return switcher.get(operation, default)(num1, num2)


while True:

    print('''Welcome to the SimpleCalc
    Press 1 to add two numbers
    Press 2 to subtract two numbers
    Press 3 to multiply two numbers
    Press 4 to divide two numbers
    Press 5 to Exit''')
    choice = int(input("Select operation from 1,2,3,4,5 : "))
    if choice == 5:
        print("exited!")
        break
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    switch(choice, num1, num2)
    key = input("Do You Want To Continue? [y/n] :")
    if key == "n":
        print("exited!")
        break

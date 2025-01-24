def add():
    print("Perform addition.\n")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3= float(input("Enter the third number :"))
    print(f"The result of addition is: {num1 + num2+num3}\n")

def subtract():
    print("Perform subtraction.\n")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3= float(input("Enter the third number :"))
    print(f"The result of subtraction is: {num1 - num2-num3}\n")


def multiply():
    print("Perform multiplication.\n")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3= float(input("Enter the third number :"))
    print(f"The result of multiplication is: {num1 * num2 * num3}\n")


def divide():
    print("Perform division.\n")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3= float(input("Enter the third number :"))
    if num2 == 0 or num3 == 0:
        print("Error: Division by zero is not allowed.\n")
    else:
        print(f"The result of division is: {num1 / num2 / num3}\n")


def calculator():
    print("Menu-driven calculator program.\n")
    while (1):
        print("**** Basic Calculator ****")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            add()
        elif choice == '2':
            subtract()
        elif choice == '3':
            multiply()
        elif choice == '4':
            divide()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

calculator()
    

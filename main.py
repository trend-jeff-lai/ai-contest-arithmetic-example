import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square_root(x):
    return math.sqrt(x)

def square(x):
    return x * x

def cube(x):
    return x * x * x

def display_menu():
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square root")
    print("6. Square")
    print("7. Cube")
    print("0. Exit")

def get_choice():
    choice = input("Enter choice (0/1/2/3/4/5/6/7): ")

    if choice in ('0', '1', '2', '3', '4', '5', '6', '7'):
        return choice
    else:
        print("Invalid choice.")
        return None

def get_two_input():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

def get_single_input():
    num = float(input("Enter number: "))
    return num

def perform_calculation(choice, num1, num2):
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        print("sqrt(", num1, ")=", square_root(num1))
    elif choice == '6':
        print(num1, "*", num1, "=", square(num1))
    elif choice == '7':
        print(num1, "*", num1, "*", num1, "=", cube(num1))
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    display_menu()
    choice = get_choice()

    if choice is not None:
        if choice == '0':
            print("Goodbye.")
        else:
            if choice == '5' or choice == '6' or choice == '7':
                num1 = get_single_input()
                perform_calculation(choice, num1, None)
            else:
                num1, num2 = get_two_input()
                perform_calculation(choice, num1, num2)

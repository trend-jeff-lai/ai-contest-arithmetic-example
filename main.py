import math

def add(x, y):
    return x + y

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
    choice = input("Enter choice (0/1): ")

    if choice in ('0', '1'):
        return choice
    else:
        print("Invalid choice.")
        return None

def get_two_input():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

def perform_calculation(choice, num1, num2):
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    display_menu()
    choice = get_choice()

    if choice is not None:
        if choice == '0':
            print("Goodbye.")
        else:
            num1, num2 = get_two_input()
            perform_calculation(choice, num1, num2)

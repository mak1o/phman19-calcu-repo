def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot be divided by 0"
    return a / b

def display_menu():
    print("Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_valid_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")

def simple_calcu():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the program...")
            break
        elif choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a number from 1 to 5.")
            continue

        a = get_valid_number("Enter the first number: ")
        b = get_valid_number("Enter the second number: ")

        result = None

        if choice == '1':
            result = addition(a, b)
        elif choice == '2':
            result = subtraction(a, b)
        elif choice == '3':
            result = multiplication(a, b)
        elif choice == '4':
            result = division(a, b)

        print("Result: ", result)

        continue_choice = input("Do you want to continue? (yes/no): ")
        if continue_choice.lower() != 'yes':
            print("Exiting the calculator...")
            break

simple_calcu()

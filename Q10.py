import math
import random
from datetime import datetime

history = {}

def basic_arithmetic():
    try:
        num1 = float(input("\nEnter First Number: "))
        num2 = float(input("Enter Second Number: "))

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("\nChoose Operation: "))

        if choice == 1:
            result = num1 + num2
            operation = "Addition"

        elif choice == 2:
            result = num1 - num2
            operation = "Subtraction"

        elif choice == 3:
            result = num1 * num2
            operation = "Multiplication"

        elif choice == 4:
            result = num1 / num2
            operation = "Division"

        else:
            print("Invalid Choice")
            return

        print("Result:", result)
        store_result(operation, result)

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except ValueError:
        print("Invalid input! Enter numbers only.")

def scientific_calculation():
    try:
        num = float(input("\nEnter Number: "))

        print("\n1. Square Root")
        print("2. Square")
        print("3. Factorial")

        choice = int(input("\nChoose Operation: "))

        if choice == 1:
            result = math.sqrt(num)
            operation = "Square Root"

        elif choice == 2:
            result = math.pow(num, 2)
            operation = "Square"

        elif choice == 3:
            result = math.factorial(int(num))
            operation = "Factorial"

        else:
            print("Invalid Choice")
            return

        print("Result:", result)
        store_result(operation, result)

    except Exception as e:
        print("Error:", e)

def generate_random():
    numbers = []

    for i in range(5):
        numbers.append(random.randint(1, 100))

    print("Random Numbers:", numbers)

    store_result("Random Numbers", numbers)

def store_result(operation, result):
    timestamp = str(datetime.now())

    history[timestamp] = {
        "Operation": operation,
        "Result": result
    }


def view_history():
    if len(history) == 0:
        print("No History Available.")

    else:
        print("\n------ History ------")

        for time, data in history.items():
            print("Time:", time)
            print("Operation:", data["Operation"])
            print("Result:", data["Result"])
            print("-------------------------")

while True:

    print("\n>>>>>>> Smart Calculator <<<<<<<")
    print("\n1. Basic Arithmetic")
    print("2. Scientific Calculation")
    print("3. Generate Random Numbers")
    print("4. View History")
    print("5. Exit")

    try:
        choice = int(input("\nEnter Your Choice: "))

        if choice == 1:
            basic_arithmetic()

        elif choice == 2:
            scientific_calculation()

        elif choice == 3:
            generate_random()

        elif choice == 4:
            view_history()

        elif choice == 5:
            print("\nProgram Closed Successfully.")
            break

        else:
            print("Invalid Choice.")

    except ValueError:
        print("Please enter a valid number.")
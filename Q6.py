import random
import math

try:
    numbers = set()

    print("\nEnter 10 numbers---")
    print()
    while len(numbers) < 10:
        num = int(input(f"Enter number {len(numbers)+1}: "))
        numbers.add(num)

    print("\nUnique Numbers (Set):", numbers)

    number_tuple = tuple(numbers)

    print("\nTuple:", number_tuple)

    random_numbers = random.sample(number_tuple, 3)
    print("\n3 Random Numbers:", random_numbers)

    total = sum(number_tuple)
    square_root = math.sqrt(total)

    print("\nSum of Tuple Elements:", total)
    print("\nSquare Root of Sum:", square_root)
    print()
except ValueError:
    print("\nInvalid input! Please enter only numbers.")

except Exception as e:
    print("Error:", e)
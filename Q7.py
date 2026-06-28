square = lambda x: x * x
numbers = range(1, 21)
square_list = list(map(square, numbers))

print("\nSquares of numbers from 1 to 20:")
print(square_list)

print("\nEven Squares:")
for num in square_list:
    if num % 2 == 0:
       print(num,end=" ")
print()


numbers = [1, 2, 3, 4, 5]

# Define a function that squares a number
def square(x):
    return x ** 2

# Apply the square function to each item in the numbers list using map()
squared_numbers = map(square, numbers)

# Convert the map object to a list and print it
print(tuple(squared_numbers))


print(list(map(lambda x: x ** 2, numbers)))

print("filter")


numbers = ["green","blue","red","orange","black","pink"]

def square(x):
    if "a" in x:
        return x

# Apply the square function to each item in the numbers list using map()
squared_numbers = map(square, numbers)
Filtered_color = filter(square, numbers)

# Convert the map object to a list and print it
print(tuple(squared_numbers))
print(list(Filtered_color))


print("reduce()")

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)

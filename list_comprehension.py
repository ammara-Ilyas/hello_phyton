numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)


numbers = [1, 2, 3, 4, 5, 6]
squared_even_numbers = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
print(list(squared_even_numbers))

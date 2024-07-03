# x="Hello"
# y=25
# print(x,y)
# print("good")
# # taking input
# # name=input("who are you?")
# # print(name)
# ####################### concetenation
# # old_age=input("Enter your age")
# # new_age=int(old_age)+2
# # print("age"+str(new_age))
# # float()
# # str()
# # int()
# # bool()
# ################### methods
# print(x.upper())
# #################keywords
# fName="Tony Sekhar"
# print("S" in fName)
# ############operation
# # +,-,*,/,%,**
# # #################################operation procedeer
# # []{}()*/-+
# # ##############operator
# # or not and
# print(3 > 2 and 5<2)
# #############33 if else
# age=18
# if age>=20:
#      print("adult")
# elif age>=10 and age<=20:
#      print("child")
# ###############################
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))
# tex= f"My name is John, and I am {age}"
# print(tex)
# ########################################################String
# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"
# x,y,z="orange","banana","grapes"
# print(x , y ,z)
# print(x.lower())
# #########################String methods 
# """upper(): Converts the string to uppercase.
# lower(): Converts the string to lowercase.
# strip(): Removes leading and trailing whitespace.
# replace(): Replaces a substring with a new string.
# split(): Splits the string into a list of substrings.
# join(): Joins a list of strings into a single string.
# len(): Returns the length of the string.
# find(): Finds the index of a substring.
# rfind(): Finds the index of a substring, starting from the end.
# count(): Counts the number of occurrences of a substring.
# startswith(): Checks if the string starts with a substring.
# endswith(): Checks if the string ends with a substring.
# index(): Returns the index of a substring.
# rindex(): Returns the index of a substring, starting from the end.
# format(): Formats the string with variables.
# capitalize(): Capitalizes the first letter of the string.
# title(): Capitalizes the first letter of each word.
# swapcase(): Swaps the case of the string."""

# my_string = "   hello   "
# print(my_string.strip())  # Output: "hello"
# my_string = "hello world"
# print(my_string.replace("world", "Python"))  # Output: "hello Python"
# my_string = "hello,world,Python"
# print(my_string.split(","))  # Output: ["hello", "world", "Python"]
# my_list = ["hello", "world", "Python"]
# print(",".join(my_list))  # Output: "hello,world,Python"
# my_string = "hello"
# print(len(my_string))  # Output: 5
# my_string = "hello world"
# print(my_string.find("world"))  # Output: 6
# my_string = "hello world world"
# print(my_string.count("world"))  # Output: 2
# my_string = "hello world"
# print(my_string.startswith("hello"))  # Output: True
# my_string = "hello world"
# print(my_string.endswith("world"))  # Output: True
# ###############################Integers
# x=20
# print(x.__float__())

# f-string
name="Yahoo"
age=23
hobby="Hockey"
print(f"My name is {name}, and my age is {age} and my hobby is {hobby}")
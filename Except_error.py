try:
    result = 10 / 0
    print(result)
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}",end="\n")


try:
    result = int("a string")
except (ValueError, TypeError) as e:
    print(f"Caught an exception: {e}",end="\n")


try:
    result = 10 / 2
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
else:
    print(f"Result is: {result}")
finally:
    print("This will always execute.")


class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(f"Caught an exception: {e.message}")


try:
    with open("non_existent_file.txt", "r") as file:
        data = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")
else:
    print("File read successfully.")
finally:
    print("Execution complete.")

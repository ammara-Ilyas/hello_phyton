# file = open("example.txt", "r")  # Open for reading (default mode)
# file = open("example.txt", "w")  # Open for writing (truncates file if exists)
# file = open("example.txt", "a")  # Open for appending (creates file if doesn't exist)
# file = open("example.txt", "b")  # Open in binary mode



# with open("example.txt", "w") as file:
#     file.write("Hello, World!\n")  # Writes a string to the file
    # file.writelines(["Line 1\n", "Line 2\n"])  # Writes a list of strings
    
    
with open("example.txt", "r") as file:
#     content = file.read()  # Reads the entire file
#     line = file.readline()  # Reads one line at a time
    lines = file.readlines()  # Reads all lines into a list
#     print(f"Content is {content} and line is {line} and lines are {lines}")


with open("example.txt","a") as file:
    file.write("This is append lines \n")
    file.write("This is append lines2 \n")
    


delet_line="This is append linesThis is append linesThis is append lines2This is append lines /nThis is append lines2 /nThis is append lines "

deleted = [line for line in lines if line != delet_line]

with open("example.txt", "w") as file:
  file.writelines(deleted)  # Writes a list of strings


with open("example.txt", "r") as file:
  read_lines= file.readlines()
  
  print(read_lines)
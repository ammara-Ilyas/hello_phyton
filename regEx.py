import re

text = "This is an example_123."
matches = re.findall(r'\w+', text)
print(matches)  # Output: ['This', 'is', 'an', 'example_123']


text = "This  is \t a test."
matches = re.findall(r'\s+', text)
print(matches)  # Output: ['  ', ' ', '\t ', ' ']


text = "Hello, my friend!"
matches = re.findall(r'[a-z]+', text)
print(matches)  # Output: ['ello', 'my', 'friend']


text = "HELLO and Hi!"
matches = re.findall(r'[A-Z]+', text)
print(matches)  # Output: ['HELLO', 'H']


text = "This is a test for four-word matching."
matches = re.findall(r'\b\w{4}\b', text)
print(matches)  # Output: ['This', 'test', 'four']


text = "Item 1 costs 500 dollars."
matches = re.findall(r'\D+', text)
print(matches)  # Output: ['Item ', ' costs ', ' dollars.']


text = "This is a test!"
matches = re.findall(r'\S+', text)
print(matches)  # Output: ['This', 'is', 'a', 'test!']


text = "Regex123 is cool!"
matches = re.findall(r'[a-zA-Z]+', text)
print(matches)  # Output: ['Regex', 'is', 'cool']


text = "I have 99 problems, 1234 solutions, and 5 reasons."
matches = re.findall(r'\b\d{2,4}\b', text)
print(matches)  # Output: ['99', '1234']


text = "There are 123 apples and 45 bananas."
matches = re.findall(r'[^\d]+', text)
print(matches)  # Output: ['There are ', ' apples and ', ' bananas.']

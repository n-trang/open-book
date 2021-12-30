import string

str = input('please enter a string: ')
list = string.ascii_lowercase
for char in str:
    list[char] += 1
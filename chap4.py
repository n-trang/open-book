# prefixes = "JKLMNOPQ"
# suffix = "ack"

# for i in prefixes:
#     if i == 'Q' or i == 'O':
#         print(i + 'u' + suffix)
#     else:
#         print(i + suffix)

# sentence = list(input("Enter a string: "))

# # remove a letter
# rm_letter = input("Enter the letter to remove: ")
# new_sentence = ""
# for char in sentence:
#     if char != rm_letter:
#         new_sentence += char
# print(new_sentence)

# #count a letter
# count_letter = input("Enter letter to count: ")
# i = 0
# for char in sentence:
#     if char == count_letter:
#         i += 1
# print("the letter", count_letter, "appears", i, "times." )

# #counting the length
# a = ['spam!', 'one', ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
# for i in a:
#     print(len(i))

# """Compute the sum of 1 + 2 + 3 + ... + n, and print the total."""
# n = int(input("Enter the number to which you want to sum: "))

# running_total = 0
# num = 1
# while num <= n:
#     running_total = running_total + num
#     print(running_total)
#     num = num + 1
#     print(num)

# print("The total is: ", running_total)

# n = int(input("Enter n: "))

# count = 0
# while n != 0:
#     count = count + 1
#     print(count)
#     n = n // 10
#     print(n)

# print(count)

invite = input('Enter invitee name: ')
list = []
while invite != "":
    list.append(invite)
    invite = input('Enter invitee name: ')

for i in list:
    print(i, "please join.")
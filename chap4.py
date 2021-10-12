prefixes = "JKLMNOPQ"
suffix = "ack"

for i in prefixes:
    if i == 'Q' or i == 'O':
        print(i + 'u' + suffix)
    else:
        print(i + suffix)

sentence = input("Enter a string: ")
letter = input("Enter the letter to remove: ")
print(enumerate(sentence))
# for index, char in enumerate(sentence):
#     if char == letter:
#         del sentence[index]
# print(sentence)
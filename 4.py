#1
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    print(letter + suffix)

#2
sentence = input("Enter the sentence ")
removed_letter = input("Enter the letter to removed ")

for letter in sentence:
    if letter == removed_letter:
        new_sentence = sentence.replace(letter, "")
    else:
        new_sentence = sentence
print(new_sentence)

#3
t = 0
for letter in sentence:
    if letter == removed_letter:
        t += 1
if t == 0:
    print('there is no ', removed_letter, 'in the sentence')
else:
    print('the letter', removed_letter, 'appeared', t, 'times')

#5
x = ['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
for thing in x:
    if type(thing) == int:
        continue
    else:
        print(len(thing))


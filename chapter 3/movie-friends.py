print("invite 4 friends:")
list_friend=[]

while len(list_friend) < 4:
    friend = input('Who you want to invite:' )
    list_friend.append(friend)
    print(list_friend)

print("great let's go with ", list_friend)

class_room = ("Alejandro", "Ed", "Kathryn", "Presila", "Sean", "Peter")
print(class_room[:])
print(class_room[4:-1])
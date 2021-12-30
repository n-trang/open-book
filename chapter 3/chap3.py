print("invite 4 friends:")
list_friend=[]

while len(list_friend) < 4:
    friend = input('Who you want to invite:' )
    list_friend.append(friend)
    print(list_friend)

print("great let's go with ", list_friend)

# this = ['I', 'am', 'not', 'a', 'crook']
# that = ['I', 'am', 'not', 'a', 'crook']
# print("Test 1:", this is that)
# print(this==that)
# that = this
# print("Test 2:", this is that)

# # Test 1 return `Flase` because the object `a` is not the object `b`, eventhough we can see they are equal. the keyword `is` is to test if two varibles refer to the same object.
# # Test 2 return `True` because not that we have assigned `that` to `this`, they are the same object, hence the result `True`.

class_room = ("Alejandro", "Ed", "Kathryn", "Presila", "Sean", "Peter")
print(class_room[:])
print(class_room[4:-1])
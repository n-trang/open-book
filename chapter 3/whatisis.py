this = ['I', 'am', 'not', 'a', 'crook']
that = ['I', 'am', 'not', 'a', 'crookk']

print (this)
print (that)
print("Test 1:", this is that)
that = this
print(that)
print("Test 2:", this is that)
hello = 'hello'
that = (this.append(hello))
print ('Test 3:', this is that)

# Explaination: Test 1 fail because the 2 list are different objects, regardless of their contents are the same. But when reassign that to this, now they are the same object (`is`) with different name.

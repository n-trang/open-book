name_list = []
name = input("enter a name ")
name_list.append(name)
print(name_list)
invitation = 'welcome ' + name
# 
while name != "":
    name_list.append(name)
    name = input('write name ')
    print(name_list)

for i in name_list:
    print(invitation, i)

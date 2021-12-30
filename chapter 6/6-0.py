d = {'apples': 15, 'bananas': 35, 'grapes': 12}

print(d['bananas'])
d ['oranges'] = 20
print(len(d))
print('grapes' in d)
print('kiwi' in d)
print(d.get('apples', 0))
print(d.get('kiwi', "there is no kiwis"))

d2 = {(3, 2): 15, (1, 3): 35, (7, 4): 12, (6, 1): 42, (5, 5): 19}
del d2[(1, 3)]
print(d2)

def add_fruit(inventory, fruit, quantity=0):
    """
    Adds quantity of fruit to inventory.

       >>> new_inventory = {}
       >>> add_fruit(new_inventory, 'strawberries', 10)
       >>> 'strawberries' in new_inventory
       True
       >>> new_inventory['strawberries']
       10
       >>> add_fruit(new_inventory, 'strawberries', 25)
       >>> new_inventory['strawberries']
       35
     """
    new_inventory = {}
    new_inventory ['strawberries'] = 10
    'strawberries' in new_inventory
    

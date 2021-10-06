#Robert Bayer
#Module 11 Class Activity 1

#1:
#a: 35
#b: 1
#c: True
#d: Error
#e: 0
#f: Error (Cannot sort dict_keys), then displays the fruit
#g: False

#2
def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity


# make these tests work...
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
# test that 'strawberries' in new_inventory
print("strawberries" in new_inventory)
# test that new_inventory['strawberries'] is 10
print(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, 'strawberries', 25)
# test that new_inventory['strawberries'] is now 35)
print(new_inventory["strawberries"] == 35)

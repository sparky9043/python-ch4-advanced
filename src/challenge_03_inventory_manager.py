inventory = ['keyboard', 'mouse', 'monitor', 'laptop', 'hdmi cable',
             'earhpones', 'pencil', 'paper']

updated_inventory = inventory[:]

updated_inventory.pop()
updated_inventory.pop()

updated_inventory.append('chips')
updated_inventory.append('sharpener')

print(inventory[-3:])
print(updated_inventory[-3:])

print(f"original count: {len(inventory)}")
print(f"updated count: {len(updated_inventory)}")
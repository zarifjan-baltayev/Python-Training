enemy = {
    'loc-x': 70,
    'loc-y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo'
}
enemy['rank'] = 'Admiral'
enemy['status'] = 'Active'
del enemy['rank']
enemy['loc-x'] = enemy['loc-x'] +40
enemy['health'] = enemy['health'] -15
if enemy['health'] < 80:
    enemy['color'] = 'yellow'
    enemy['status'] = 'Critical'.upper()

for x in enemy:
    print(x + " : \n\t\t " + str(enemy[x]))
print(enemy.keys())
print(enemy.values())
enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo',
    'awards': ['za Rodinu', 'za Sebe']
}
for n in enemy:
    print(n + ' : ' + str(enemy[n]))

all_enemies = []
for x in range(0, 10):
    all_enemies.append(enemy.copy())

all_enemies[5]['color'] = 'red'
all_enemies[5]['health'] -= 90
all_enemies[7]['loc_x'] += 50
all_enemies[7]['loc_y'] -= 40


for z in all_enemies:
    print(str(z) + '\n')
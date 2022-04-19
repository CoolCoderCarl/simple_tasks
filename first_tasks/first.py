string = "TEST"
car_stats = ['Bently', 121, {'color': 'red'}]

# Get color from third value of list
car_color = car_stats[2].get('color')

d1_classes = {'warrior': 'strength',
              'rogue': 'agility',
              'mage': 'intellect'
              }

digits = set('123')

print(car_stats[0])

if car_color == 'green':
    print(car_color)
elif len(digits) == 4:
    print(len(digits))
else:
    print(d1_classes)

i = 2
while i > 0:
    print(i)
    i -= 1

list_to_print = [0, 1, 2, 3, 4, 5]

for i in list_to_print:
    print(i, end=' ')

if 'E' in string:
    print('')
    print('pass')

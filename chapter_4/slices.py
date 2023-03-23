pizzas = ['calabresa', 'portuguesa', 'lombo canadense', 'milho e bacon', 'frango com catupiry']

print('The first three items in the list are:')

for pizza in pizzas[:3]:
    print(pizza)

print('The three items from the middle of the list are:')

for pizza in pizzas[1:4]:
    print(pizza)

print('The last three items from the list are:')

for pizza in pizzas[-3:]:
    print(pizza)

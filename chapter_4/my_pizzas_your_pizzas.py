my_pizzas = ['calabresa', 'portuguesa', 'lombo canadense', 'milho e bacon', 'frango com catupiry']

friend_pizzas = my_pizzas[:]

my_pizzas.append('pepperoni')

friend_pizzas.append('scarola')

print('My favorite pizzas are:')

for pizza in my_pizzas:
    print(pizza)

print('My friend favorete pizzas are:')

for pizza in friend_pizzas:
    print(pizza)

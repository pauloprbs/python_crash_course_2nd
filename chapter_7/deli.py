sandwich_orders = ['cheeseburger', 'baconburguer', 'pastrami', 'chickenburguer',
                    'tuna', 'cheeseburger', 'pastrami', 'baconburguer', 'pastrami']

finished_sandwiches = []

print("\nSorry, we're out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich.')
    finished_sandwiches.append(sandwich)

print('\nFinished sandwiches:\n')
print(finished_sandwiches)

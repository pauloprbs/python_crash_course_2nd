#3-4

guests = ['Dzargo', 'Daemon', 'Alvaro']

print(f'{guests[0]}, gostaria de jantar comigo?')
print(f'{guests[1]}, gostaria de jantar comigo?')
print(f'{guests[2]}, gostaria de jantar comigo?')

#3-5

print(f'\n{guests[1]} não pode ir.')

del guests[1]

guests.append('Scaridon')

print(f'{guests[0]}, gostaria de jantar comigo?')
print(f'{guests[1]}, gostaria de jantar comigo?')
print(f'{guests[2]}, gostaria de jantar comigo?')


#3-6

print('\nConsegui uma mesa maior.')

guests.insert(3, 'Cervo')
guests.insert(4, 'Helios')
guests.append('Kaito')

print(f'{guests[0]}, gostaria de jantar comigo?')
print(f'{guests[1]}, gostaria de jantar comigo?')
print(f'{guests[2]}, gostaria de jantar comigo?')
print(f'{guests[3]}, gostaria de jantar comigo?')
print(f'{guests[4]}, gostaria de jantar comigo?')
print(f'{guests[5]}, gostaria de jantar comigo?')


#3-7

print('\nMy table wont get ready in time.')

print(f'Sorry {guests.pop()}')
print(f'Sorry {guests.pop()}')
print(f'Sorry {guests.pop()}')
print(f'Sorry {guests.pop()}')

print(f'{guests[0]} ainda está convidado')
print(f'{guests[1]} ainda está convidado')

del guests[1]
del guests[0]

rivers = {
    'nile' : 'egypt',
    'amazonas' : 'brazil',
    'rio negro' : 'brazil'
}

for river, country in rivers.items():
    print(f'The {river} runs through {country}.')

for river in rivers.keys():
    print(river)

for country in set(rivers.values()):
    print(country)

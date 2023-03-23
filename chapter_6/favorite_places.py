favorite_places = {
    'paulo' : ['home', 'cafeteria', 'bar'],
    'felicia' : ['home', 'rua', 'praca'],
    'vania' : ['home', 'trabalho', 'praia']
}

for person, places in favorite_places.items():
    print(f"{person} likes")
    for place in places:
        print(place)
    print('\n')

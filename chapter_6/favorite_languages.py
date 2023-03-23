favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

should_take = ['sarah', 'paulo', 'renato']

for person in should_take:
    if person in favorite_languages.keys():
        print(f'Thank you {person.title()} for taking the poll.')
    else:
        print(f'{person.title()}, you should take the poll.')

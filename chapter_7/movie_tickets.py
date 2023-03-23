prompt = '\nEnter your age: '

while True:
    age = int(input(prompt))

    if age <= 3:
        print('Your ticket is free!')
    elif age <= 12:
        print('Your ticket will cost $10!')
    else:
        print('Your ticket will cost $15!')

    exec = input('\nContinue running(y/n)?')

    if exec == 'n':
        break

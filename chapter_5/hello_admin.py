usernames = ['admin', 'user1', 'user2', 'user3', 'user4', 'user5']

if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {username.title()}, thank you for logging again.')
else:
    print('We need to find some users!')

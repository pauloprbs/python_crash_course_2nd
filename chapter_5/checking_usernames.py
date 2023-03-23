current_users = ['user1', 'user2', 'user3', 'user4', 'user5']

new_users = ['user6', 'user2', 'user7', 'user4', 'user8']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'The username {new_user} is already in use.')
    else:
        print(f'The username {new_user} is available.')

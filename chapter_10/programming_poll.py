while True:
    reason = input("Why you like programming (q to quit)? ")

    if reason == 'q':
        break

    filename = "programming_poll.txt"

    with open(filename, 'a') as file_object:
        file_object.write(reason + '\n')
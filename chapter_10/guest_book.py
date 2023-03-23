while True:
    guest_name = input("Insert your name (q to quit): ")

    if guest_name == 'q':
        break

    filename = "guest_book.txt"

    with open(filename, 'a') as file_object:
        file_object.write(guest_name + '\n')
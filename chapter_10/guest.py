guest_name = input("Insert your name: ")

filename = "guest.txt"

with open(filename, 'w') as file_object:
    file_object.write(guest_name)
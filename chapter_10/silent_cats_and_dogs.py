cats_filename = 'cats.txt'
dogs_filename = 'dogs.txt'

try:
    with open(cats_filename) as cats:
        print("Names of cats:")
        for line in cats:
            print(line.rstrip())
    
    print()

    with open(dogs_filename) as dogs:
        print("Names of dogs:\n")
        for line in dogs:
            print(line.rstrip())
            
except FileNotFoundError:
    pass
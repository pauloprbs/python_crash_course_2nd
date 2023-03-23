while True:

    first_number = input("Enter the first number (q to quit): ")
    second_number = input("Enter the second number (q to quit): ")

    if first_number == 'q' or second_number == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("The inputs must be numbers")
    else:
        print(f"{first_number} + {second_number} = {answer}.")

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("The inputs must be numbers")
else:
    print(f"{first_number} + {second_number} = {answer}.")

from random import sample

lottery_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

#print("Any ticket matching these numbers or letters wins a prize.")

#print(sample(lottery_numbers, 4))

ticket = [0, 3, 9, 'c']

counter = 0

while True:
    counter += 1

    print("Any ticket matching these numbers or letters wins a prize.")

    result = sample(lottery_numbers, 4)

    print(result)

    if set(result) == set(ticket):
        break

print(f"I won after {counter} attemps with the ticket {ticket}")
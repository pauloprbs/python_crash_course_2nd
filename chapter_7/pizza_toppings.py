topping = ''
prompt = '\nEnter the topping we should add to the pizza'
prompt += '\n(Enter quit to stop adding toppings)'

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f'Adding {topping} to the pizza!')
    else:
        break

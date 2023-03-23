def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0)
        print(message)
        sent_messages.append(message)

messages = ['Hello world!', 'Good morning!', 'Good evening!', 'Hello, how are you?']
sent_messages = []

send_messages(messages, sent_messages)

print(messages)
print(sent_messages)

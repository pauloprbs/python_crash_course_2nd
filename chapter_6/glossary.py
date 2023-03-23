glossary = {
    'print' : 'prints something',
    'list' : 'data structure to store information',
    'integer' : 'type of integer number variable',
    'string' : 'type of text variable',
    'if' : 'conditional statement',
    'set' : 'stores data without duplicates',
    'dictionary' : 'stores key:value associated data',
    'float' : 'floating point number type',
    'sort' : 'arrange data in alphabetic order',
    'sorted' : 'data in order without change the original position'
}

# print(f'print: {glossary["print"]}\n')
# print(f'list: {glossary["list"]}\n')
# print(f'integer: {glossary["integer"]}\n')
# print(f'string: {glossary["string"]}\n')
# print(f'if: {glossary["if"]}\n')

for key, value in glossary.items():
    print(f'{key}: {value}\n')

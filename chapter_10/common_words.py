frank_filename = 'frankenstein.txt'
moby_filename = 'moby_dick.txt'
gatsby_filename = 'the_great_gatsby'

frank_count = 0
moby_count = 0
gatsby_count = 0

with open(frank_filename) as frank:
    frank_count = frank.read().lower().count('the')
#with open(moby_filename) as moby:
#    moby_count = moby.read().lower().count('the')
#with open(gatsby_count) as gatsby:
#    gatsby_count = gatsby.read().lower().count('the')

print("First results:")
print(f"Frankenstein: {frank_count}")
print(f"Moby Dick: {moby_count}")
print(f"The Great Gatsby: {gatsby_count}")

with open(frank_filename) as frank:
    frank_count = frank.read().lower().count('the ')
#with open(moby_filename) as moby:
#    moby_count = moby.read().lower().count('the ')
#with open(gatsby_count) as gatsby:
#    gatsby_count = gatsby.read().lower().count('the ')

print("Second results:")
print(f"Frankenstein: {frank_count}")
print(f"Moby Dick: {moby_count}")
print(f"The Great Gatsby: {gatsby_count}")
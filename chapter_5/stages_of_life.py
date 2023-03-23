age = 31

if age < 2:
    stage_of_life = 'baby'
elif age < 4:
    stage_of_life = 'toddler'
elif age < 13:
    stage_of_life = 'kid'
elif age < 20:
    stage_of_life = 'teenager'
elif age < 65:
    stage_of_life = 'adult'
else:
    stage_of_life = 'elder'

print(f'At the age of {age}, the person are a {stage_of_life}.')

lion_name = 'Simba'
lion_diet = 'Carnivore'
lion_fur_color = 'Brown'
lion_mane_color = 'Dark Brown'
lion_type = 'Lion'

parrot_name = 'Polly'
parrot_diet = 'Herbivore'
parrot_feather_color = 'Green'
parrot_vocab_size = 50
parrot_type = 'Parrot'

shark_name = 'Jaws'
shark_diet = 'Carnivore'
shark_scale_color = 'Gray'
shark_fin_size = 'Large'
shark_type = 'Shark'

if lion_type == 'Lion' or lion_type == 'Mammal':
    lion_sound = 'Generic Mammal Sound'
print(f"{lion_name} sound: {lion_sound}")

if parrot_type == 'Bird' or parrot_type == 'Parrot':
    parrot_sound = 'Chirp'
print(f"{parrot_name} sound: {parrot_sound}")

if shark_type == 'Fish' or shark_type == 'Shark':
    shark_sound = 'Glub'
print(f"{shark_name} sound: {shark_sound}")

if lion_type == 'Lion' or lion_type == 'Mammal':
    lion_walk = f"{lion_name} is walking."
print(lion_walk)

if lion_type == 'Lion' or lion_type == 'Mammal':
    lion_hunt = f"{lion_name} is hunting."
print(lion_hunt)

if shark_type == 'Shark' or shark_type == 'Fish':
    shark_hunt = f"{shark_name} is hunting."
print(shark_hunt)

if parrot_type == 'Bird' or parrot_type == 'Parrot':
    parrot_fly = f"{parrot_name} is flying."
print(parrot_fly)

if parrot_type == 'Parrot':
    parrot_talk = f"{parrot_name} is talking."
print(parrot_talk)

if shark_type == 'Shark' or shark_type == 'Fish':
    shark_swim = f"{shark_name} is swimming."
print(shark_swim)

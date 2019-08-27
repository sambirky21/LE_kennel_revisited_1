animals_in_kennel = [
    {
        "id": 1,
        "breed": "German Shepherd",
        "age": 3,
        "name": "Jack"
    },
    {
        "id": 2,
        "breed": "Siamese",
        "age": 9,
        "name": "Shy"
    },
    {
        "id": 3,
        "breed": "Labradoodle",
        "age": 5,
        "name": "Avett"
    },
    {
        "id": 4,
        "breed": "Shnauzer",
        "age": 1,
        "name": "Gypsy"
    },
]

# for key, value in animals_in_kennel.items():
#     result = f'Key {key} = {value}'
#     print(result)
#This didn't work because its a bunch of dictionaries in a list. So you have to pull everything out of the list first[] and then take that argument and loop over it again.

for animal in animals_in_kennel:
    for key, value in animal.items():
        print(f'Key "{key}" = {value}')


# Key "id" = 1
# Key "breed" = German Shepherd
# Key "age" = 3
# Key "name" = Jack
# Key "id" = 2
# Key "breed" = Siamese
# Key "age" = 9
# Key "name" = Shy
# Key "id" = 3
# Key "breed" = Labradoodle
# Key "age" = 5
# Key "name" = Avett
# Key "id" = 4
# Key "breed" = Shnauzer
# Key "age" = 1
# Key "name" = Gypsy
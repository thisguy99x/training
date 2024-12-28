houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

people = [
    {"name": "Harry", "house": houses[0]},
    {"name": "Cho", "house": houses[1]},
    {"name": "Draco", "house": houses[3]}
]



people.sort(key =lambda person: person["name"])

print(people)
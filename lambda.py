people = [
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Cho", "house":"Ravenlaw"},
    {"name":"Draco", "house":"Slytherin"},
]

people.sort(key=lambda person:person["name"])

print(people)
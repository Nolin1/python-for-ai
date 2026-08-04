person= {
    "name" : "Nolin",
    "age" : 23,
    "city" : "Dhaka",
    "job" : "Student",
    "can_drive" : True
}

print(person["city"])
print(person)

person["smoke"] = True
print(person)

del person["smoke"]
print(person)
student = {
    "Alice": {"Math": 89, "Finnish": 92},
    "Bob": {"Math": 77, "Science": 97},
    "Princess": {"Math": 67, "Finnish": 90},
    "Clary": {"Math": 90, "Finnish": 88},
    "Joshua": {"Math": 60, "Finnish": 89},
    "Tara": {"Physics": 55, "Finnish": 90},
}

print(student["Alice"]["Math"])
print(student["Bob"]["Science"])

student["Alice"]["History"] = 92
print(student["Alice"])

student["Bob"]["Math"] = 82

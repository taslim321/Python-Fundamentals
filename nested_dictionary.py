student = {
    "name" : "taslim amin",
    "subjects" : {
        "phy" : 97,
        "che" : 45,
        "math" : 56
    }
}
print(student["subjects"]["che"])
print(student.keys())
print(list(student.keys())) #type casting
print(len(list(student.keys()))) 
#value
print(student.values())
print(list(student.values()))
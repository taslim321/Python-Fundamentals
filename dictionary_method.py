student = {
    "name" : "taslim amin",
    "subjects" : {
        "phy" : 97,
        "che" : 45,
        "math" : 56
    }
}
print(student.keys())
print(student.values())
print(student.items()) #return pair as tuple
pair = list(student.items())
print(pair[0])
# print(student["name2"]) #error
print(student.get("name2")) #no error ->none
student.update({"city" : "dhaka"})
print(student)  #new pair add
new_dict = {
            "age" : "infinty"}
student.update(new_dict)
print(student)

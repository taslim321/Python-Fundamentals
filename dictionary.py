info = {
    "key" : "value",
    "age" : 30
}
info["key"] = "name change" # overwrite
info["new key"] = "last"   # new assign
# dictionary mutable
null_dict ={}  
print(type(info))
print(info["key"])
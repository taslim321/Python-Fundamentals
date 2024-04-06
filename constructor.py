class student:
    name = "karan"
    college_name = "juhlib"   # class attribute
    def __init__(self, fullname,age): 
        self.name= fullname   # obj attr >class attr
        self.age = age        # constructor
        print(self)
        print("adding new student in data base")
    
s1 =student("karan",99)
with open("demo.txt","a") as f:
    data = f.read()
with open("demo.txt","w") as f:
    data = f.write("Taslim Amin")

# with can be close file automatically 
    
# replace data
with open("demo.txt","r") as f:
    data = f.read()
    new_data = data.replace("java","python")  # java replace by py

with open("demo.txt","w") as f:
    data = f.write("new_data")

# find data
with open("demo.txt","r") as f:
    data = f.read()
    if(data.find("learning")==-1):
        print("found")
    else:
        print("not found")


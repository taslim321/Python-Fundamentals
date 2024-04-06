f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

# read one line at a time
line1 = f.readline()
line2 = f.readline()
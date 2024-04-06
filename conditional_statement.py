#conditional statement
#(if-elif-else)
age = 18
if(age>=18):
    print("adult")
elif(age<18):
    print("Not adult")
#exp
    marks = 80
if(marks>=90):
    print("A")

a = int(input("enter first number:")) 
b = int(input("enter second number:")) 
c = int(input("enter third number:")) 

if(a>=b and a>=c):
    print("first number is largest:", a)
elif(b>=c):
    print('second number is largest', b)
else:
    print("third number is largest", c)

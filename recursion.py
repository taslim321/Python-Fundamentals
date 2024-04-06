# when a function calls itself repeatedly
# recursive function
def show(n):
    if(n==0):    #base case
        return         # call stake concept
    print(n)
    show(n-1)

show(5)

# n factorial 
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
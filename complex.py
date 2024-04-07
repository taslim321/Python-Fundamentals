#polymorphism
#dunder function

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def create_number(self):
        print(self.real,"i +", self.img,"j")
    # def __add__(self,num2):
    # def __sub__(self,num2):
    # def __mul__(self,num2):


    
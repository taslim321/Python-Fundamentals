class Account:
    def __init__(self,acc_no , acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # __ for private

    def reset_pass(self):
        print(self.__acc_pass)
    
acc1 = Account("12345","abcd")

print(acc1.acc_no)
print(acc1.reset_pass())
# private method
class person:
    __name = "anonymous"   #__

    def __hello(self,name):
        print("Hello Person!")

    def welcome(self):
        self._hello()

p1 = person()

print(p1.__hello())
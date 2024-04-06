class car:
    @staticmethod
    def start():
        print("car start")

    @staticmethod
    def stop():
        print("car stop")

class toyota(car):   #inheritance  #single
    def __init__(self,brand_name):
        self.brand_name = brand_name

class fortune(toyota):  #multi-level 
    print("Hello car")

class all(car,toyota):  #multiple 
    print("khuh")

car1 = toyota("fortuner")


print(car1.start())
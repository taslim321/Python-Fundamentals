class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car start")

    @staticmethod
    def stop():
        print("car stop")

class toyota(car):
    def __init__(self,brand_name,type):
        self.brand_name = brand_name
        super().__init__(type)
        super().start()

car1 = toyota("hguh","gfyg")
print(car1.type)
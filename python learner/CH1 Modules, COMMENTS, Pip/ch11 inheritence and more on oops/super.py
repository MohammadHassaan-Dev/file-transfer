class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stoped")


class Bmw(Car):
    def __init__(self, type):
        super().__init__(type)

a = Bmw("Electric")
print(a.type)
        


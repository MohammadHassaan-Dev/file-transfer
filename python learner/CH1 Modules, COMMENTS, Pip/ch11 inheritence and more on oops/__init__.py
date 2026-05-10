class car:
    def __init__(self, car, color): #Init means (initialize)
        self.car = car
        self.color = color
        print("Car started!")

car = car("Swift", "White")   #Sometimes i write car = car for creating an object which is wrong the correct way for this is car = car()
print(car.car, car.color)

# 2. Write a class “Calculator” capable of finding square, cube and square root of a 
# number.

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square of {self.n} = {self.n*self.n}")

    def cube(self):
        print(f"Cube of {self.n} = {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"squareroot of {self.n} = {round(self.n**0.5, 3)}")

o = Calculator(2)
o.square()
o.cube()
o.squareroot()
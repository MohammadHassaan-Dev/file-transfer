# 4. Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square of {self.n} = {self.n*self.n}")

    def cube(self):
        print(f"Cube of {self.n} = {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"squareroot of {self.n} = {round(self.n**0.5, 3)}")

    @staticmethod
    def greet():
        print("Hello user!")


o = Calculator(2)

print(f"Number is ")
o.greet()
o.square()
o.cube()
o.squareroot()
# class Car:
#     pass

# obj1 = Car()
# obj1.brand = "Suzuki"
# obj1.color = "white"

# obj2 = Car()
# obj2.brand = "Toyota"
# obj2.color = "black"

# print(obj1.brand, obj1.color)
# print(obj2.brand, obj2.color)


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

obj1 = Student("Hassaan", 13, "A+")


obj2 = Student("Ali", 12, "B")


print(obj1.name, obj1.age, obj1.grade)
print(obj2.name, obj2.age, obj2.grade)


# class Player:
#     name = "Steve"
#     def jump(self):
#         print("Jumped")

# player = Player()
# print(player.name)
# player.jump()

# class Car:
#     pass

# c1 = Car()
# c1.brand = "Toyota"
# c1.speed = 120

# print(c1.brand)
# print(c1.speed)

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s1 = Student("Hassaan", 95)
# s2 = Student("Ali", 88)

# print(s1.name)
# print(s2.marks)

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         print("Dog is barking")

# d1 = Dog("Rocky", "Bulldog")
# d1.bark()


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def info(self):
#         print(f"{self.title} written by {self.author}")

# b1 = Book("Python Basics", "John")

# b1.info()

# class Person:
#     def introduce(self):
#         print("I am a person")

# class Student(Person):
#     def study(self):
#         print("Student is studying")

# s1 = Student()

# s1.introduce()
# s1.study()

# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Cat:
#     def sound(self):
#         print("Cat says meow")

# c1 = Cat()
# c1.sound()

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         print("Car is starting")


# c = Car()
# c.start()

# class Acc:
#     def __init__(self, balance):
#         self.__balance = balance

#     def bankbalance(self):
#         print(self.__balance)

#     def deposit(self, amount):
#         self.__balance += amount 

# acc = Acc(1500)
# acc.deposit(1000)
# acc.bankbalance()

# class Laptop:
#     def __init__(self, price):
#         self.__price = price


#     def set_price(self, price):
#         self.__price = price

#     def show_price(self):
#         print(self.__price)

# l = Laptop(50000)

# l.show_price()

# l.set_price(60000)

# l.show_price()
        
# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog:
#     def __init__(self, name, breed):
#         super.__init__(name)
#         self.breed = breed

# d = Dog("Rocky", "Bulldog")

# print(d.name)
# print(d.breed)

class Book:
    def __init__(self, weight1):
        self.weight1 = weight1

    def __add__(self, other):
        return Book(self.weight1 + other.weight1)

b1 = Book(100)
b2 = Book(200)

b3 = b1 + b2

print(b3.weight1)

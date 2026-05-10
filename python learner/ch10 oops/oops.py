class Person:
    def greet(self):
        print("Hello")
    
class Student(Person):
    def study(self):
        print("I am studying")

student = Student()
student.greet()
student.study()
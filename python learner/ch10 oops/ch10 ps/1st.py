# 1. Create a class “Programmer” for storing information of few programmers 
# working at Microsoft.


class Programmer:
    company = "microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Hassaan", 200000, 49793)
print(p.pin, p.salary, p.name, p.company)
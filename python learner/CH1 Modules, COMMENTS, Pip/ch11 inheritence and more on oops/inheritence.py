class employee:
    company = "ITC"
    def show(self):
        print(f"the name is {self.name}")

class programmer(employee):
    company = "ITC Info tech"

    def showlang(self):
        print(f"The name is {self.name} and he is good")

a = employee()
b = programmer()
print(a.company, b.company)

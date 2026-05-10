class employee:
    company = "ITC"
    def show(self):
        print(f"the name is {self.name}")

class Coder:
    lang = "Py"

class programmer(employee):
    company = "ITC Info tech"

    def showlang(self):
        print(f"The name is {self.name} and he is good")



a = employee()
b = programmer()
c = Coder()

print(a.company, b.company, c.lang)

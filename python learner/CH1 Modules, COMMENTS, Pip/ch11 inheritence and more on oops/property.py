class employee:
    a = 1
    @classmethod
    def show(self):
        print(f"The value of a(class) is {self.a}")

a = employee()
a.a = 45
a.name = "Harry"
print(a.name)
a.show()
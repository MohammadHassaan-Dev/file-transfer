# 1. Write a program to find the greatest of four numbers entered by the user

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

if (a>b and a>c and a>d):
    print(f"{a} is winner.")

elif (b>a and b>c and b>d):
    print(f"{b} is winner.")

elif (c>a and c>b and c>d):
    print(f"{c} is winner.")

elif (d>a and d>b and d>c):
    print(f"{d} is winner.")
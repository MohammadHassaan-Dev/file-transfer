# 6. Write a program to calculate the factorial of a given number using for loop.
a = int(input("Enter number: "))
product = 1
for i in range(1,a+1):
    product = product*i

print(product)
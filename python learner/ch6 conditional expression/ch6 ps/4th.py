# 4. Write a program to find whether a given username contains less than 10 
# characters or not.

a = input("Enter username: ")
b = len(a)
if(b>10):
    print("More than 10characters")

elif(b==10):
    print("Equals to 10")
else:
    print("Less than 10 characters")
# 7. Write a program to find out whether a given post is talking about “Harry” or not.

a = input("Enter your comment").lower()

if "harry" in a:
    print("this comment is talking about harry")

else:
    print("No this comment is not talking about harry!")
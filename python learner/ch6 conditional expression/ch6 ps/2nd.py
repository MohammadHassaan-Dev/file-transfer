# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

a = int(input("Enter marks of IS: "))
b = int(input("Enter marks of Math: "))
c = int(input("Enter marks of Eng: "))

totalp = (100)*(a + b +c)/300
if(totalp>=40 and a and b and c>=33):
    print("Pass")

else:
    print("Fail")
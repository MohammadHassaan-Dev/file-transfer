# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F


a = int(input("Enter marks: "))
if a>90:
    print("Ex")
    
elif a>80:
    print("A")

elif a>80:
    print("B")

elif a>70:
    print("C")

elif a>60:
    print("D")

elif a>50:
    print("F")

else:
    print("Something went wrong!")
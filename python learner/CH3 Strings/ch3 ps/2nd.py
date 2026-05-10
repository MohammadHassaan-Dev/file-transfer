# 2. Write a program to fill in a letter template given below with name and date.
letter = ''' Dear Harry,
You are selected!
24-11-2025
'''

a = letter.replace("Harry", "Hassaan").replace("24-11-2025", "18sept 2033")
print(a)
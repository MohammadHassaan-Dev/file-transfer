# 3. Check that a tuple type cannot be changed in python.

tuple = ("Hy", 1 ,2 )
z = tuple[1] = 10
print(z)

# ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 4, in <module>
# TypeError: 'tuple' object does not support item assignment

# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.

a = input("Enter comment: ").lower()
spam = ["make a lot of money", "buy now", "subscribe this", "click this"]
if(a in spam):
    print("May be spam")
else:
    print("Not a spam")
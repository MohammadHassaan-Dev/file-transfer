# 9. Write a program to find out whether a file is identical & matches the content of 
# another file.

with open("file.txt")as f:
    data1 = f.read()

with open("file.txt")as f:
    data2 = f.read()

if data1 == data2:
    print("Yes its identical")

else:
    print("No it is not identical and matches the content")


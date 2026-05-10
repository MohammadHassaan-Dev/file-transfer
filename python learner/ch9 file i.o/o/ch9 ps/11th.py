# 11. Write a python program to rename a file to “renamed_by_ python.txt.

with open("file.txt", "r")as f:
    data = f.read()

with open("renamed_by_file.txt", "w")as f:
    f.write(data)
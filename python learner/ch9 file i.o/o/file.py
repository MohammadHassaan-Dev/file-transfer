# a = open("hy.txt")
# b = a.read()
# print(b)
# a.close()

# a = "Hy hassaan are you learning python? Yes i am learning right now. hmm"
# b = open("python.txt", "w")
# c = b.write(a)
# b.close()

# f = open("hy.txt")
# f.readline()
# sec = f.readline()
# print(sec)

# imagine "hy.txt ke andar likha howa hai hy mera naam\n hassaan ni hai\n blke ali hai."


# f = open("hy.txt")
# data = f.readlines()
# print(data[1])

# # imagine "hy.txt ke andar likha howa hai hy mera naam\n hassaan ni hai\n blke ali hai."


f = open("hy.txt")
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close

# # imagine "hy.txt ke andar likha howa hai hy mera naam\n hassaan ni hai\n blke ali hai."
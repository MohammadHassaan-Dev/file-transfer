s = "python is easy and python is powerful".lower()
s = s.split()
dict = {}

for word in s:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

print(dict)
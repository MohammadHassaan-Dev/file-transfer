s = "I love python because python is easy and python is powerful".lower()
s = s.split()

dict ={}
for word in s:
    if word in dict:
        dict[word] += 1

    else:
        dict[word] = 1

for key,value in dict.items():
    if value > 1:
        print(f'{key} : {value}')
# print(dict)
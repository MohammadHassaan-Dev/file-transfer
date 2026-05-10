s = "Learning Python is fun".replace(" ","").lower()

count = {}


for word in s:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)
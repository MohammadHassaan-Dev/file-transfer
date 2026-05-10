with open("file.txt")as f:
    data = f.read().lower()
    a = data.split()
count = 0

for word in a:
    if word == "python":
        count += 1

print(f"Python -> {count}")
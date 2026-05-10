with open("file.txt")as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        print(f"It contains in line{i+1}:{line}")
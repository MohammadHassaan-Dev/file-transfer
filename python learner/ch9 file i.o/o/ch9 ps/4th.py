with open("replace.txt")as f:
    a = f.read()
    if "donkey" in a:
        b = a.replace("donkey", "******")
        with open("replace.txt", "w")as f:
            f.write(b)
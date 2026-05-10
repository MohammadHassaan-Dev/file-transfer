import random
def game():
    score =  random.randint(1,50)
    print(f"Your score is {score}")

    with open("hiscore.txt")as f:
        hiscore = f.read()
        if hiscore == "":
            hiscore = 0
        else:
            hiscore = int(hiscore)
        
    if score>hiscore :
        with open("hiscore.txt", "w")as f:
            f.write(str(score))

game()









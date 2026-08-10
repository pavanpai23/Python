import random

def game():
    print("you are playing a game")
    score=random.randint(1,100)
    with open ("chapter9_pratice.py/highscore.txt") as f:
        highscore=f.read()
        if(highscore!=""):
            highscore=int(highscore)
        else:
            highscore=0

    print(f"your score {score} ")
    if(score>highscore):
        with open("chapter9_pratice.py/highscore.txt","w") as f:
            f.write(str(score))

    return score

game()
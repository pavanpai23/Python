
import random
# """
# 1 for snake
# -1 for you
# 0 for gun
# """

computer=random.choice([1,0,-1])

youstr=input("enter your choice: ")
youdict={"s":1,"y":-1,"g":0}
reversedict={1:"snake",-1:"you",0:"gun"}

you=youdict[youstr]

print(f"you choice {reversedict [you]}\n computer choice {reversedict[computer]}")

if(computer==you):
    print("draw")
else:
    if(computer==-1 and you==1):
        print("YOU WIN")
    elif(computer==-1 and you==0):
        print("you loose")
    elif(computer==1 and you==-1):
        print("you loose")
    elif(computer==1 and you==0):
        print("you win")
    elif(computer==0 and you==-1):
        print("you win")
    elif(computer==0 and you==1):
        print("you loose")
    else:
        print("something went wrong")
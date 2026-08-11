import random
n=random.randint(1,100)
a=-1
guess=0
while(a!=n):
    guess+=1
    a=int(input("guess the number : "))
    if(a>n):
        print("lower num please")
    else:
        print("higher num please")

print(f"you have guessed the number {n} correctly in {guess} attempts")
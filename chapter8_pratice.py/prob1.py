def great(a,b,c):
    if(a>b and a>c):
        print("a is greater")
    elif(b>a and b>c):
        print("bis grater")
    else:
        print("c")

a=int(input("enter num : "))
b=int(input("enter num : "))
c=int(input("enter num : "))

great(a,b,c)
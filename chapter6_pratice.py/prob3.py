m1=int( input("enter marks 1 : "))
m2=int( input("enter marks 2 : "))
m3=int( input("enter marks 3 : "))

avg=((m1+m2+m3)/300)*100

if(avg>=40 and m1>=33 and m2>=33 and m3>=33):
    print("pass",avg)
else:
    print("failed",avg)
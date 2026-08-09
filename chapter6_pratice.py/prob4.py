p1="buy lot of money"
p2="buy now"
p3="subscribe now"
p4="click this"

message=input("enter your msg  : ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("spam msg")
else:
    print("not spam")
    
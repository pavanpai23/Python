try:
    a=int(input("enter a n0. :"))
    b=int(input("enter a n0. :"))
    print(a/b)
except ZeroDivisionError as e:
    print(e)

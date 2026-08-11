class employe():
    def __init__(self):
        print("constructor of employee")
    a=1
class programmer(employe):
    def __init__(self):
             print("constructor of programmer")
    b=2
class manager(programmer):
    def __init__(self):
            super().__init__()
            print("constructor of manager")
    c=3
    
# o=employe()
# print(o.a)
# # print(o.b) #error as b is not present in employee

# o=programmer()
# print(o.a,o.b)

o=manager()
print(o.a,o.b,o.c)
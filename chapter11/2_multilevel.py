class employe():
    a=1
class programmer(employe):
    b=2
class manager(programmer):
    c=3
o=employe()
print(o.a)
# print(o.b) #error as b is not present in employee

o=programmer()
print(o.a,o.b)

o=manager()
print(o.a,o.b,o.c)
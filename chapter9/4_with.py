f=open("chapter9/file.txt")
data=f.read()
print(data)
f.close()


# the same can be writtine using if statement like this
with open("chapter9/file.txt") as f:
    print(f.read())


# you dont have to explicity close the file
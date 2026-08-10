f=open("chapter9_pratice.py/file.txt")

data=f.read()

if("twinkel" in data):
    print("the word twinkel is present")
else:
    print("not present")

f.close()
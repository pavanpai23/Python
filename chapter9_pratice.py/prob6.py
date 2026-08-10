with open("chapter9_pratice.py/log.txt") as f:
    content=f.read()

if("python" in content):
    print("yes")
else:
    print("no")
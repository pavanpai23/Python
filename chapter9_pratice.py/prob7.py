with open("chapter9_pratice.py/this.txt", "r") as f:
    content=f.read()

with open("chapter9_pratice.py/copy_this.txt","w") as f:
    f.write(content)
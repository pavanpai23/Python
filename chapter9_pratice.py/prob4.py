word="donkey"

with open ("chapter9_pratice.py/file2.txt","r") as f:
    content=f.read()

newcontent=content.replace(word,'#####')

with open ("chapter9_pratice.py/file2.txt","w") as f:
    f.write(newcontent)
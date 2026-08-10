words=["donkey","good","friend","having"]

with open("chapter9_pratice.py/file2.txt","r") as f:
    content=f.read()

for word in words:
    content=content.replace(word,'####')


with open("chapter9_pratice.py/file2.txt","w") as f:
    f.write(content)
file = open("file.py")
content = file.read()
print(content)

file.seek(0)
lines = file.readlines()
print(lines)
file.close()

file = open("file.py", "w")

num = file.write(content)
print(num)
file.close()

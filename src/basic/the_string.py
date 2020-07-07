hello = "hello"
print("hello[0] =", hello[0])
print("hello[1, 2] =", hello[1:3])

print()
print("h in hello =", "h" in hello)
print("h not in hello =", "h" not in hello)

print()
print("my name is %s, I'm %d years old!" % ('xiaoming', 3))
print(f"{hello} world")

print()
# toLowerCase
print("hello.lower() =", hello.lower())
# toUpperCase
print("hello.upper() =", hello.upper())
# replace
print("hello.replace(l, 1) =", hello.replace("l", "1"))
# split
print("hello.split(l, 1) =", hello.split("l"))
# trim
print("hello.strip() =", hello.strip())
# indexOf
print("hello.find(l) =", hello.find("l"))
print("hello.find(w) =", hello.find("w"))
print("hello.rfind(l) =", hello.rfind("l"))


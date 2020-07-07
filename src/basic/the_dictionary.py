student = {"xiaoming": 18, "xiaohong": 17}
print("student =", student)
# size
print("len(student) =", len(student))

print()
# get(K key)
print(f'{student["xiaoming"] = }')
print(f'{student["xiaohong"] = }')
print(f'{student.get("xiaohong") = }')
# getOrDefault
print(f'{student.get("dazhuang", 19) = }')

print()
# put(K key, V value)
student["xiaohong"] = 16
student["dazhuang"] = 19
print("after put, student =", student)

print()
# remove(K key)
del student["dazhuang"]
print("after del, student =", student)

print()
# entrySet
items = student.items()
for k, v in items:
    print(f'{k}: {v}', end=" ")
print()
print("keys =", student.keys())

student.clear()
print("after clear, student =", student)

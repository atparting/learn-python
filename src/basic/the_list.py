animals = ["dog", "pig", "sheep"]

# size
print("len(animals) =", len(animals))

print()
print("[1, 2] + [3] =", [1, 2] + [3])
print("[1] * 3 =", [1] * 3)
# contains
print("3 in [1, 2, 3] =", 3 in [1, 2, 3])

print()
# for in
for x in [1, 2, 3]:
    print(x, end=" ")
print()

print()
print("animals[0] =", animals[0])
print("animals[-1] =", animals[-1])
print("animals[1:] =", animals[1:])

print()
# indexOf
print("animals.index(pig) =", animals.index("pig"))
# add
animals.append("bird")
print("after append(bird), animals =", animals)
# addAll
animals.extend(["panda", "cat"])
print("after extend([panda, cat]), animals =", animals)
# add(int index, T element)
animals.insert(2, "xiaoming")
print("after insert(2, xiaoming), animals =", animals)
# remove(Object element)
animals.remove("xiaoming")
print("after remove(xiaoming), animals =", animals)
# remove(int index)
del animals[2]
print("after del animals[2], animals =", animals)
# clear
animals.clear()
print("after clear, animals =", animals)


import sys

animals = ["dog", "pig", "sheep"]
animalsIter = iter(animals)

print("begin for in")
for animal in animalsIter:
    print(animal)

animalsIter = iter(animals)

print()
print("begin next")
while True:
    try:
        print(next(animalsIter))
    except StopIteration:
        sys.exit()

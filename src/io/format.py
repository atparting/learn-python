import math

animal = "panda"
print(f'str({animal}) = {str(animal)}')
print(f'repr({animal}) = {repr(animal)}')

print()
print("animal is {}".format(animal))
print("dog is {}, pig is {}".format("dog", "pig"))
print("pig is {1}, dog is {0}".format("dog", "pig"))
print("dog is {0}, pig is {pig}".format("dog", pig="pig"))
print("pi is {0:.2f}".format(math.pi))




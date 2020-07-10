animal = "panda"


def change_animal():
    global animal
    animal = "cat"
    print(animal)


change_animal()
print(animal)

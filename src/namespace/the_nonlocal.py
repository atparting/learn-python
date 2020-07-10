def print_animal():
    animal = "panda"
    print(animal)

    def print_animal2():
        nonlocal animal
        animal = "cat"
        print(animal)

    print_animal2()
    print(animal)


print_animal()

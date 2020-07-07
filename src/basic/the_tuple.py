animals = ("dog", "pig", "sheep")
print("type(animals) =", type(animals))

# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符
numbers = (1)
print("type((1)) =", type(numbers))
numbers = (1,)
print("type((1,)) =", type(numbers))
animalsList = list(animals)
print("type(animalsList) = ", type(animalsList))
animalsTuple = tuple(animalsList)
print("type(animalsTuple) = ", type(animalsTuple))

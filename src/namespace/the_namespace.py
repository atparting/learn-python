global_animal = "panda"


def print_animal():

    global_animal = "dog"  # 等于重新声明 未更改全局的 global_animal
    print(global_animal)

    if True:
        local_animal = "dog"
    print(local_animal)  # 和java不一样，if不重新生成作用域，所以这里能读到if中定义的global_animal

    def print_animal2():
        local_animal = "pig"  # 等于重新声明 未更改局部外的局部变量 local_animal
        print(local_animal)

    print_animal2()
    print(local_animal)


print_animal()
print(global_animal)

import random

animals = ["dog", "pig", "panda", "cat"]
animalsName = {"dog": "小狗", "pig": "小猪", "panda": "熊猫", "cat": "小猫"}
# for in
for animal in animals:
    if random.randrange(0, 2) == 0:
        print("这里好像没有，去下一个地方找吧")
        continue
    if animal == "panda":
        print("找到熊猫了！")
        break
    print("找到了" + animalsName[animal])
else:
    print("没找到熊猫...")
print()

# for i
for i in range(len(animals)):
    print(f'第{i + 1}只动物是{animalsName[animals[i]]}')

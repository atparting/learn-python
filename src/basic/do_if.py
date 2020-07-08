import random

rand = random.randrange(0, 3)
print("开奖了，这轮是：", end="")
if rand == 0:
    print("小")
elif rand == 1:
    print("中")
else:
    print("大")

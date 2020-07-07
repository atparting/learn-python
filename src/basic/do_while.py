import random

rand = random.randrange(0, 3)
while rand < 2:
    if rand == 0:
        print("等于0，退出循环")
        break
    print("等于1，重新随机")
    rand = random.randrange(0, 3)
else:
    print("等于2！")

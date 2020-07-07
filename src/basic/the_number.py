import math
import random

# 整型
i = 1
# 浮点型
f = 1.11
# 复数
c0 = complex(1, 2)
c1 = 1 + 2j

print(f'int({f}) = {int(f)}')
print(f'float({i}) = {float(i)}')
print("c0 == c1 ?", c0 == c1)

print()
print("pi =", math.pi)
print("e =", math.e)

print()
# 生成[0, 1)范围的随机数
print("random.random() =", random.random())
# 生成[start, stop)范围内的随机数
print("random.randrange(1, 10) =", random.randrange(1, 10))

print()
# 4舍6入5看齐,奇进偶不进
print("round(1.1) =", round(1.1))
print("round(1.5) =", round(1.5))
print("round(2.5) =", round(2.5))
# 向上取整
print("ceil(2.5) =", math.ceil(2.5))
# 向下取整
print("floor(2.5) =", math.floor(2.5))


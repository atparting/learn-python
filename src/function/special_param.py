"""
强制位置参数
/ 前的参数只能使用 指定位置参数
* 后的参数只能使用 关键字参数
/ 和 * 之间的参数可以使用 指定位置参数 或 关键字参数
"""


def print_sum(a, /, b, c, *, d):
    print(a + b + c + d)


print_sum(1, 2, c=3, d=4)

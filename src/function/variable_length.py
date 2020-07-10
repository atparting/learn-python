def print_sum(a, *numbers):
    print("type(numbers) =", type(numbers))
    for num in numbers:
        a += num
    print("total =", a)


print_sum(1, 2, 3, 4)


def print_every(a, **others):
    print("type(others) =", type(others))
    print("a =", a)
    items = others.items()
    for k, v in items:
        print(f'{k} = {v}')


print_every(1, b=2, c=3)

def fibonacci(count):
    a = 0
    b = 1
    fibonacci_list = []
    for i in range(count):
        fibonacci_list.append(a)
        temp = a
        a = b
        b = temp + b
    print(fibonacci_list)


fibonacci(10)
fibonacci(count=10)

a = 0
b = 1
count = 20
fibonacciList = []
for i in range(count):
    fibonacciList.append(a)
    temp = a
    a = b
    b = temp + b
print(fibonacciList)

def divide(dividend, divisor):
    try:
        if type(dividend) != int or type(divisor) != int:
            raise TypeError
        result = dividend / divisor
    except ZeroDivisionError:
        print("divisor can not be zero")
    else:
        print(f"{dividend} / {divisor} = {result}")
    finally:
        print()


divide(10, 5)
divide(10, 0)
divide(10.1, 1)

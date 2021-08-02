array = []


def Fibonacci(n):
    array.clear()
    if n == 0:
        return 0
    if n == 1:
        return 1
    array.append(0)
    array.append(1)
    for i in range(n-1):
        array.append(array[-1] + array[-2])
    return array[-1]


n = int(input())
print(Fibonacci(n))

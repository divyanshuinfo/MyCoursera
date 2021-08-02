PISANO = 60


def Fibonacci(n):
    if n < 2:
        return n

    n %= PISANO

    array = [1, 1]
    for _ in range(n):
        array.append((array[-1] + array[-2]) % 10)
    return (array[-1] - 1) % 10


n = int(input())

print(Fibonacci(n))

PISANO = 60


def Fibonacci(n, m):
    assert not n > m

    fib_mods = [0, 1]
    for _ in range(PISANO - 2):
        fib_mods.append((fib_mods[-1] + fib_mods[-2]) % 10)

    n %= PISANO
    m %= PISANO
    if m < n:
        m += PISANO

    array = 0
    for i in range(n, m + 1):
        array += fib_mods[i % PISANO]
    return array % 10


m, n = map(int, input().split())
print(Fibonacci(m, n) % 10)

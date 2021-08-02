n = int(input())
m = 10
fib_array = []
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


if n <= m:
    print(Fibonacci(n) % m)
    quit()

fib_array.append(0)
array.append(0 % m)
fib_array.append(1)
array.append(1 % m)
for item in range(2, n):
    fib_array.append(fib_array[-1]+fib_array[-2])
    array.append(fib_array[-1] % m)
    if array[-1] == 1 and array[-2] == 0:
        break
pisano = len(array)-2
fib = n % pisano
print(Fibonacci(fib) % m)

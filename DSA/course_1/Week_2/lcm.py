num1, num2 = list(map(int, input().split()))


def gcd1(a, b):

    n = a % b
    if n == 0:
        return b
    return gcd1(b, n)


print(int(num1*num2/gcd1(num1, num2)))

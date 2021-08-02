nums = sorted(list(map(int, input().split())), reverse=True)


def gcd1(a, b):

    n = a % b
    if n == 0:
        return b
    return gcd1(b, n)


print(gcd1(nums[0], nums[1]))

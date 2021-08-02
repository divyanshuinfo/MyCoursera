def pisano_num_mod10(n):
    p, c = 0, 1
    n = n % 60
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        for _ in range(2, n+1):
            p, c = c, (p + c) % 60
        return c


n = int(input())
print(pisano_num_mod10(n)*pisano_num_mod10(n+1) % 10)

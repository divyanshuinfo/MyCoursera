input = 28

n = input
count = 0
for i in range(n):
    if n >= 10:
        n -= 10
        count += 1
    elif n >= 5:
        n -= 5
        count += 1
    elif n > 0:
        n -= 1
        count += 1
        continue

print(count)

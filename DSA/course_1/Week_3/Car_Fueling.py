d = int(input())
m = int(input())
n = int(input())
stops = list(map(int, input().split()))
stops.append(d)
refils = 0
for i in range(n):
    pivot = 0
    if stops[i+1] - stops[i] > m:
        print("-1")
        quit()
    if stops[i] - pivot > m:
        i -= 1
        pivot = stops[i]
        refils += 1
print(refils)

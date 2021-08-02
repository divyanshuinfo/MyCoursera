n = int(input())
start, end, length = [], [], []
points = list()

def take_second(elem):
    return elem[1]

for i in range(n):
    Tstart, Tend = map(int, input().split())
    start.append(Tstart)
    end.append(Tend)
lst = list(zip(start, end))
lst = sorted(lst, key=take_second)
points.append(lst[0][1])
for i in lst:
    if i[0] > points[-1]:
        points.append(i[1])
print(len(points))
print(' '.join(map(str, points)))

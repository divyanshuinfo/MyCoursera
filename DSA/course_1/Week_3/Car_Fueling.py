max_distance = int(input())
max_coverable_distance = int(input())
N_of_stops = int(input())
stops = list(map(int, input().split()))
stops.append(max_distance)
refils = 0
try:
    for i in range(N_of_stops):
        pivot = 0
        if stops[i+1] - stops[i] > max_coverable_distance:
            print("-1")
            quit()
        if stops[i] - pivot > max_coverable_distance:
            i -= 1
            pivot = stops[i]
            refils += 1
except IndexError:
    print("-1")
    quit()
print(refils)

n, W = map(int, input().split())
Weight, Value, value_per_unit = [], [], []


def take_third(elem):
    return elem[2]


for i in range(n):
    TValue, TWeight = map(int, input().split())
    Weight.append(TWeight)
    Value.append(TValue)
    value_per_unit.append(TValue/TWeight)

lst = list(zip(Value, Weight, value_per_unit))
lst = sorted(lst, key=take_third, reverse=True)
max_value = 0

for i in range(n):
    if W == 0:
        break
    if lst[i][1] <= W:
        max_value += lst[i][0]
        W -= lst[i][1]
        continue
    else:
        max_value += (lst[i][2]*W)
        break
print(f'{max_value:.4f}')

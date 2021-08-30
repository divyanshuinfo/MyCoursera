input()
input1 = list(map(int, input().split()))
input()
input2 = list(map(int, input().split()))
input1.pop(0)
input2.pop(0)
for i in input2:
    if i in input1:
        print(input1.index(i), end=' ')
    else:
        print("-1", end=" ")


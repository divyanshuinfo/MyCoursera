n = int(input())
seq_a = list(map(int, input().split()))
seq_b = list(map(int, input().split()))

seq_a = sorted(seq_a, reverse=True)
seq_b = sorted(seq_b, reverse=True)
final = 0
for i in range(n):
    final+=(seq_a[i]*seq_b[i])
print(final)
n = int(input())
lst = list()
count =0
for i in range(1, n+1):
    lst.append(i)
    n-=i
    if n - i <= 0:
        break

print(len(lst))
lst[-1]+=n
print(" ".join(map(str, lst)))
        
    
    
         
def compute(line, n):
    dic = dict()
    for i in line:
        dic[i] = dic.get(i, 0) + 1
    a = max(dic, key=dic.get) 
    if dic[a] > n//2:
        return True
    else:
        return False

if __name__ == "__main__" :
    n = int(input())
    line1 = list(map(int,input().split()))
    flag = compute(line1, n)
    if flag:
        print(1)
    else:
        print(0)

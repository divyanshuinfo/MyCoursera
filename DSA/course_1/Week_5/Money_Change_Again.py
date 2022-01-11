def DPChange(money, coins):
    MinNumCoins = [0]*(money+1)
    MinNumCoins[0] = 0
    for m in range(1, money+1):
        MinNumCoins[m] = float('inf')
        for i in range(len(coins)):
            if m >= coins[i]:
                NumCoins = MinNumCoins[m - coins[i]] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
    return MinNumCoins[money]

def compute(n):
    coins = [1, 3, 4]
    return DPChange(n, coins)
    

if __name__ == "__main__" :
    n = int(input())
    print(compute(n))
    
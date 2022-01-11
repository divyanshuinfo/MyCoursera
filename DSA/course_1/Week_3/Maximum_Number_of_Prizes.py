def Compute_Maximum_Number_of_Prizes(n):
    lst = list()
    count =0
    for i in range(1, n+1):
        lst.append(i)
        n-=i
        if n - i <= 0:
            break

    l = len(lst)
    lst[-1]+=n
    s = " ".join(map(str, lst))
    #print(str(l)+ " " + str(s))
    return str(l) + "\n" + str(s)

if __name__ == '__main__':
    print(Compute_Maximum_Number_of_Prizes(int(input())))
        
    
         
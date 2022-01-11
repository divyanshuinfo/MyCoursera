def first(arr, low, high, x):
    if(high >= low):
        mid = low + (high - low) // 2
        if((mid == 0 or x > arr[mid - 1]) and arr[mid] == x):
            return mid
        elif(x > arr[mid]):
            return first(arr, (mid + 1), high, x)
        else:
            return first(arr, low, (mid - 1), x)

    return -1

def binary_search(array, low, high, val):
    if low > high:       # error case
        return -1
    mid = (low + high) // 2
    if val == array[mid]:
        return mid    
    elif val < array[mid]:
        return binary_search(array, low, mid-1, val)
    elif val > array[mid]:
        return binary_search(array, mid+1, high, val)
    else:
        return -1
    
def compute(line1, line2):
    a = []
    for i in line2:
        a.append(str(binary_search(line1,0, len(line1)-1, i )))
        pass
    return(" ".join(a))
    
    
    
if __name__ == "__main__" :
    n = input()
    line1 = list(map(int,input().split()))
    n = input()
    line2 = list(map(int, input().split()))
    print(compute(line1, line2))

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    starts.sort()
    ends.sort()
    n = len(ends)
    for i in range(len(points)):
        l = b_search(starts, points[i])
        while l+1 < len(starts) and starts[l+1] == points[i]:
            l += 1
        if l < len(starts) and starts[l] <= points[i]:
            l += 1
        r1 = b_search(ends, points[i])
        while ends[r1-1] == points[i] and r1 > 0:
            r1 -= 1
        r = n - r1
        cnt[i] = l+r-n

    return cnt


def b_search(a, x):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low+high)//2
        if(a[mid] == x):
            return mid+1
        elif (a[mid] < x):
            low = mid+1
        else:
            high = mid-1
    if x > a[mid]:
        return mid+1
    return mid

def naive_compute(s, p, segments, points):
    result = ""
    for i in range(p):
        count = 0
        for j in range(s):
            if points[i] in range(segments[j][0], segments[j][1]+1):
                count += 1
        result+= str(count)+" "
    return result[:-1]


def compute(s, p, segments, points):
    
    result = []
    line1 = []

    for i in segments:
        line1+=list(range(i[0], i[1]+1))
    dic = dict()
    for i in line1:
        dic[i] = dic.get(i, 0) + 1
    for j in points:
        result.append(str(dic.get(j, 0)))
    
    return " ".join(result)

if __name__ == "__main__" :
    s, p = list(map(int, input().split()))
    segment1, segment2 = [], []
    for i in range(s):
        s1, s2 = list(map(int, input().split()))
        segment1.append(s1)
        segment2.append(s2)
    
    points = list(map(int, input().split()))
    
    cnt = fast_count_segments(segment1, segment2, points)
    for x in cnt:
       print(x, end=' ')
    
def compute(line1, line2):
    m = len(line1)
    n = len(line2)

    # declaring the array for storing the dp values
    matrix = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif line1[i-1] == line2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]+1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    # L[m][n] contains the length of LCS of line1[0..n-1] & line2[0..m-1]
    return matrix[m][n]

if __name__ == "__main__":
    n = input()
    line1 = list(map(int, input().split()))
    n = input()
    line2 = list(map(int, input().split()))
    print(compute(line1, line2))

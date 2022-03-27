def compute(line1, line2, line3):
    matrix = [[[0 for i in range(len(line3)+1)] for j in range(len(line2)+1)]
                  for k in range(len(line1)+1)]
    
    for i in range(len(line1)+1):
        for j in range(len(line2)+1):
            for k in range(len(line3)+1):
                if (i == 0 or j == 0 or k == 0):
                    matrix[i][j][k] = 0

                elif (line1[i-1] == line2[j-1] and
                      line1[i-1] == line3[k-1]):
                    matrix[i][j][k] = matrix[i-1][j-1][k-1] + 1

                else:
                    matrix[i][j][k] = max(max(matrix[i-1][j][k],
                                         matrix[i][j-1][k]),
                                     matrix[i][j][k-1])

    return matrix[len(line1)][len(line2)][len(line3)]

if __name__ == "__main__":
    n = input()
    line1 = list(map(int, input().split()))
    n = input()
    line2 = list(map(int, input().split()))
    n = input()
    line3 = list(map(int, input().split()))
    print(compute(line1, line2, line3))

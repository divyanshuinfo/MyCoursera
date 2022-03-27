def compute(str1, str2):
    matrix = [[float("inf")]*(len(str2)+1) for _ in range(len(str1) + 1)]
 
    for j in range(len(str2)+1):
        matrix[len(str1)][j] = len(str2) - j
    for i in range(len(str1) + 1):
        matrix[i][len(str2)] = len(str1) - i
    
    for i in range(len(str1) - 1, -1, -1):
        for j in range(len(str2) -1, -1, -1):
            if str1[i] == str2[j]:
                matrix[i][j] = matrix[i + 1][j + 1]
            else:
                matrix[i][j] = 1 + min(matrix[i + 1][j], matrix[i][j+1], matrix[i+1][j+1])
    return matrix[0][0]


if __name__ == "__main__":
    str1 = input()
    str2 = input()
    print(compute(str1, str2))

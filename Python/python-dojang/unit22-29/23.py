def toCountMatrix(col:int, row:int, matrix:list):
    countMatrix = [[0] * col for i in range(row)]
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '*':
                countMatrix[i][j] = '*'
                continue
            
            count = 0
            for r in range(i-1, i+2):
                for c in range(j-1, j+2):
                    if r < 0 or c < 0 or r >= row or c >= col:
                        continue
                    if matrix[r][c] == '*':
                        count += 1

            countMatrix[i][j] = count

    return countMatrix

(col, row) = [int(i) for i in input().split()]

matrix = []
for i in range(row):
    matrix.append(list(input()))

countMatrix = toCountMatrix(col, row, matrix)

for r in countMatrix:
    for j in r:
        print(j, end='')
    print()
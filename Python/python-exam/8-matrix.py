from random import *
import copy

row, col = 5, 5
mat = [[randint(1, 4) for j in range(col)] for i in range(row)]
mat_star = copy.deepcopy(mat)

# mat into mat_star (row)
for r in range(1, row-1):
    for c in range(col):
        if mat[r-1][c] == mat[r][c] and mat[r][c] == mat[r+1][c]:
            mat_star[r][c] = '*'
            mat_star[r-1][c] = '*'
            mat_star[r+1][c] = '*'

# mat into mat_star (col)
for r in range(row):
    for c in range(1, col-1):
        if mat[r][c+1] == mat[r][c] and mat[r][c] == mat[r][c-1]:
            mat_star[r][c] = '*'
            mat_star[r][c-1] = '*'
            mat_star[r][c+1] = '*'

'''
# print mat
for r in range(row):
    for c in range(col):
        print(mat[r][c], end='')
    print()
'''

# print mat_star
for r in range(row):
    for c in range(col):
        print(mat[r][c], end='')
    print('        ', end='')

    for c in range(col):
        print(mat_star[r][c], end='')
    print()

# 행렬찾기
# D4
import sys
sys.stdin = open('input_1258.txt')

def find_sub_matrix(r, c):
    height, width = 0, 0
    for i in range(r, n):
        if matrix[i][c]: height += 1
        else: break
    for i in range(c, n):
        if matrix[r][i]: width += 1
        else: break
    for i in range(r, height + r):
        for j in range(c, width + c):
            matrix[i][j] = 0
    sub_matrices.append([height, width])

def sort_sub_matrix():
    for i in range(len(sub_matrices)):
        for j in range(len(sub_matrices) - (i+1)):
            now_size = sub_matrices[j][0] * sub_matrices[j][1]
            next_size = sub_matrices[j+1][0] * sub_matrices[j+1][1]
            if now_size > next_size:
                sub_matrices[j], sub_matrices[j+1] = sub_matrices[j+1], sub_matrices[j]
            elif now_size == next_size:
                if sub_matrices[j][0] > sub_matrices[j+1][0]:
                    sub_matrices[j], sub_matrices[j + 1] = sub_matrices[j + 1], sub_matrices[j]


for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    # print(matrix)

    cnt = 0
    sub_matrices = list()
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                cnt += 1
                find_sub_matrix(i, j)
    # print(cnt, sub_matrices)

    sort_sub_matrix()
    print("#{} {}".format(tc, cnt), end=" ")
    for sm in sub_matrices:
        print(*sm, end=" ")
    print()

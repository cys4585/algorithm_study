# 파스칼의 삼각형
# D2
import sys
sys.stdin = open('input_2005.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(i+1):
            if j == 0 or i == j:
                arr[i][j] = 1
            else:
                if i > 0 and j > 0:
                    arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()

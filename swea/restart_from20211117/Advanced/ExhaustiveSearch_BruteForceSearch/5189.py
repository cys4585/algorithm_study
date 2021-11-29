import sys
sys.stdin = open('./5189_sample_input.txt', 'r')

def my_func(n, sum_v):
    global result

    if result and result < sum_v: return
    if n == 0 and visited[n]:
        if not result or result > sum_v: result = sum_v
        return

    for i in range(N):
        if visited[i]: continue
        if n == i: continue
        if i == 0 and 0 in visited[1:]: continue
        visited[i] = 1
        my_func(i, sum_v + table[n][i])
        visited[i] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    result = None
    visited = [0] * N
    my_func(0, 0)

    print(f'#{tc} {result}')
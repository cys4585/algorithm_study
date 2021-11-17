import sys
sys.stdin = open('./4836_sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    area = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                area[r][c] += color

    cnt = 0
    for arr in area:
        cnt += arr.count(3)

    print(f'#{tc} {cnt}')
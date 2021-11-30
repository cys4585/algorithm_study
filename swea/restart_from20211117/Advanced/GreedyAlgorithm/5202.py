import sys
sys.stdin = open('./5202_sample_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    schedule = [list(map(int, input().split())) for _ in range(N)]
    schedule.sort(key=lambda x: x[1] - x[0])

    table = [0] * 24
    cnt = 0

    for s, e in schedule:
        for i in range(s, e):
            if table[i]: break
        else:
            for i in range(s, e): table[i] = 1
            cnt += 1
    print(f'#{tc} {cnt}')